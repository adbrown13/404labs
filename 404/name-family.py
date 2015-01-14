class Student:
	courseMarks={}
	name= ""
	def __init__(self, name, family):
		self.name=name
		self.family=family
	def addCourseMark(self, course, mark):
		self.courseMarks[course] = mark
	def average(self):
		total=0
		count=0
		average=0
		for x in self.courseMarks.keys():
			count=count+1
			total=total+self.courseMarks[x]
		average=total/count
		return average


