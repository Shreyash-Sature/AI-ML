class Student:         #class

    subject = "Maths"  # \
    division = "TE-D"  #  => all these are class variables
    college = "DYPIT"  # /

stud1 = Student()
stud2 = Student()      # these two are objects 

print(stud1.subject , stud2.college)

""" class variables are shared with all objects but object variable is specific of that object"""

#increases reusibality of code