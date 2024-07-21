""" The date June 10, 1960, is special because when it is written numerically, the month multiplied by the day equals the year:
6/10/60 --> 6*10 = 60

Write a program that asks the user to enter a month (in numeric form), a day, and a two-digit year in three separate input statements. 

The program should determine whether the month times the day equals the year. 

If so, it should print, "This date is magic!" Otherwise, it should print, "This date is not magic."

Look carefully at the following sample runs of the program. 
In particular, notice the wording of the messages and the placement of spaces, colons, periods, and exclamation marks. Your program's output must match this.

Sample Run (user input shown in bold)
Enter month (numeric):12
Enter day:8
Enter two digit year:96
This date is magic!

Sample Run (user input shown in bold)
Enter month (numeric):10
Enter day:2
Enter two digit year:75
This date is not magic. """



month = int(input('Enter month (numeric):'))
day = int(input('Enter day:'))
year = int(input('Enter two digit year:'))

day_times_month = day * month

if day_times_month == year:
    print('This date is magic!')
else:
    print('This date is not magic.')

