""" Several litters of new pups were recently born in the otter habitat at the local zoo. 
Write a program that calculates the percentage of male and female otters currently in the habitat.

The program should ask the user for the number of males and the number of females using two separate input statements. 

When the program asks for the number of males, it should display the following string as a prompt:
'Enter number of males:'

When the program asks for the number of females, it should display the following string as a prompt:
'Enter number of females:'

The program should display the percentage of males and females (round to the nearest whole number) in the following format:
Percent males: 35%
Percent females: 65%

The following sample run shows an example of the program's output, with the user's input shown in bold. 
(Notice the wording of the messages and the placement of spaces, colons, and punctuation. 
Your program's output must match this.)

Sample Run
Enter number of males:75
Enter number of females:25
Percent males: 75%
Percent females: 25% """


num_males = int(input('Enter number of males:'))
num_females = int(input('Enter number of females:'))

total_otters = num_males + num_females

male_percent = (num_males / total_otters) * 100
female_percent = (num_females / total_otters) * 100

print(f'Percent males: {male_percent:.0f}%')
print(f'Percent females: {female_percent:.0f}%')