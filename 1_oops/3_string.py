# Create object as string =>


# 1 One way=> if you want to make a meaningfull object ,
# and whenever you will print it will show in human read format.
class StringAsObj:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return self.name


print(StringAsObj("jitesh", "pandey"))


# 2 Second way=> it is attribute way to makin object , it is quite easy,
# but whenever you will print this obj then it would not be in human readable formate.
class StringAsAttributes:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def stringReturn(self):
        return self.lastname


print(StringAsAttributes("Jay", "Pandey").lastname)