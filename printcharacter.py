# Write a program to print first 5 character of your name using for loop.


class firstFiveCHAR:
    def __init__(self,name):
        # self.size=size
        self.name=name
        
    def character(self,size):
        self.size=size
        for i in range (size):
            print(self.name[i],end='-')
            
            
text=input("Enter your name: ")

obj=firstFiveCHAR(text)

s=int(input("Enter the size you want to display: "))
# sep=input("Enter the seperator By Default space: ")
obj.character(s)