import csv 

students =      [
                    {'firstname':'John','lastname':'Moras','Gender':'Male','Address':'Episkopou Amvrosiou 5','City':'Thessaloniki'},
                    {'firstname':'George','lastname':'Dimitriou','Gender':'Male','Address':'Aristotelous 4','City':'Veroia'},
                    {'firstname':'Dimitris','lastname':'Georgiou','Gender':'Male','Address':'Michael Logiou 5','City':'Naoussa'},
                    {'firstname':'Petros','lastname':'Papadopoulos','Gender':'Male','Address':'Pyrrou 6','City':'Athens'}
                ]
with open('students.csv','w+',newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    #Παίρνουμε τα keys του 1oυ dictionary τα οποία θα χρησιμοποιήσουμε σαν κεφαλίδες στο csv
    headers = [*students[0]]
    csvWriter = csv.DictWriter(csvFile, fieldnames=headers)
    csvWriter.writeheader()
    for student in students:
        csvWriter.writerow(student)

with open('students.csv','r+',newline='') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print(str(row))

    
        


   
