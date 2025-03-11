import win32com.client
import datetime
import pytz
import os
import pickle
import time
import re
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
# https://docs.google.com/spreadsheets/d/1_QHX_A9lJPRBeZmDQUMv6MCphKEWrw5gVBTtYCzfxYk/edit?usp=sharing
url = os.getenv("DB_URL")
key = os.getenv("DB_KEY")
supabase: Client = create_client(url, key)

def get_last_checked_time(account_name):
    try:
        if os.path.exists(f"last_checked_time_{account_name}.pickle"):
            with open(f"last_checked_time_{account_name}.pickle", "rb") as f:
                last_checked_time = pickle.load(f)
                return datetime.datetime.fromisoformat(last_checked_time)
    except Exception as e:
        print(f"Error loading last checked time for {account_name}: {e}")
    return datetime.datetime.now() - datetime.timedelta(days=1)

def save_last_checked_time(account_name, last_checked_time):
    try:
        with open(f"last_checked_time_{account_name}.pickle", "wb") as f:
            pickle.dump(last_checked_time.isoformat(), f)
    except Exception as e:
        print(f"Error saving last checked time for {account_name}: {e}")

def extract_verification_code(body):
    match = re.search(r"Verification Code:\s*(\d+)", body)
    if match:
        return match.group(1)
    return None

def extract_receiver_name(body):
    match = re.search(r"Dear (\w+),", body)
    if match:
        return match.group(1)
    return "Unknown"

def insert_otp_to_supabase(name, email_address, otp):
    try:
        response = supabase.table("otp_data").insert({
            "name": name,
            "email_address": email_address,
            "otp": otp
        }).execute()

        if response.status_code == 201:
            print(f"Inserted OTP for {name} ({email_address}) successfully.")
        else:
            print(f"Failed to insert OTP data: {response.data}")
    except Exception as e:
        print(f"Error inserting OTP into Supabase: {e}")

# def check_new_emails(account, last_checked_time):
#     outlook = win32com.client.Dispatch("Outlook.Application")
#     namespace = outlook.GetNamespace("MAPI")
#     local_tz = pytz.timezone("America/New_York")

#     if last_checked_time.tzinfo is None:
#         time_window = local_tz.localize(last_checked_time)
#     else:
#         time_window = last_checked_time

#     try:
#         print(f"Checking account: {account.Name}")
#         inbox = account.Folders["Inbox"]
#         messages = inbox.Items
#         messages.Sort("[ReceivedTime]", True)

#         for msg in messages:
#             if msg.ReceivedTime > time_window:
#                 if msg.Subject == "Aspire Verification Code":
#                     sender = msg.SenderName if msg.SenderName else "No Sender"
#                     received_time = msg.ReceivedTime.strftime("%Y-%m-%d %H:%M:%S") if msg.ReceivedTime else "No Time"
#                     body = msg.Body if msg.Body else "No Body"
#                     print(f"New email from {sender}: {received_time}")
#                     receiver_name = extract_receiver_name(body)
#                     print(f"Receiver Name: {receiver_name}")
#                     verification_code = extract_verification_code(body)
#                     if verification_code:
#                         print(f"Verification Code: {verification_code}")
#                         insert_otp_to_supabase(receiver_name, msg.SenderEmailAddress, verification_code)

#                 last_checked_time = msg.ReceivedTime

#         save_last_checked_time(account.Name, last_checked_time)

#     except Exception as e:
#         print(f"An error occurred while checking the account '{account.Name}': {e}")

def check_new_emails(account, last_checked_time):
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    local_tz = pytz.timezone("America/New_York")

    if last_checked_time.tzinfo is None:
        time_window = local_tz.localize(last_checked_time)
    else:
        time_window = last_checked_time

    try:
        print(f"Checking account: {account.Name}")
        inbox = account.Folders["Inbox"]
        deleted_items = account.Folders["Deleted Items"]
        messages = inbox.Items
        messages.Sort("[ReceivedTime]", True)

        for msg in messages:
            if msg.ReceivedTime > time_window:
                if msg.Subject == "Aspire Verification Code":
                    sender = msg.SenderName if msg.SenderName else "No Sender"
                    received_time = msg.ReceivedTime.strftime("%Y-%m-%d %H:%M:%S") if msg.ReceivedTime else "No Time"
                    body = msg.Body if msg.Body else "No Body"
                    print(f"New email from {sender}: {received_time}")
                    receiver_name = extract_receiver_name(body)
                    print(f"Receiver Name: {receiver_name}")
                    verification_code = extract_verification_code(body)
                    if verification_code:
                        print(f"Verification Code: {verification_code}")
                        insert_otp_to_supabase(receiver_name, msg.SenderEmailAddress, verification_code)
                    
                    # Move the message to Deleted Items folder
                    msg.Move(deleted_items)
                    print(f"Moved email to Deleted Items folder")

                last_checked_time = msg.ReceivedTime

        save_last_checked_time(account.Name, last_checked_time)

    except Exception as e:
        print(f"An error occurred while checking the account '{account.Name}': {e}")


if __name__ == "__main__":
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    accounts = namespace.Folders

    while True:
        for account in accounts:
            last_checked_time = get_last_checked_time(account.Name)
            check_new_emails(account, last_checked_time)
        print("Waiting for the next check...")
        time.sleep(30)
