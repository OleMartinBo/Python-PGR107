import openpyxl
#Make the excel file
workbook = openpyxl.Workbook()
sheet = workbook.active

# Insert into sheets
sheet['A1'] = 'name' 
sheet['B1'] = 'age'  
sheet['C1'] = 'city' 
sheet['A2'] = 'Daniel Hope' 
sheet['B2'] = 21
sheet['C2'] = 'Bømlo' 

#Save the file
workbook.save('Testing.xlsx') 

