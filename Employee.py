import person
p=person.person
class employee(p):
    def setWorkShift(self,shift):
        self.workShift=shift
    def setSalary(self,salary):
        self.salary=salary
    def setWorkHours(self,workHours):
        self.workHours=workHours
    def incrementLeave(self):
        self.leave += 1
    #temporary/permanent
    def setType(self,type):
        self.type=type
    def setJobTitle(self,title):
        self.jobTitle=title


