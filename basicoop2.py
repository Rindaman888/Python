
#สร้าง constructor
def __init__(self):
    print("Test")

def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
class Employee:
        #print("กำหนดคุณสมบัติ")
    def showdata(self):
        print("ขื่อ = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))


#สร้างวัตถุ
obj1 = Employee()
obj1.detail("Cat",1000,"ครู")

obj2 = Employee()
obj2.detail("Dog",5000,"ตำรวจ")

obj3 = Employee()
obj3.detail("Cow",3000,"ทหาร")
