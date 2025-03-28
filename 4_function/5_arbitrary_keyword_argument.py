#5 Arbitrary keyword argument=>
#i) Arbitrary keyword arguments allow a function to accept an unlimited number of keyword arguments.
#ii) You can declare it using **parameter_name, which collects all keyword arguments as a dictionary.

def sum(**number):
    print(number['a']); #output=> 11
    print(number['b']); #output=> 10
    print(number["c"]); #output=> 9

sum(b=10,c=9,a=11);