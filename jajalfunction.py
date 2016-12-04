def coba1(mylist):
    "Docstring cobacoba"
    print("Value inside function before change: ",mylist)
    mylist[2] = 50
    print("Value inside function after change : ", mylist,"\n")
    return

mylist = [1, 2, 3]
print("\nValue OUTSIDE function: ", mylist)
coba1(mylist)

# =====================================================

def coba2(mylist2):
    "Docstring coba2"
    mylist2 = [1,2,3,4,5]
    print("Value inside function: ", mylist2)
    return

mylist2 = [6,7,8,9,0]
coba2(mylist2)
print("Value outside function: ", mylist2,"\n")

# =====================================================

def coba3(str1):
    "Docstring coba3"
    print(str1)
    return

coba3(str1 = "passing string :D ")

# =====================================================

def coba4(str1, str2):
    "Docstring coba4"
    print("\nName : ", str1)
    print("Age  : ", str2,"\n")
    return

coba4(str1="Tino", str2=20)

# =====================================================

def coba5(arg1, *berderet):
    "Docstring coba5"
    print("Output: ")
    print(arg1)
    for deret in berderet:
        print(deret)
    return

coba5(1)
coba5(2,3,4)


# ANONYMOUS FUNCTION
# =====================================================

sum = lambda arg1, arg2 : arg1*arg2

print("\nTotal : ", sum(2,3))
print("Total : ", sum(5,2),"\n")


# RETURN STATEMENT
# =====================================================

def coba6(arg1, arg2):
    "Docstring coba6"
    total = arg1 + arg2
    print("Total inside function : ", total)
    return total

print("Total outside function : ", coba6(5,10),"\n")


# GLOBAL - LOCAL (VARIABLE)
# =====================================================

total7 = 0  # GLOBAL

def coba7(arg1, arg2):
    "Docstring coba7"
    total7 = arg1 * arg2
    print ("Local Variable : ",total7)
    return

coba7(5,2)
print ("Global Variable : ", total7, "\n")


# IMPORT MODUL
# =====================================================

import jajalmodul

jajalmodul.cobapackage("Tino")
