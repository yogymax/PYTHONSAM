
print('hiii')
print('hello')

class Marks:
    def __init__(self,web,python,java,cloud='NA',env='NA'):
        self.websubmarks = web
        self.pythonsubmarks = python
        self.javasubmarks = java
        self.cloudsubmarks = cloud
        self.envsubmarks = env

    def __repr__(self):
        return str(self)

    def str(self):
        return f'''
            Web :  {self.websubmarks}
            Java :  {self.javasubmarks}
            Python :  {self.pythonsubmarks}
            Cloud :  {self.cloudsubmarks}
            Env :  {self.envsubmarks}
        '''


class Address:
    def __init__(self,adid,city,state,pin):
        self.adrid = adid
        self.city = city
        self.state = state
        self.pincode=pin

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
            Address Id : {self.adrid}
            Address City : {self.city}
            Address State : {self.state}
            Address Pincode : {self.pincode}
        '''

class Person:
    def __init__(self,pid,pnm,pag,padr,pacc):
        self.personId = pid
        self.personName=pnm
        self.personAge = pag
        self.personAddress = padr
        self.personAccount =pacc

    def __str__(self):
        return '''
            Id :  {}
            Name :  {}
            Age :  {}
            Address :  {}
            Account :  {}
        '''

class College:
    def __init__(self,regid,colnm,adr,dept,account):
        self.collgeId = regid
        self.collegeName = colnm
        self.collegeAdr = adr
        self.collegeDepts = dept
        self.collegeAccount = account


    def __str__(self):
        return f'''
College Id : {self.collgeId} 
College Name : {self.collegeName} 
College Dept : {self.collegeDepts}
College Adr : {self.collegeAdr}
College Account : {self.collegeAccount}
        '''

class Account:
    def __init__(self,accId,acctype,balance):
        self.accId = accId
        self.accBalance = balance
        self.accType = acctype

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
                    Account No : {self.accId}
                    Account Type : {self.accType}
                    Account Balance : {self.accBalance}
        '''

class Student(Person):
    def __init__(self,sid,snm,sag,sfees,account,adr,subjs):
        super().__init__(sid,snm,sag,adr,account)
        self.studFees = sfees
        self.studSubjs = subjs

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
                Stud Id : {self.personId}
                Stud Name: {self.personName}
                Stud Age : {self.personAge}
                Stud Fees : {self.studFees}
                Stud Account : {self.personAccount}
                Stud Subjects : {self.studSubjs}
                Stud Address  : {self.personAddress}
        '''

class Dept:
    def __init__(self,did,dcode,dnam,prof,studs):
        self.deptId = did
        self.deptCode = dcode
        self.deptName = dnam
        self.deptProfs = prof
        self.deptstudents = studs


    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
            Dept Id : {self.deptId},
            Dept Code : {self.deptCode}
            Dept Name : {self.deptName}
            Dept Prof : {self.deptProfs}
            Dept Students : {self.deptstudents}
        '''

