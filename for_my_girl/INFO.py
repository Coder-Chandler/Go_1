#-*- coding: utf-8 -*- 2
import datetime
class Person(object):
    def __init__(self,name):
        '''create a person called name'''
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[0]

    def getName(self):
        return self.name

    def getLastName(self):
        '''return self's first name'''
        return self.lastName

    def setBirthday(self, year, month, day):
        '''sets self's birthday to birthdayDate'''
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        '''sets self's birthday to birthDate'''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days/365

    def __lt__(self,other):
        '''Sorted by last name, if the same name then random sort'''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

    __repr__ = __str__

def add():
    stu ={}
    a = raw_input('输入要添加的学生姓名 ： ')
    newstudent = Person(str(a))
    year,month,day = raw_input('输入被添加学生的出生日期 ： ').split()
    newstudent.setBirthday(int(year), int(month), int(day))
    stu[newstudent.getName()] = newstudent.getAge()
    return stu
x=add()
print x