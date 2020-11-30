#!/usr/bin/python3
def GradeMultiply(num1, num2):
    print("The first number_list: ", num1)
    print("The second number_list: ", num2)
    
    # Check the sign of the numbers
    sign = -1 if (num1[0]< 0) ^ (num2[0]<0) else 1
    print("Sign of the result will be: ", sign)
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0]*(len(num1) + len(num2))
    
    # results = n2 X n1
    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            result[i + j + 1] += num2[i] * num1[j]
            # Floor Division (//) - 
            # The division of operands where the result 
            # is the quotient in which the digits 
            # after the decimal point are removed. 
            # But if one of the operands is negative, 
            # the result is floored, 
            # i.e., rounded away from zero (towards negative infinity)
            
            # For example:
            # 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
            result[i + j] += result[i + j+ 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeros
    result =  result[next((i for i, x in enumerate(result)
                           if x != 0), len(result)):] or [0]

    return [sign * result[0]] + result[1:]

def GetSign(n)->int:
    sign = 1 
    if (n < 0):
        sign = -1
    return sign

n  = int(input("Enter 1st number: "))
sign = GetSign(n)
n = abs(n)
num1 = [int(x) for x in str(n)]
num1[0] = sign * num1[0]
print(num1)

n  = int(input("Enter 2nd number: "))
sign = GetSign(n)
n = abs(n)
num2 = [int(x) for x in str(n)]
num2[0] = sign * num2[0]
print(num2)

res = GradeMultiply(num1, num2)
strings = [str(r) for r in res]
res_string = "".join(strings)
res_int = int(res_string) 
print("result: ", res_int)