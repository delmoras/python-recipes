import threading
import os
import math
import time

def calc():
    for i in range(0,9000000):
        math.sqrt(i)

timeStart = time.time()
thread_list = []

#θα δημιουργήσουμε τόσα threads οσα και τα cores του επεξεργαστή μας
for i in range(os.cpu_count()):
    print('Καταχώρηση Thread Νο: %d' %i)    
    thread_list.append(threading.Thread(target=calc))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

timeEnd = time.time()
totalTime = timeEnd-timeStart
#Τυπώνουμε πόσα δευτερόλεπτα πήρε η εκτέλεση του προγράμματος
print("Συνολικός Χρόνος Εκτέλεσης σε δευτερόλεπτα : "+str(totalTime))