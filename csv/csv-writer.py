#Python Recipe 1
#CSV WRITER
import csv

rows = [["John","Moras","DTEK","Episkopou Amvrosiou 5","Thessaloniki","Macedonia","Thessaloniki","54630","6993054642","2316777065","john@moras.gr","https://dtek.gr"],
["George","Tester","Phoneparts","Agiou Dimitriou 5","Thessaloniki","Macedonia","Thessaloniki","54630","6393574699","2310757666","dont@spam.gr","https://phoneparts.gr"]]
print(type(rows))
with open('us-500.csv','a+',newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    for row in rows:
        csvWriter.writerow(row)

