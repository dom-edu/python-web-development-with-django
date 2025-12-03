
# SOME TERMS 


virtual environment - is a sandbox , everything installed there does not affect system wide libraries 

## OOP Overview
```
class Student(object):

    # intializer that initizes fields 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    # string representation
    def __str__(self):
        return f"Name: {self.name} / Age: {self.age}"


student1 = Student("Dom", "30")
student2 = Student("Tom", "30")



#print(student1.name)
#print(student2.name)

#now because of our __str__ def of he Student() object
#we can directly print out string representation of the object

print(student1)
print(student2)
```
## Generic Views For Modularization  
```
from django.http import HttpResponse
from django.views import View # base view 


# we want the greetings view to always return a get request
class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)

# You can override that in a subclass:

# easily update it for overriding GreetingView's greeting
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
```





# USEFUL CMD STUFF

## show files in a directory by timestamp 
```
ls -la
```

## show all libraries installed in a virtual environment 
```
pip freeze
```

## save installed config of vm to requirements.txt 
```
pip freeze > requirements.txt
```

## install from requirements file 
```
pip install -r requirements.txt
```
## showing current working directory path
```
pwd  
i.e /Users/n/Documents/GitHub/python-web-development-with-django/03-Models-ORM-and-Admin
```


