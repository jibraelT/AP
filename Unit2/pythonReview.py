
# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.

classwork = True
homework = True

if classwork is True and homework:
    #print("there assighnments are turned in")

# hint: find the a operator that allows you to evaluate 2 condtions.

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

 def the_function(x):
    return x[::-1]
thetxt= the_function("this might look a little weird")
#print(thetxt)


# hint: look into string reverse in w3schools


#Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.

def guesscheck():
    print("ple ase enter a number")
    number = input()
    values= []
    while number != 'q':
        values.append(int(number))
        print(values)
        print("please enter a number")
        number = input()
    else:
        print('doing calculation...')
        total = sum(values)
        print(total)



    