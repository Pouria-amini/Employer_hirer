"""
        [===============================================================================================]
        [                                                                                               ]
        [                         Module 1 assignment                                                   ]
        [                         Author: Mahdi Amini                                                   ]
        [                         P.Con: Using class in Python                                          ]
        [                         Date Started: 10-04-2020                                              ]
        [                         Date Finished: 17-04-2020                                             ]
        [                         ICS3UI-02 for Ms. Harris                                              ]
        [                                                                                               ]
        [-----------------------------------------------------------------------------------------------]
        [                                 Program Description                                           ]
        [                                                                                               ]
        [   This program checks if the a person with his major can be hired or not. The number of vacan-]
        [cies are also considered. If the person's major is needed, persons information adds to a text  ]
        [file named [employees_information]. The order of adding is that the information adds under the ]
        [title of the job. For instance, when a person applies for Marketing Specialist, his or her inf-]
        [ormation adds under the Marketing Specialist title. The text file is human readable. The other ]
        [text file called [vacancies] has all the vacancies in a particular job. If there is no vacanci-]
        [es, information would not be added to the [employees_information] text file. The inputs should ]
        [be exactly the same as the dictionary keys in the top of the program.(lower and upper cases are]
        [also considered.) If you wish to change the data, make sure to change them on both dictionary  ]
        [and vacancy text files.                                                                        ]
        [                                                                                               ]
        [===============================================================================================]

"""
import random

available_jobs = {'Marketing Specialist': 3, 'Marketing Manager': 7, 'Marketing Director': 2,
                  'Marketing Research Analyst': 8,
                  'Marketing Communications Manager': 15}

available_rooms_for_employees = [room for room in range(0, 100)]


class Employee:
    def __init__(self, name, last_name, age, major):
        self.name = name + '-' + last_name
        self.age = age
        self.major = major
        self.check_vacancy()

    def check_vacancy(self):
        for job in available_jobs.keys():
            if self.major == job and available_jobs[job] != 0:
                with open("vacancies.txt", 'r') as v:
                    vacant = v.readlines()
                for c in vacant:
                    if c == job + '\n':
                        q = vacant.pop(vacant.index(c)+1)
                        vacant.insert(vacant.index(c) + 1, str(int(q) - 1) + '\n')
                with open("vacancies.txt", 'w') as v:
                    for i in vacant:
                        v.write(str(i))
                available_jobs[job] = int(q) - 1
                Employed(self.name, self.major)

class Employed:
    def __init__(self, name, major):
        self.email = name + '@' + major + '.ca'
        self.room = random.choice(available_rooms_for_employees)
        available_rooms_for_employees.pop(self.room)
        self.Add_employee_to_employees(name, major)

    def Add_employee_to_employees(self, name, major):

        # Check if the file is empty or not:
        with open("employees_information.txt", 'r') as f:
            Data = f.readlines()
        if not Data:
            with open("employees_information.txt", 'w') as f:
                f.write(major + '\n')
        with open("employees_information.txt", 'r') as f:
            Data = f.readlines()

        Check = False
        if major + '\n' not in Data and Check is False:
            with open("employees_information.txt", 'a+') as f:
                f.write(major + '\n')
            Check = True
        # Read the whole file :
        with open("employees_information.txt", 'r') as f:
            Data = f.readlines()
        # Check if the employee is not in the file :
        repeated_employee = False
        for i in Data:
            if '|name: ' + name + '\n' == i:
                repeated_employee = True

        for i in Data:
            for j in available_jobs.keys():
                if i == j + '\n' and j == major and Data and not repeated_employee:
                    Data.insert(Data.index(i) + 1, '|name: ' + name + '\n')
                    Data.insert(Data.index(i) + 2, '|email: ' + self.email + '\n')
                    Data.insert(Data.index(i) + 3, '|room No: ' + str(self.room) + '\n')
        with open("employees_information.txt", 'w') as f:
            for i in Data:
                f.write(i)

print("welcome to employee hirer")
name = input("Give the person's name >> ")
last_name = input("Give the person's last name >> ")
age = input("Give the person's age >> ")
major = input("Give the person's major: (The inputs should be exactly the same as the dictionary keys \n"
              "in the top of the program.(lower and upper cases are also considered.)) >> ")
employee = Employee(name, last_name, age, major)
