#!/usr/bin/env python
# coding: utf-8

# # Write a program to display the multiplication table of a given number.# 

# In[ ]:


#Take input
n=int(input())
for i in range(1,11):
    print(n,'*',i,'=',n*i)


# # Write a program to accept a string value from the user and accept a char value from the user and find out the total occurrence of the char value in the string value. Note that the count is not case-sensitive

# In[ ]:


# Take input
input_string=input()
input_char=input()
print(input_string.count(input_string)+input_char.count(input_char))


# # Write a program to calculate the sum of the digits of a given number 

# In[ ]:


#Take input
n=int(input())
n=str(n)
# write your code here
def sum_digit(n):
    list_num=list(map(int,n.strip()))
    return sum(list_num)

# print the results
print(sum_digit(n))


# # Write a program to accept a number from the user and count the zeros, odd digits and non-zero even digits from the entered number.

# In[ ]:


# Take input
n=int(input())
n=str(n)
odd=['1','3','5','7','9']
even=['2','4','6','8']
zero=['0']
a=0
b=0
c=0
for i in n:
    if i in odd:
        a+=1
    elif i in even:
        b+=1
    elif i in zero:
        c+=1
print('Number of odd digits:',a)
print('Number of non-zero even digits:',b)
print('Number of zeros:',c)
#write your code here


# Another approach to the above problem is as given below ::>>

# In[ ]:


# Take input
n=int(input())

# creating three variables to keep the count of odd, even and zero digits
n_odd=0
n_even=0
n_zeros=0



while n>0:

# Storing the reminder(is also digit at one's place of n) of n%10
    r=n%10

    # If the reminder(is also digit at one's place of n) is 0, the digit is 0. Increase the count of zeros by 1
    if r==0:
        n_zeros+=1
        
    #If the reminder is divisible by 2, it is an even digit otherwise odd. Increase the respective counts
    elif r%2==0:
        n_even+=1
        
    else:
        r%2==1
        n_odd+=1
    
    # Updating the value of n by dividing it by 10 inorder to get the next digit during next iteration
    n=n//10
        
#Print the results
print("Number of odd digits:",n_odd)
print("Number of non-zero even digits:",n_even)
print("Number of zeros:",n_zeros)


# # Write a program that takes a string as the input and does the following:
# 
#     -Removes the numbers, special characters
# 
#     -Converts uppercase letters to lowercase letters, and vice versa 

# In[ ]:


#Take input
input_string=str(input())
output=''
for i in input_string:
    if (i>='a' and i <='z') or (i >='A' and i <='Z'):
        output=output+i
#print(output)
output2=''
for j in output:
    if j.islower():
        output2=output2+j.upper()
    elif j.isupper():
        output2=output2+j.lower()
print(output2)
#write your code here


# another approach for the above ques :->

# In[ ]:


#Take input
input_string=input()

#Initialising an empty string that will store the modified resultant string
new_str=''

# looping through the input_string where 'c' is each character of the string
for c in input_string:

    # if the character 'c' is an alphabet, implement the code following otherwise skip that character and go for next iteration
    if (c.isalpha()):
        
        # if the character 'c' is an uppercase, convert it into lowercase otherwise convert the character into uppercase
        if c.isupper():
            new_str=new_str+c.lower()
        else:
            new_str=new_str+c.upper()
        

print(new_str)


# In[ ]:




