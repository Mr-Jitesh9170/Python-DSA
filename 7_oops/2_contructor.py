#2 Constructor in class =>
class Parent:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
  
    def sum(self):
        print(self.x+" "+self.y);
        
parent1=Parent(10,"hello");

# modify properties=>
parent1.x=20;
parent1.y=30;
parent1.sum()

# delete properties=>
del parent1.x;

print(parent1.y)