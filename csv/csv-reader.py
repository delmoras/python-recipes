import csv

with open('us-500.csv','r+',newline='') as csvFile:
    csvReader = csv.reader(csvFile)    
    for row in csvReader:
        print(str(row))