class Professor(Person):
    def __init__(self,pid,pfnm,pag,pexp,psal,account,adr,subjs):
        super().__init__(pid,pfnm,pag,adr,account)
        self.profExp = pexp
        self.profSal = psal
        self.profSubjs = subjs

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
                Prof Id : {self.personId}
                Prof Name : {self.personName}
                Prof Exp : {self.profExp},
                Prof Sal : {self.profSal}
                Prof Age : {self.personAge}
                Prof Subj : {self.profSubjs}
                Prof Account : {self.personAccount}
                \t\tProf Address : {self.personAddress} 
                    
        '''

class Subject:
    def __init__(self,sid,snm,scod):
        self.subjid = sid
        self.subjName = snm
        self.subjCode = scod

    def __hash__(self):
        return self.subjid

    def __eq__(self, other):
        return self.subjid == other.subjid

    def __str__(self):
        return f'''
                    Subject ID : {self.subjid} -
                    Subject Code  : {self.subjCode}-
                    Subject Name  : {self.subjName}
        '''

    def __repr__(self):
        return str(self)


if __name__ == '__main__':

    ad = Address(adid=101,city='Pune',state='MH',pin=121212)
    #print(ad)
    #subj  = Subject(sid=1122,snm='Python',scod='PY')
    #print(subj)

    prof1 = Professor(pid=12831,pfnm='XXXX1',pag=29,pexp=4,psal=12893.44,account=Account(accId=121221,acctype='Saving',balance=2872.34),adr=ad,subjs=["Web","Cloud"])
    prof2 = Professor(pid=12281, pfnm='XXXX2', pag=33, pexp=7, psal=45893.44, account=Account(accId=111221,acctype='Saving',balance=1872.34), adr=ad, subjs=["Web","Java"])
    prof3 = Professor(pid=15281, pfnm='XXXX3', pag=44, pexp=10, psal=23432.44, account=Account(accId=221221,acctype='Saving',balance=3872.34), adr=ad, subjs=["Web","Python"])
    prof4 = Professor(pid=16281, pfnm='XXXX4', pag=54, pexp=14, psal=29454.44, account=Account(accId=39221,acctype='Saving',balance=4572.34), adr=ad, subjs=["ENV","Python"])
    prof5 = Professor(pid=12871, pfnm='XXXX5', pag=30, pexp=7, psal=39404.44, account=Account(accId=234221,acctype='Saving',balance=21872.34), adr=ad, subjs=["Java","ENV"])

    sb11 = Subject(sid=1122, snm='Python', scod='PY')
    sb12 = Subject(sid=2312, snm='Web', scod='WEB')
    sb13 = Subject(sid=3412, snm='Java', scod='JD')
    sb14 = Subject(sid=2344, snm='ENV', scod='EN')
    sb15 = Subject(sid=3124, snm='Cloud', scod='CD')

    stud1 = Student(sid=1286,snm='AAAA',sag=20,sfees=12389.23,
                   account=Account(accId=111221,acctype='Saving',
                                   balance=2872.34),
                    adr=Address(adid=101,city='Pune1',state='MH',pin=121212),
                   subjs=[sb11,sb12,sb13,sb14])
    stud1.studMarksheet = Marks(web=77,python=89,java=87,env=67)

    stud2 = Student(sid=128612, snm='AAAA', sag=20, sfees=12389.23,
                   account=Account(accId=222221, acctype='Saving',
                                   balance=1872.34),
                    adr=Address(adid=102, city='Pune2', state='MH', pin=121212),
                   subjs=[sb11,sb12,sb13,sb14])
    stud2.studMarksheet = Marks(web=17, python=24, java=0, env=100)

    stud3 = Student(sid=12861, snm='XYZ', sag=15, sfees=40000.23,
                   account=Account(accId=333221, acctype='Saving',
                                   balance=472.34),
                    adr=Address(adid=103, city='Pune3', state='MH', pin=121212),
                   subjs=[sb11,sb12,sb13,sb15])
    stud3.studMarksheet = Marks(web=78, python=49, java=88, cloud=20)

    stud4 = Student(sid=12856, snm='PQR', sag=21, sfees=40000.23,
                   account=Account(accId=444221, acctype='Saving',
                                   balance=5572.34),
                    adr=Address(adid=104, city='Pune4', state='MH', pin=121212),
                   subjs=[sb11,sb12,sb13,sb14])
    stud4.studMarksheet = Marks(web=99, python=95, java=19, env=90)

    stud5 = Student(sid=12386, snm='AAAABB', sag=18, sfees=40000.23,
                   account=Account(accId=555221, acctype='Saving',
                                   balance=55872.34),
                    adr=Address(adid=105, city='Pune5', state='MH', pin=121212),
                   subjs=[sb11,sb12,sb13,sb15])
    stud5.studMarksheet = Marks(web=36, python=54, java=56, cloud=80)

    stud6 = Student(sid=21286, snm='YYY', sag=25, sfees=40000.23,
                   account=Account(accId=666221, acctype='Saving',
                                   balance=25672.34),
                    adr=Address(adid=106, city='Pune6', state='MH', pin=121212),
                   subjs=[sb11,sb12,sb13,sb14])
    stud6.studMarksheet = Marks(web=67, python=77, java=87, env=75)


    #print(prof1)
    itdept = Dept(did=12122,dcode='IT',dnam='Information Tech',
                prof=[prof1,prof2],studs=[stud1,stud2])

    csedept = Dept(did=12313, dcode='CSE', dnam='Computer',
                  prof=[prof3,prof1], studs=[stud3,stud4])

    mechdept = Dept(did=44422, dcode='MECH', dnam='Mechanical',
                  prof=[prof5,prof4], studs=[stud5,stud6])


    college = College(regid='XX12132',colnm='PICT',
                      adr=Address(adid=34423,city='Pune',state='MH',pin=331212),
            dept=[itdept,csedept,mechdept],
            account=Account(accId=223333,acctype='Current',balance=21872.34))

    print(college)

import sys
sys.exit(0)

v1 = 10
v2 = 10

setNumbers = {v1,v2} # 1 -- which one -- v1

s1 = Subject(101,"Python","py")
s2 = Subject(101,"Python","py")

print(isinstance(s1,Subject))
print(isinstance(s1,Student))

print('---------------------------------')

print(isinstance(s1,Subject))
print(isinstance(s2,Subject))


print('SetOfNumbers -- ',len(setNumbers),setNumbers)
#print('SetofSubjects -',len(setValues),setValues)




import sys
sys.exit(0)

print(s1 is s2) # is --ref check -- #61993264 61993296 -- False
print(id(s1) == id(s2)) #same -- ref check -- False
#within an execution of an application address same -- but next execution will chnage the mem adr

print(s1 is s2,s2 is s3,s3 is s1)
print(id(s1),id(s2),id(s3))

print(type(s1) == type(s2))


s3 = s1
print(s1.subjid,s3.subjid)

s3.subjid = 123

#setValues = {s1,s2} # 2 --?
print(s1.subjid,s3.subjid)
print('Content Equality -- ',s1 == s3) #eq -- equality
    #e1 -- content equality --
            #depends -- eq - overriden -- subject eq -- dev -- which property?
                        #  !overriden -- object eq ---- is -ref equality




'''
id/is --ref check 
==-- 
		overidden -- content check  -- eq written inside same class
		!overidden -- ref check -- object thru -- not written -- ref parent-- object-- eq -- is
