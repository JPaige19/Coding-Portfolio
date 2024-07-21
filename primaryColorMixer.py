"""The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors. 
When you mix two primary colors, you get a secondary color:
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.

Write a program that prompts the user to enter the names of two primary colors, one at a time. 

If the user enters anything other than "red," "blue," or "yellow," the program should print "You didn't input two primary colors." 

Otherwise, it should print a message in the following format: "When you mix red and blue, you get purple." (Assuming the user entered "red" and "blue”.)

Look carefully at the following sample runs of the program. 

In particular, notice the wording of the messages and the placement of spaces, colons, and punctuation. Your program's output must match this.

Sample Run (User input shown in bold)
Enter primary color:red
Enter primary color:blue
When you mix red and blue, you get purple

Sample Run (User input shown in bold)
Enter primary color:teal
Enter primary color:orange
You didn't input two primary colors."""


prim1 = input('Enter primary color:')
prim2 = input('Enter primary color:')

prim1 = prim1.lower() 
prim2 = prim2.lower()
color = 'no color'

if prim1 == 'yellow' and prim2 == 'blue' or prim1 == 'blue' and prim2 == 'yellow':
    color = 'green'
elif prim1 == 'red' and prim2 == 'yellow' or prim1 == 'yellow' and prim2 == 'red':
    color = 'orange'
elif prim1 == 'red' and prim2 == 'blue' or prim1 == 'blue' and prim2 == 'red':
    color = 'purple'

if color == 'no color':
    print("You didn't input two primary colors.")
else:
    print(f'When you mix {prim1} and {prim2}, you get {color}.')