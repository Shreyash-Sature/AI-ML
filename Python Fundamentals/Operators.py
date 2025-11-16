"""
Operators:

-Arithmatic : +, -, /, *, %, **
-Realtional/ Comaprisions : >, >=,<,<=, ==
-Assignment : = , +=
-Logical : not, and, or


OPERATOR PRECEDENCE:

()
**
*,/,%
+,-
==,!=,>,<,>=,<=
not
and
or


TYPE CASTING AND CONCERSION



"""
#Arithmatic
a =10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#module
print(a**b) # to the power of  

#Relational/Comaprisional Operators

print (a<b)
print (a<=b)
print (a>b)

#Assignment Operators

a = 10
a = a +1
a+=1
print(a)

#Type Casting

a =11.5
b=12
sum = int(a+b)
print(sum)




