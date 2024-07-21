"""A cookie recipe calls for the following ingredients:
1.5 cups of sugar
1 cup of butter
2.75 cups of flour

The recipe produces 48 cookies with this amount of ingredients. 
Write a program that asks the user how many cookies they want to make 
and then displays the number of cups of each ingredient needed for the specified number of cookies.

When the program asks the user for the number of cookies, it should display the following string as a prompt:
'Enter number of cookies:'

When the program displays the number of cups of ingredients, it should display a message in the following format:
You need x cups of sugar, y cups of butter, and z cups of flour.

Where x is the number of cups of sugar, y is the number of cups of butter, and z is the number of cups of flour. 
Don’t worry about rounding the numbers in the output.
The following sample run shows an example of the program's output, with the user's input shown in bold. (Notice the wording of the messages and the placement of spaces, colons, and punctuation. Your program's output must match this.)

Sample Run
Enter number of cookies: 48
You need 1.5 cups of sugar, 1.0 cups of butter, and 2.75 cups of flour. """


num_cookies = int(input('Enter number of cookies:'))
cups_sugar = 1.5 * num_cookies / 48
cups_butter = num_cookies / 48
cups_flour = 2.75 * num_cookies / 48

print(f'You need {cups_sugar} cups of sugar, {cups_butter} cups of butter, and {cups_flour} cups of flour.')