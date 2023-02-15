"""
150. Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should TRUNCATE toward ZERO.

It is guaranteed that the given RPN expression is always valid. 
That means the expression would always evaluate to a result, 
and there will not be any division by zero operation.
"""
from typing import List

def evaluate(expression: str) -> int:
    intermediate_results: List[int] = []
    delimiter = ','
    operators = {
        '+': lambda y, x: x+y,
        '-': lambda y, x: x-y,
        '*': lambda y, x: x*y,
        '/': lambda y, x: int(x/y)
    }

    L = expression.split(delimiter)
    print(L)

    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(operators[token](intermediate_results.pop(), intermediate_results.pop()))
        else:# token is number
            intermediate_results.append(int(token))

    return intermediate_results[-1]


print(evaluate("2,1,+,3,*,-11,+"))
print(evaluate("10,6,9,3,+,-11,*,/,*,17,+,5,+"))

"""
Time complexity is O(n) and Space O(1)
"""


A = [10,3,1,4,5]
s = lambda y , x : x - y
#      y=5        x=4
print(s(A.pop(), A.pop()))
#      y=1        x=3 
print(s(A.pop(), A.pop()))

#Leet Code Solution
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         intermediate_results: List[int] = []

#         operators = {
#             '+': lambda y, x: x+y,
#             '-': lambda y, x: x-y,
#             '*': lambda y, x: x*y,
#             '/': lambda y, x: int(x/y)
#         }

#         for token in tokens:
#             if token in operators:
#                 intermediate_results.append(operators[token](intermediate_results.pop(),intermediate_results.pop()))
            
#             else:# token is number
#                 intermediate_results.append(int(token))

#         return intermediate_results[-1]

