#Program to change first and last letter of string

str=input("Enter the String : ")
r=str[-1:]+str[1:-1]+str[:1]
print(r)

'''
output:
Enter the String : abhishek
kbhishea
'''
