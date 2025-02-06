from openpyxl import Workbook, load_workbook

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
wb = load_workbook('dummy_data.xlsx')
ws = wb.active

# Read data from cells
# name = ws['A2'].value
# age = ws['B2'].value
# print(f"Name: {name}, Age: {age}")

# Iterate through rows
for row in ws.iter_rows(min_row=2, values_only=True):
    name = row[0]
    lastname = row[1]
    address = row[2]
    city = row[3]
    state = row[4]
    zip = row[5]
    email = row[6]
    phone = row[7]
    dob = row[8]
    ssn = row[9]
    annual_income = row[10]
    

# Add a new sheet
# new_sheet = wb.create_sheet("Sheet2")

# # Save changes
# wb.save('example.xlsx')