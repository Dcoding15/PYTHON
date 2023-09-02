#! /usr/bin/python3

# OPERATOR in python

'''

1) Arithematic opeator: +  -  *  **  /  //  %
2) Relational operator: <  >  <=  >=  ==  !=
3) Logical operator: and  or  not
4) Bitwise operator: &  |  ^  ~  <<  >>
5) Assignment operator: +=  -=  *=  **=  /=  //=  %=  &=  |=  ^=  >>=  <<=
6) Identity operator: is  is not
7) Membership operator: in  not in
8) Ternary operator: ( condition ) if ( statement ) else ( statement )

'''

# + and * operation using string

#print('abc'+'def')
# Output: abcdef

#print('abc'*5)
# Output: abcabcabcabcabc

#print(max(10, 20, 30, 40, 50, 60, 118))
# Output: 118

#print(min(10, 20, 30, 40, 50, 60, 118))
# Output: 10


# Arithematic operator

print(True + 20)					#21
print(False + 20)					#20
print(10 + 20)						#30
print(12.43 + 23)					#35.43
print(34.32 + 65.34)				#99.66
print(10+12j + 12)					#(22+12j)
print(10+12j + 12j)					#(10+24j)
print(10+12j + 23+76j)				#(33+88j)
print(10+12j + 23.33)				#(33.33+12j)
print(10+12j + 76.66j)				#(10+88.66j)
print(10.45+12.54j + 23.33+76.66j)	#(33.78+89.19999999999999j)

print(True - 20)					#-19
print(False - 20)					#-20
print(10 - 20)						#-10
print(12.43 - 23)					#-10.57
print(34.32 - 65.34)				#-31.020000000000003
print(10+12j - 12)					#(-2+12j)
print(10+12j - 12j)					#(10+0j)
print(10+12j - 23+76j)				#(-13+88j)
print(10+12j - 23.33)				#(-13.329999999999998+12j)
print(10+12j - 76.66j)				#(10-64.66j)
print(10.45+12.54j - 23.33+76.66j)	#(-12.879999999999999+89.19999999999999j)
