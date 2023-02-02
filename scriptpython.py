import os
import re

from myExperience import module as fomodule



print(fomodule.readmode)
print(fomodule.readtofile('notes.txt'))

print("*******************************")

print(os.getcwd())
print("*******************************")
print(os.system('dir'))
print("*******************************")
print(os.listdir('/'))

print("*****************************")

str = "Hello, I'm Aya Hassan "
pattern = re.search("^Hello.Aya.",str)
print(pattern)