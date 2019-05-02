#!/usr/bin/python3


"""

Assignment:
 a small function that generates a sequential alphanumeric ID number using an 
 immutable prefix and an integer component, from a prompt for an integer. 
 
The output needs to increment the numeric component by 1 until it equals the 
number of the integer given at input. For example; if the input is 3, it 
will generate three alphnumeric numbers so XXX0001, XXX0002, XXX0003.

"""


try:
 
    a_num = int(input("Enter a number:  "))
 
# Check for non-float

except ValueError as e:
 
    print ("Must enter digits greater than 0 !")
    print(e)
 
 
try:

    a_prefix = str(input("Enter a three letter prefix:  "))

# Check for non-text
except ValueError as f:

    print ("Must enter letters !")
    print(f)

if ((a_prefix.isnumeric()) or (str(a_num)[0]=='-' and len(str(a_num))>1)):
# bail out as not text, or had negative sign with '-' 
    print ("Prefix Input is either not text, or Number input is negative.") 
    exit()

else:
# initialise counter
    inc_num = 1

    for i in range(a_num+1):
        while(inc_num <= a_num):
            print("{:.3}{:d}".format(a_prefix, inc_num))
            inc_num += 1

    print("Finished\n")
 
