from multiprocessing import Process
import os
import math
import time

def calc():
    for i in range(0,9000000):
        math.sqrt(i)

#Για να αποφύγουμε την αναδρομική δημιουργία processes στα windows βάζουμε
#την παρακάτω γραμμή κώδικα οπου εξασφαλίζουμε την εκτέλεση του main module στην αρχή
if __name__ == '__main__':
    timeStart = time.time()
    process_list = []

    for i in range(os.cpu_count()):
        print('Καταχώρηση Process Νο: %d' %i)    
        process_list.append(Process(target=calc))

    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    timeEnd = time.time()
    totalTime = timeEnd-timeStart
    #Τυπώνουμε πόσα δευτερόλεπτα πήρε η εκτέλεση του προγράμματος
    print("Συνολικός Χρόνος Εκτέλεσης σε δευτερόλεπτα : "+str(totalTime))