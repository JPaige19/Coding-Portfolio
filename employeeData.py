"""Write a class named Employee that holds the following data about an employee in attributes:
Name
ID Number
Department
Job title

Once you have written the class, write a program that creates three Employee objects to hold the following data:
Name: Susan Meyers
ID Number: 47899
Department: Accounting
Job Title: Vice President

Name: Mark Jones
ID Number: 39119
Department: IT
Job Title: Programmer

Name: Joy Rogers
ID NUmber: 81774
Department: Manufacturing
Job Title: Engineer

The program should store this data in three Employee objects and then print the data for each employee as shown exactly in the following sample run.
Note: Pay close attention to the placement of spaces, colons and blank lines in the sample run. Your output must match this.

Sample Run:
Name: Susan Meyers
ID Number: 47899
Department: Accounting
Job Title:·Vice President

Name: Mark Jones
ID Number: 39119
Department: IT
Job Title: Programmer

Name: Joy Rogers
ID Number: 81774
Department: Manufacturing
Job Title: Engineer

"""



class Employee:
    def __init__(self):
        self.name = ''
        self.idNumber = ''
        self.department = ''
        self.jobTitle = ''
    
    def set_name(self, name):
        self.name = name
    
    def set_idNumber(self, id):
        self.idNumber = id
    
    def set_department(self, dept):
        self.department = dept
    
    def set_jobTitle(self, title):
        self.jobTitle = title
    
    def get_name(self):
        return self.name

    def get_idNumber(self):
        return self.idNumber
    
    def get_department(self):
        return self.department
    
    def get_jobTitle(self):
        return self.jobTitle

susanMeyers = Employee()
susanMeyers.set_name('Susan Meyers')
susanMeyers.set_idNumber('47899')
susanMeyers.set_department('Accounting')
susanMeyers.set_jobTitle('Vice President')

markJones = Employee()
markJones.set_name('Mark Jones')
markJones.set_idNumber('39119')
markJones.set_department('IT')
markJones.set_jobTitle('Programmer')

joyRogers = Employee()
joyRogers.set_name('Joy Rogers')
joyRogers.set_idNumber('81774')
joyRogers.set_department('Manufacturing')
joyRogers.set_jobTitle('Engineer')

emp = [susanMeyers, markJones, joyRogers]

for employee in emp:
    print(f'Name: {employee.get_name()}')
    print(f'ID Number: {employee.get_idNumber()}')
    print(f'Department: {employee.get_department()}')
    print(f'Job Title: {employee.get_jobTitle()}')
    print()