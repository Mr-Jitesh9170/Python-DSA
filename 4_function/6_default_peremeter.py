#6 Default parameter=>
#i)In function declaration can assign default parameter, if argument is not passed, then it will take default parameter.
 
#Example-1
def sum(a,b=2):
    print(a+b);
    
sum(10); #output=> 12

# OR

sum(10,20); #output=> 30