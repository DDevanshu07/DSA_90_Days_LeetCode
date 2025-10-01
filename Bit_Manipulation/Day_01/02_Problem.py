"""
Leetcode problem 67. Add Binary 
Given two binary strings a and b, return their sum as a binary string.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = int(a,2),int(b,2)
        while b!= 0:
            add = a^b
            carry = (a&b)<<1
            a,b = add,carry
        return bin(a)[2:]