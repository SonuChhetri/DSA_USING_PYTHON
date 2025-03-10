class studentMarks:
    def __init__(self, name, roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def showdata(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        # print("Marks:",self.marks)
    def showmarks(self):
        print("Marks:",self.marks)

obj1 = studentMarks("SONU","11",90)
obj1.showdata()  
obj1.showmarks()  
