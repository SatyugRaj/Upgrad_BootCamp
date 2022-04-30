#!/usr/bin/env python
# coding: utf-8

# # Write a program to display whether the input is a digit or a letter of the alphabet.

# In[ ]:


# Take input
inp=input()
if inp in '0123456789':
    print('Integer')
else:
    print('Alphabet')
#write your code here


# # Write a program to accept a character and display its next and previous character. 

# In[ ]:


inp=input()
prev_char=chr(ord(inp)- 1)
next_char=chr(ord(inp) + 1)

#Write your code here
print(prev_char)
print(next_char)


# # Write a program to accept a string from the user, delete all vowels from the string and display the result. 

# In[ ]:


# Take input
s=input()

# Write your code here
def no_vowel (s):
    vowels=['a','e','i','o','u']
    trimm=[j for j in s if j.lower() not in vowels]
    final=''.join(trimm)
    return(final)
#Print the result
q=no_vowel(s)
print(q)


# # Write a program to accept three sides of a triangle as the input and print whether the triangle is valid or not.
# 
# (A triangle is valid if the sum of any two sides is greater than the third side.)

# In[ ]:


a,b,c= input().split()

# Write your code here
# Convert a,b,c into numeric type and check for the validity of triangle
a=int(a)
b=int(b)
c=int(c)
if (a+b>c and b+c>a and a+c>b):
    print('Valid')
else:
    print('Invalid')

