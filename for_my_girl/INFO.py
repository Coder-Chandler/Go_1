#-*- coding: utf-8 -*- 2
import datetime
class Person(object):
    def __init__(self, name, gender):
        '''create a person called name'''
        self.name = name
        self.gender = gender
        self.birthday = None
        self.lastName = name.split(' ')[0]

    def __str__(self):
        return self.name

    def getName(self):
        return str(self.name)

    def getGender(self):
        return self.gender

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

    __repr__ = __str__

class Student(Person):
    nextNum = 1

    def __init__(self, name, gender):
        Person.__init__(self,name,gender)
        self.course = None
        self.parent = None
        self.address = None
        self.school = None
        self.idnum = Student.nextNum
        Student.nextNum += 1

    def __str__(self):
        return self.name

    def getIdNum(self):
        return self.idnum

    def setCourse(self,course):
        if self.course == None:
            self.course = course

    def getCourse(self):
        return self.course

    def setParent(self,parent):
        if self.parent == None:
            self.parent = parent

    def getParent(self):
        return self.parent

    def setAddress(self,address):
        if self.address == None:
            self.address = address

    def getAddress(self):
        return self.address

    def setSchool(self,school):
        if self.school == None:
            self.school = school

    def getSchool(self):
        return self.school

    __repr__ = __str__


class Parent(Person):
    def __init__(self, name, gender):
        Person.__init__(self, name, gender)
        self.phone = None

    def setPhone(self,phone):
        if self.phone == None:
            self.phone = phone

    def getPhone(self):
        return self.phone

stu ={}

def add():
    name = raw_input('输入要添加的学生姓名 ： ')
    gender = raw_input('输入要添加的学生性别 ： ')
    newstudent = Student(name, gender)
    year,month,day = raw_input('输入被添加学生的出生日期 ： ').split()
    assert len((year, month, day)) == 3, '出生日期输入格式有误！(示例：2001,01,01)'
    newstudent.setBirthday(int(year), int(month), int(day))
    course = raw_input('输入要添加的学生专业 ： ')
    newstudent.setCourse(course)
    parent = raw_input('输入要添加的学生监护人姓名 ： ')
    newstudent.setParent(parent)
    address = raw_input('输入要添加的学生住址 ： ')
    newstudent.setAddress(address)
    school = raw_input('输入要添加的学生所在学校 ： ')
    newstudent.setSchool(school)
    stu[newstudent.getName()] = newstudent.getGender(),newstudent.getAge(),\
                                newstudent.getCourse(),newstudent.getParent(),\
                                newstudent.getAddress(),newstudent.getSchool()
    return stu
'''
print add()
for k,v in stu.items():
    print '%s ： %s '%(k,v)
'''

def Input():
    raw_input('您要添加(a)、修改(r)、查看(d)学生信息？ ： ')
    


