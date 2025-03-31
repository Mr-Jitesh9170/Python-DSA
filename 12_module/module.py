# Module=> module is nothin but importing and exports the prewritten/packeges code in one to another files.

# There is tow type of module.
# i) built in module=> this module dowloaded using pip manager to use in our codebase.
# ii) user made module=> this module written by user which is imported from one to another.

# Note=>
# i) module can imported and exported if user written.
# ii) module while importing can changed its name.
# iii) builtin module can be imported anywhere if need.
# iv) we can import any another nested module using dot operator.
# v) in python if any variable, function , object created , it would be automatically exported.


# Way to importing in python=>

# Example-1=> General imports.
import userDetail

print(userDetail.name)

# Example-2=> Importing using alias.
import userDetail as user

print(user.name)

# Example-3=> Importing only necessary data.
from userDetail import greeting, name
greeting();