type  -- own --true
isinstance -- own and all parents -- same hierarchy..







-- Domain Entities --
		
		SDLC -- 
		
	Client			Company
	X----------->	Scoopen
					Payroll
	Idea ---------------> scoopen
	ProductOwnerClient		BA
							Solution Arch
							Devs/Testers-- Team
							
					req---------->		
	ProductOwer		Spoc    BA/SolutionArch
	Testers--				Testers
			To make quality Apps
			
	
				
				Req Gathering And Analysis
						Raw Text--docs
						Meetings
						Emails
						Refs Sites
						Verbal -NonVerbal -----
									BA[NoNTech]/SolutionArch[Tech]--
											Managerial --Manager --SrManager -- Program Manager -- Sr Prog Manager -- Director -- SBU Head -- CEO/Founders
		Jun Eng -- Soft Eng-- SSE -- Lead -- 
		
											Technical -- Tech Spclist -- Sr.Tech Splct -- Solutio Arch --
																							10-12+
				Reqs -- clinet -- knowlegde -- 
							which best tech -- to implement college System.
							
				Gather
				Process
				Finalize
				
				
				
				Design
					HLD -- Soft  -- 
							List of softwares -- 
							Aggrements -- SLA
							TEam
							Duration
							
					LLD	
						-- Table -- and class--properties--
				
					HLD + LLD --------> SRS [Software Req Specification Doc]
				
				Coding	---
					TDD - Test Driven Development
					BDD  -- Bahivour Driven development.
					
						
	def add(num1,num):
		paas
		
		
	
	result = add(10,20)
	test result -- 30--- None -- Fail ---Refactor code -- add business logic
		as per SRS ---- Test case as per SRS
		
		Dev -- SRS
		Test -- SRS
			Test--- Dev
					Test -- pass -- dev pass -- req pass.
					
	
						
				
				Testing
				Deployment
				Support/Maintainance.
		
Domain --


type -- check datatype - which class instance
is -- check ref equality - address comparison
id -- check ref equality -- address comparison
== -- eq == first inside caller class --if present -
			
					present -- content equality --
					absent -- MRO -- object-- is -- ref comparison
isinstance --
				check the which class instance..
			
		==
		is/id
		
						A -- Z
		type			
					x = X()
					l = L()
					
					type(l) == A - parent -- False
					type(l) == L -- same   -- True
					type(l) == X -- child
					
					type(x) == L -- parent --False
					type(x) == X -- same -- True
					type(x) == Z -- child -- False
					
					
					
		isinstance

					x = X()
					l = L()
					
					isinstance(l,A) -- parent -- True
					isinstance(l,L) -- same -- True
					isinstance(l,X) -- child --False
					
					isinstance(x,L) -- parent -- True
					isinstance(x,X) -- same -- True
					isinstance(x,Z) -- child --False
					
					anytype -- type(anytype)==object  -- False 
					anytype -- isinstance(anytype,object) -- True
					
					
				  A
					
			B			C
								D
				  Z			
									X
							
									Y		
							
							
							
					
					
		
 == 
 
		overriden -- content equality
		!overriden -- ref equality	
 is/id -- ref equality
  in built types --
			content equality -- eq overidden
			generics -- 
				number
				string
				bool
				
		

College
Student
Dept
Subjects
Faculty
Library
Account

find out total expenses for the college
    totalExpes = 0.0
    for dept in college.collegedepts:
        for prof in dept.professors:
            totalexpe += prof.salary
    print(totalexps)

find out student agr marks
    for dept  in college.collegedepts
        collegesum=0.0
        for st in dept.students:
            stagr = 0.0
            totalmarks=0.0
            for key,val in st.marks.__dict__.items():
                    if val=='NA':
                        continue
                    totalmarks += val
            totalmarks/4 -- agrs -- student
            collegesum +=totalmarks

'''