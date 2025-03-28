#3 arbitary argument=>
#i) passing unknown number of arguments.
#ii)using *keyword in peremeter can access passed arguments.

#Example-1
def sum(*numbers):
    return numbers[0]+numbers[1]+numbers[2]+numbers[3];

print(sum(1,2,3,5));