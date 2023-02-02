import openpyxl
import os
from openpyxl.chart import BarChart, Reference
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

# Create a bar chart
data = Reference(sheet, min_col=2, min_row=1, max_col=3, max_row=2)
categories = Reference(sheet, min_col=1, min_row=2, max_row=2)
chart = BarChart()
chart.add_data(data)
chart.set_categories(categories)
sheet.add_chart(chart, 'E1')

#Save the file
workbook.save('selvstudie\Daniel\Testing.xlsx') 


