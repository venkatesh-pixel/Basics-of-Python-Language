'''DATA TYPES - It is used to represent data of which type are used to perform a specific operation/task in program. In this we have 2 types
1. Individual/single valued Data Type
2. Multi valued datatype/collection datatype

1.Individual/single valued Data Type:- here only one value can de assigned and classified into 2 types
    a.Numeric D.T
     1(a)Integer:- It is a single Valued numeric D.T where only numbers without decimal point is accepted.
     2(a)Float:- It is a single Valued numeric D.T where numbers with decimal point is accepted.
     3(a)Complex:- It is a single Valued numeric D.T which contains a number which is in the form of a+bj format, which has 'a' in real part and 'bj' as an imaginary part.
                Here real part is not mandatory,but imaginary part is mandatory.

    b.Boolean:- It is a individual D.T which contains only two values TRUE or FALSE'''

'''Type() - gives what type of data is assigned to a particular variable
        EX: a = 10
        print (type(a))
        O/P
        Class(<type>'int')'''

'''Typecasting : Conversion from one datatype to another
      int --> float, complex --> possible
      float --> int, complex --> possible
      complex --> int, float --> not possible'''

# a = -10
# print(type(a))      #<class 'int'>
# a = 7
# print(float(a))     #7.0
# print(complex(a))       #(7+0j)
# print(complex(a, -9))        #(7-9j)
# print(bool(a))      #True

# a = -9.8
# print(int(a))       #9
# print(complex(a))           #(-9.8+0j)
# print(complex(a, -7))       #(-9.8-7j)
# print(bool(a))

# a = 2 + 6j
# print(int(a))     #TypeError
# print(float(a))     #TypeError
# print(bool(a))      #True

# a = True
# print(a)
# print(type(a))      #<class 'bool'>
# print(int(a))       #1
# print(float(a))     #1.0
# print(complex(a))   #(1+0j)

#########################################################
'''Boolean'''
# print(bool(-1))
# print(bool(0.0000007))
# print(bool(0+0j))
# print(bool(-0.9))

# print(bool(0))
# print(bool(int()))
#
# print(bool(0.0))
# print(bool(float()))
#
# print(bool(0j))
# print(bool(complex()))
#
# print(bool(False))
# print(bool(bool()))

'''
1. Default value of int is 0 and int()
2. Default value of float is 0.0 and float()
3. Default value of complex is 0+0j/0j and complex()
4. Default value of boolean is False and bool()
'''
#############################################################
'''dir() : Will give the list of attributes'''
# a = 1
# b = 2
# print(a + b)
# print(dir(a))

################################################################
'''isinstance() : It is an inbuilt function. It will check if the value belongs to the 
given datatype or not. If yes, it will give True else False
Syntax : isinstance(value, datatype)
'''
# print(isinstance(-7, int))      #True
# print(isinstance(89, float))    #False
# print(isinstance(2, int, float))        #TypeError
# print(isinstance(2, (int, float)))

