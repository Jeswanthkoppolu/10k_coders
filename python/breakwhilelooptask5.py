#Write a program to check input string is palindrome or not using while loop
str=input("enter input:")
str=str.lower()
start=0
end=len(str)-1
palindrome=True
while start<end:
    if str[start]!=str[end]:
        palindrome=False
        break
    start+=1    
    end-=1
if palindrome:
    print("The string is palindrome")    
else: 
    print("The string is not a palindrome")



#Write a program to reverse a number without converting into string
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10             
    reversed_num = reversed_num * 10 + digit  
    num = num // 10                
print("Reversed number is:", reversed_num)       




