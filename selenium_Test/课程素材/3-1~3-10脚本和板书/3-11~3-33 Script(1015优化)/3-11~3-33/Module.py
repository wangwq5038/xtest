#import time
import random
from time import sleep

from School.Student import Student

#print(time.ctime())
num=random.randint(10,20)
print(num)
sleep(5)
print("Sleep over!")

stu1=Student('jack','Beijing')
stu1.talk()
stu2=Student('Harry','Shanghai')
stu2.talk()

