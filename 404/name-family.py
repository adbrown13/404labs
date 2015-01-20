#Written by Ashley Fegan
class Student:
    courseMarks={}
    name= ""
    def __init__(self, name, family):
        """
        testing:
        >>> hi=Student("blah","blah")
        >>> print hi.name
        blah
        """
        self.name=name
        self.family=family
   
    def addCourseMark(self, course, mark):
        """
        testing:
        >>> hi=Student("blah","blah")
        >>> hi.addCourseMark("meh",90)
        >>> print hi.courseMarks["meh"]
        90
        """
        self.courseMarks[course] = mark
    def average(self):
        """
        testing:
        >>> hi=Student("blah","blah")
        >>> hi.addCourseMark("meh",90)
        >>> hi.addCourseMark("blahs",20)
        >>> print hi.average()
        55
        """
        total=0
        count=0
        average=0
        for x in self.courseMarks.keys():
            count=count+1
            total=total+self.courseMarks[x]
        average=total/count
        return average

if __name__ == '__main__':
    import doctest
    doctest.testmod()
