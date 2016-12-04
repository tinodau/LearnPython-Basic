
# QUOTE ======================
print ('hello single quote!') # COMMENT
print ("""hello tripple quote!""")
print ("hello double quote! \n") # with new line


# NUMBERS ======================
import sys; x = "coba"; sys.stdout.write( x + "\n")
bulat = 9
pecahan = 9.9
kata = "Sembilan"


# VARIABLE ======================
print (bulat)
print (pecahan)
print (kata,"\n")
var1, var2, var3 = 10, 10.1, "Sepuluh"


# STRING ======================
str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST\n") # Prints concatenated string


# ARRAY / LISTS ======================
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist,"\n") # Prints concatenated lists


# TUPLE (READ-ONLY) ======================
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print (tuple) # Prints complete tuple
print (tuple[0]) # Prints first element of the tuple
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints tuple two times
print (tuple + tinytuple,"\n") # Prints concatenated tuple


# DICTIONARY (KEY - VALUE) ======================
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values(),"\n") # Prints all the values


# BASIC OPERATION ======================
a = 21
b = 10
c = 0
c = a + b; print ("Line 1 - Value of c is ", c)
c = a - b; print ("Line 2 - Value of c is ", c )
c = a * b; print ("Line 3 - Value of c is ", c)
c = a / b; print ("Line 4 - Value of c is ", c )
c = a % b; print ("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b; print ("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b; print ("Line 7 - Value of c is ", c,"\n")


# COMPARISON ======================
a = 21
b = 10
if ( a == b ):
    print ("Line 1 - a is equal to b")
else:
    print ("Line 1 - a is not equal to b")

if ( a != b ):
    print ("Line 2 - a is not equal to b")
else:
    print ("Line 2 - a is equal to b")

if ( a < b ):
    print ("Line 3 - a is less than b" )
else:
    print ("Line 3 - a is not less than b")

if ( a > b ):
    print ("Line 4 - a is greater than b")
else:
    print ("Line 4 - a is not greater than b")

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21
if ( a <= b ):
    print ("Line 5 - a is either less than or equal to b")
else:
    print ("Line 5 - a is neither less than nor equal to b")

if ( b >= a ):
    print ("Line 6 - b is either greater than or equal to b\n")
else:
    print ("Line 6 - b is neither greater than nor equal to b\n")


# BITWISE OPERATOR ======================
a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0
c = a & b;
# 12 = 0000 1100
print ("result of AND is ", c,':',bin(c))
c = a | b;
# 61 = 0011 1101
print ("result of OR is ", c,':',bin(c))
c = a ^ b;
# 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))
c = ~a;
# -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))
c = a << 2;
# 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))
c = a >> 2;
# 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c),"\n")


# MEMBERSHIP ======================
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")

if ( b not in list ):
    print ("Line 2 - b is not available in the given list")
else:
    print ("Line 2 - b is available in the given list")

c=b/a
if ( c in list ):
    print ("Line 3 - a is available in the given list\n")
else:
    print ("Line 3 - a is not available in the given list\n")


# IDENTITY OPERATOR (compare memory location (Same or Not))
a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is b ):
    print ("Line 2 - a and b have same identity")
else:
    print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
    print ("Line 3 - a and b have same identity")
else:
    print ("Line 3 - a and b do not have same identity")

b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))
if ( a is not b ):
    print ("Line 5 - a and b do not have same identity\n")
else:
    print ("Line 5 - a and b have same identity\n")


# LOOP STATEMENT (WHILE)======================
count = 0
while (count < 3):
    print ('The count is:', count)
    count = count + 1
print ("Good bye!\n")


# LOOP STATEMENT (WHILE - ELSE) ====================
count = 0
while count < 3:
    print (count, " is less than 5")
    count = count + 1
else:
    print (count, " is not less than 5\n")


# FOR - LOOP STATEMENT ==================
for letter in 'Python': # traversal of a string sequence
    print ('Current Letter :', letter)
print()

fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # traversal of List sequence
    print ('Current fruit :', fruit)

print ("Good bye!")


# FOR (FOR - ELSE) ======================
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num%2==0:
        print ('the list contains an even number')
        break
else:
    print ('the list doesnot contain even number')


# NESTED LOOP ==================
for i in range(1,6):
    for j in range(1,6):
        k=i*j
        print (k, end=' ')
    print()
print("\n")


# CONDITION (IF) ======================
amount=int(input("Enter amount: "))

if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
elif amount<5000:
    discount=amount*0.10
    print ("Discount",discount)
else:
    discount=amount*0.15
    print ("Discount",discount)
print ("Net payable:",amount-discount,"\n")



# BREAK - CONTINUE - PASS ===============
for letter in 'Python': # First Example
    if letter == 'h':
        break
    print ('Current Letter :', letter,"\n")
# --------

for letter in 'Python': # First Example
    if letter == 'h':
        continue
    print ('Current Letter :', letter,"\n")

# ---------

for letter in 'Python':
    if letter == 'h':
        pass
        print ('This is pass block')
    print ('Current Letter :', letter,"\n")


# NUMBER (absolute / mutlak) ==========
print ("abs(-45) : ", abs(-45))
print ("abs(100.12) : ", abs(100.12),"\n")

# NUMBER (Ceiling / pembulatan) ==========
import math # This will import math module
print ("math.ceil(-45.17) : ", math.ceil(-45.17))
print ("math.ceil(100.12) : ", math.ceil(100.12))
print ("math.ceil(100.72) : ", math.ceil(100.72))
print ("math.ceil(math.pi) : ", math.ceil(math.pi),"\n")


# NUMBER (MAX - MIN) ======================
print ("max(80, 100, 1000) : ", max(80, 100, 1000))
print ("max(-20, 100, 400) : ", max(-20, 100, 400),"\n")

print ("min(80, 100, 1000) : ", min(80, 100, 1000))
print ("min(-20, 100, 400) : ", min(-20, 100, 400),"\n")


# POW (PANGKAT) ============================
print ("math.pow(100, 2) : ", math.pow(100, 2))
print ("math.pow(100, -2) : ", math.pow(100, -2),"\n")

# ROUND (PEMBULATAN - JUMLAH) =============
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2),"\n")

# SQRT (AKAR) ==============================
print ("math.sqrt(100) : ", math.sqrt(100))
print ("math.sqrt(49) : ", math.sqrt(49),"\n")


# =====================================
# RANDOM NUMBERS ======================
import random

# CHOICE
print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1,
2, 3, 5, 9]))
print
("returns random character : ", random.choice('Hello World'),"\n")

# RANDRANGE (START - STOP, STEP)
# randomly select an odd number between 1-100
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# randomly select a number between 0-99
print ("randrange(100) : ", random.randrange(100))




# INPUT ======================
input("Cannot Blank, Write somthing!")
input("Enter")
