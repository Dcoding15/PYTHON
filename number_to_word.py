#! /usr/bin/python3

n = input("Enter a number between 1 to 999999999: ")

word = {0:'', 1:'ONE ', 2:'TWO ', 3:'THREE ', 4:'FOUR ', 5:'FIVE ', 6:'SIX ', 7:'SEVEN ', 8:'EIGHT ', 9:'NINE ', 10:'TEN ', 11:'ELEVEN ', 12:'TWELVE ', 13:'THIRTEEN ', 14:'FOURTEEN ', 15:'FIFTEEN ', 16:'SIXTEEN ', 17:'SEVENTEEN ', 18:'EIGHTTEEN ', 19:'NINETEEN ', 20:'TWENTY ', 30:'THIRTY ', 40:'FOURTY ', 50:'FIFTY ', 60:'SIXTY ', 70:'SEVENTY ', 80:'EIGHTY ', 90:'NINETY '}

def t1():
    l = len(n)
    return word[int(n[l-1])]

def t2():
    l = len(n)
    if int(n[l-2]) > 1:
        return word[int(n[l-2])*10] + word[int(n[l-1])]
    elif int(n[l-2]) == 0:
    	return t1()
    else:
	    return word[int(n[l-2:])]
#------------------------------------------------------------
def tmp1(s):
    l = len(s)
    return word[int(s[l-1])]

def tmp2(s):
    l = len(s)
    if l == 2:
    	if int(s[l-2]) >= 1:
        	return word[int(s[l-2])*10] + word[int(s[l-1])]
    	elif int(s[l-2]) == 0:
        	    return tmp1(s)
    elif l == 1:
    	if int(s[l-1]) >= 1:
    		return word[int(s[l-1])]
    	elif int(s[l-1]) == 0:
    		return tmp1(s)
    elif l == 3:
    	return word[int(s[l-2:])]
#------------------------------------------------------------
def t3():
    l = len(n)
    if int(n[l-3]) > 0:
        return word[int(n[l-3])] + 'HUNDRED ' + t2()
    else:
        return t2()

def t4():
    l = len(n)
    if int(n[:l-3]) > 0:
        return tmp2(n[:l-3]) + 'THOUSAND ' + t3()
    else:
        return t3()

def t5():
    l = len(n)
    if int(n[:l-5]) > 0:
        return tmp2(n[:l-5]) + 'LAKH ' + t4()
    else:
        return t4()

def t6():
    l = len(n)
    if int(n[:l-7]) > 0:
        return tmp2(n[:l-7]) + 'CRORE ' + t5()
    else:
        return t5()

if len(n) > 9 or not n.isnumeric():
    print('Please enter within the range or enter only number !!!')
else:
    if len(n) == 1:
        print(t1())
    elif len(n) == 2:
        print(t2())
    elif len(n) == 3:
        print(t3())
    elif len(n) == 4 or len(n) == 5:
        print(t4())
    elif len(n) == 6 or len(n) == 7:
        print(t5())
    elif len(n) == 8 or len(n) == 9:
        print(t6())
