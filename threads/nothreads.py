import os
import math
import time

def calc():
    for i in range(0,9000000):
        math.sqrt(i)

timeStart = time.time()


#Εδω εκτελούμε την συνάρτηση calc σειριακά τόσες φορές όσα και τα cores του επεξεργαστή μας
for i in range(os.cpu_count()):
    print('Εκτέλεση συνάρτησης calc επανάληψη Νο. : %d' %i)    
    calc()


timeEnd = time.time()
totalTime = timeEnd-timeStart
#Τυπώνουμε πόσα δευτερόλεπτα πήρε η εκτέλεση του προγράμματος
print("Συνολικός Χρόνος Εκτέλεσης σε δευτερόλεπτα : "+str(totalTime))