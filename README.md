# command-line-arguments-to-count-word
## AIM:
To write a python program for getting the word count from the contents of a file using command line arguments.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
### Step 1:
Import numpy as np
### Step 2: 
 Enter the input values
### Step 3: 
Write python program for getting the word  count from the contenta of a file using command line arguments
### Step 4:  
Run the program
### Step 5: 
Input the values
### Step 6: 
End the program
## PROGRAM:
```
#program is developed: R PRIYANGA
#REF.NO: 23013772
import sys
count= 0
with open(sys.argv[1],'r') as file:
    for line in file:
        word= line.split()
        count += len(word)
print("program is developed: Pavithra R")
print("word count in file = ",count)
```
### OUTPUT:
![output](photo.png)


## RESULT:
Thus the program is written to find the word count from the contents of a file using command line arguments.
