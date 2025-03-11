from chase import chase
from openpyxl import Workbook, load_workbook
from citi import citi
from american import american_express
from aspire import aspire
import us

# Create a new workbook
# wb = Workbook()
# ws = wb.active

# # Write data to cells
# ws['A1'] = 'Name'
# ws['B1'] = 'Age'
# ws['A2'] = 'John'
# ws['B2'] = 30

# # Save the workbook
# wb.save('example.xlsx')

# Load an existing workbook
wb = load_workbook('data.xlsx')
ws = wb.active

# Read data from cells
# name = ws['A2'].value
# age = ws['B2'].value
# print(f"Name: {name}, Age: {age}")

# Iterate through rows
# ws['G2'] = '512334241'
# ws['G3'] = '619405542'
# ws['D2'] = 'Trythisout4200@outlook.com'
# ws['D3'] = 'pytcli21@outlook.com'
# ws['I2'] = 'Lawrence Township'
# ws['K2'] = '08648'
# ws['J2'] = 'New Jersey'
# wb.save('dummy_data.xlsx')
for row in ws.iter_rows(min_row=2, values_only=True):
    name = row[0]
    lastname = row[1]
    address = row[2]
    email = row[3]
    phone = row[4]
    dob = row[5]
    ssn = f'{row[6]}'
    annual_income = row[7]
    city = row[8]
    state = row[9]
    zipcode = row[10]
    coverage_addendum = bool(row[11])
    credit_protection = bool(row[12])
    consent = bool(row[13])
    mothers_name = row[14]
    residence_own = row[15]
    primary_income = row[16]
    # print(primary_income)
    # delta(
    #     first_name=name,
    #     last_name=lastname,
    #     email=email,
    #     username=username,
    #     password="Pikachu123",
    #     confirm_password="Pikachu123",
    #     dob=dob,
    #     address=address,
    #     city=city,
    #     state=state,
    #     zip_code=zipcode,
    #     phone_number=phone
    # )
    citi(
        firstname=name,
        lastname=lastname,
        ssn=ssn,
        dob=dob,
        address=address,
        zip=zipcode,
        phone=phone,
        email=email,
        income=annual_income
    )
    american_express(
        firstname=name,
        lastname=lastname,
        ssn=ssn,
        dob=dob,
        address=address,
        zip=zipcode,
        phone=phone,
        email=email,
        income=annual_income,
        source=primary_income,
        # state=state,
        # city=city
    )
    chase(
        firstname=name,
        lastname=lastname,
        mother_maiden_name=mothers_name,
        address=address,
        city=city,
        state=f'{us.states.lookup(state).abbr}',
        zip=zipcode,
        email=email,
        phone=phone,
        dob=dob,
        ssn=ssn,
        residence=residence_own,
        source=primary_income,
        income=annual_income
    )
    aspire(
        firstname=name,
        lastname=lastname,
        address=address,
        city=city,
        state= f'{us.states.lookup(state).abbr} - {state}',
        zip=zipcode,
        email=email,
        phone=phone,
        dob=dob,
        ssn=ssn,
        annual_income=annual_income,
        coverage_addendum=False,
        credit_protection=False,
        consent=consent
    )


# Add a new sheet
# new_sheet = wb.create_sheet("Sheet2")

# # Save changes
# wb.save('example.xlsx')