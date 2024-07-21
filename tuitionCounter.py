"""At one college, the tuition for a full-time student is $8,000 per semester. 
It has been announced that the tuition will increase by 3 percent each year for the next 5 years. 

Write a program with a loop that displays the projected semester tuition amount for the next 5 years.
Your program’s output must exactly match the output shown in the sample run below. Notice the wording of the messages and the placement of spaces and punctuation. Also, make sure that the tuition amounts are rounded to two decimal places.
Sample Run
In 1 year, the tuition will be $8240.0. 
In 2 years, the tuition will be $8487.2. 
In 3 years, the tuition will be $8741.816. 
In 4 years, the tuition will be $9004.07048. 
In 5 years, the tuition will be $9274.192594400001. """


tuition = 8240.00
tuition1 = 8000
rate = 0.03

for year1 in range(1, 2):
    tuition1 = tuition1 * (1 + rate)
    print(f"In {year1} year, the tuition will be ${tuition1}.")
    for year in range (2, 6):
        tuition *= (1 + rate)
        print(f"In {year} years, the tuition will be ${tuition}.")