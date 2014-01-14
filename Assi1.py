class Student:

	courseMarks={}
	name=''
	family=''

	def __init__(self, name, family):
		self.name = name
		self.family = family

	def addCourseWork(self,course,mark):
		self.courseMarks[course] = mark

	def average(self):
		Total_mark = sum(self.courseMarks.values()) / len(self.courseMarks)
		return Total_mark


mystudent=Student("Test1","Test2")
mystudent.addCourseWork('Math',100)
mystudent.addCourseWork('AS',30)
mystudent.addCourseWork('BIO',40)
mystudent.addCourseWork('PALEO',60)
mystudent.addCourseWork('ASTRO',70)

print 'Student Name  : %s    Student Family Name : %s ' % (mystudent.name,mystudent.family)
print 'Student Course Marks :'
for key,value in mystudent.courseMarks.iteritems():
	c =' Course Name : %s     Course Mark : %s ' % (key,value)
	print c

print 'Student Average Mark:'
print  mystudent.average()
