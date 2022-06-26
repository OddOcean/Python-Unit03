############################################################################
#     Aidan Weygandt                        2.16.2021                      #
#     Unit 3 Problems                                                      #
#.    ASCII Characters, payroll application, random uppercase letter,      #
#     String Methods, Turtle Olympic Rings                                 #
############################################################################
import time
import random
import turtle

print ("Problem #1 - ASCII Characters")
upcsltr = int(input("Enter a number between 65-90: "))
print ("Your ASCII code is the upercase letter:",chr(upcsltr)) #converts ASCII code into a letter
print ("Your codes lowercase equivalent is:", chr(upcsltr+32)) #converts ASCII code into lowercase equivalent by adding 32 (number of codes between the lower and uppercase letters)

lwcsltr = int(input("\nEnter a number between 97-122: "))
print ("Your ASCII code is the lowercase letter:",chr(lwcsltr)) #converts ASCII code into a letter
print ("Your codes uppercase equivalent is:", chr(lwcsltr-32)) #converts ASCII code into uppercase equivalent by removing 32


print ("\n\nProblem #2 - Payroll Application")
ename = input("Enter employee's name: ")
hrsworked = float(input("Enter number of hours worked in a week: "))
pay = float(input("Enter your hourly pay rate: "))
ftax = float(input("Enter federal tax withholding rate(i.e. 0.05): "))
stax =  float(input("Enter your state tax withholding rate(i.e. 0.05): "))

print ("\nEmployee name:", ename)
print ("Pay rate:", pay)
print ("Gross pay:","$", end=str((hrsworked*pay))) #hours worked times pay rate
print ("\nDeductions:")
print ("  Federal withholding: ","$",end=str(round((hrsworked*pay*ftax),2))) #ftax % of gross pay
print ("\n  State withholding: ","$",end=str(round((hrsworked*pay*stax),2))) #stax % of gross pay
print ("\n  Total Deductions: ","$",end=str(round((hrsworked*pay*stax)+(hrsworked*pay*ftax),2))) #ftax and stax total
print ("\nNet Pay:","$",end=str(round((hrsworked*pay)-((hrsworked*pay*stax)+(hrsworked*pay*ftax)),2))) #gross pay minus total deductions


print ("\n\n\nProblem #3 - Output a random uppercase letter using time.time()")
currenttime = round(time.time()%10)
print ("Random Letter:", end=" ")
print (chr(currenttime+random.randint(65, 80))) #adds current seconds to a random number for an ASCII code between 65-90


print ("\n\nProblem #4 - Convert a word with String Methods")
txt1 = "princiPle"
print ("The word", txt1, "after three string method calls is", end=" ")
print (txt1.replace("le", "al").capitalize()) #formats and changes word