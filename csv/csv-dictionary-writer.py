import csv

#Διαβάζει τα περιεχόμενα ενός CSV αρχείου
def csvRead(file):
    with open(file,'r+',newline='') as csvFile:
        csvReader = csv.reader(csvFile)    
        for row in csvReader:
            print(str(row))

#Γράφει σε ένα CSV αρχείο τα περιεχόμενα ενός Dictionary
def csvWrite(file,dictionary):
    with open(file,'w+',newline='') as csvFile:
        csvWriter = csv.writer(csvFile)        
        headers = [*dictionary[0]]
        csvWriter = csv.DictWriter(csvFile, fieldnames=headers)
        csvWriter.writeheader()
        for student in dictionary:
            csvWriter.writerow(student)

def test_run():
    #αρχικοποίηση λίστας που θα κρατάει τα dictionaries
    studentList = []
    
    #boolean μεταβλητή με την οποία ανάλογα το περιεχόμενό της θα τερματίζει ή θα συνεχίζει
    flowStatus = True

    while flowStatus:
        
        #Ζητάμε από τον χρήστη να συμπληρώσει τιμές
        firstname = input("Student Firstname: ")
        lastname  = input("Student Lastname: ")
        gender    = input("Gender: ")
        address   = input("Address: ")
        city      = input("City: ")
        
        #Προσθέτουμε το dictionary στην λίστα που δημιουργήσαμε πιο πάνω
        studentList.append({
            "name"      :firstname,
            "lastname"  :lastname,
            "gender"    :gender,
            "address"   :address,
            "city"      :city
        })
        
        #Ρωτάμε τον χρήστη εαν θέλει να καταχωρήσει άλλη εγγραφή
        userflowStatus = input("Do you want to continue y/n? ")
        if userflowStatus != 'y':
            flowStatus = False
        
    #Εγγραφή του χρήστη στο αρχείο
    csvWrite('students.csv',studentList)

    #Ανάγνωση αρχείου
    csvRead('students.csv')
test_run()







