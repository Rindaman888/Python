
#สร้าง constructor
class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
        #print("กำหนดคุณสมบัติ")
        
    def showdata(self):
        print("ขื่อ = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))

#สร้างวัตถุ
obj1 = Employee("Cat",1000,"Com")
obj2 = Employee("Dog",2000,"Sci")
obj3 = Employee("Cow",3000,"Art")
