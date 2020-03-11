
print('one more change by d1')
# hsbc -->  infosys[dev]
#client ---> company[BA/Solution arch-- team]
#[product owner--spoc]---> company --

#------------------------------>dev start
import sys

class Student:
    def __init__(self,sid,snm):
        self.studId=sid
        self.studName=snm

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)


    def __hash__(self):
        return self.studName.__hash__() + self.studId
        #return self.studName.__hash__()
    def __eq__(self, other):
        return self.studName == other.studName and self.studId == other.studId
        #return self.studName == other.studName



s1 = Student(101,"AAAA")
s2 = Student(101,"AAAA")
#starting pasn ---> end

s3 = Student(102,"XXXX")
s4 = Student(103,"AAAA")
s5 = Student(102,"BBBB")

#s1--s2--s4 --->
#[s1-s2-s4] -- s3 -- s5
#s1 -- v7       s3-v5  s5 --v2
# [s1-s2]  [s3-s5] [s4]
# s1 - v7   s5-v5   s4-v6
setofDict = {
        s1 : "v1",  #s1--> v7
        s2 : "v2",
        s5 : "v9", #s5--> v2
        s4 : "v3",
        s1 : "v4",
        s3 : "v5", #s3--> v5
        s4 : "v6",
        s5 : "v2",
        s4 : "v3",
        s1 : "v4",
        s2 : "v7",
}
print(setofDict)

import sys
sys.exit(0)
#s2 ---> v4
# s3 -- v6
# s4 -- v5
# s5 -- v7

#dict-- s3,s4,s5 -- s1/s2 -- > s2

#pairs ?



sys.exit(0)
setOfStudents = {s2,s5,s3,s1,s4,s3,s5,s1}
print(setOfStudents)

sys.exit(0)
s3 = Student(101,"BBBB")
s4 = Student(102,"AAAA")
s5 = Student(103,"CCCC")

# dev-- 5
# allcontent  --- 4 - 1,3,4,5
#id -- 3 -- 1,4,5
#name -- 3 -- 1,3,5

