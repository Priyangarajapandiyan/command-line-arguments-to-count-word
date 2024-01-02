#program is developed: R PRIYANGA
# REF.NO: 23013772
import sys
count= 0
with open(sys.argv[1],'r') as file:
    for line in file:
        word= line.split()
        count += len(word)

print("word count in file = ",count)