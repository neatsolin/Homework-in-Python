# isFound = False
# result = 0
# while not isFound:
#     number = int(input("Enter your number: "))
#     result += number
#     if result == 30:
#         print("You are correct")
#         isFound = True
#     elif result > 30:
#         print("It's not correct")
#         isFound = True
#     else:
#         print("Sum more")

# isfound = False
# while not isfound:
#     text = input("Enter text: ")
#     if len(text) != "5":
#         print("It is not corret")
#     elif len(text)== "5":
#         print("it is corret")

# text = input("Enter text: ")
# result =""
# for char in text :
#     if char== "@":
#         result = ("Good password")
#     elif char == char.upper():
#         result= ("password weak")
# print(result)
 
# 1
# isfound = False
# while not isfound:
#     name = input("Enter text : ")
#     if len(name) == 5:
#          print(name)
#          isfound = True
#     else:
#          print("Try agian")


# ext=input("enter here:")
# while (len(text) )!=5:
#     print("Try more")
#     text=input("enter here:")
# print("It's Correct")


# sumA = 0 
# while sumA < 2:
#     text = input("Enter your word: ")
#     for char in text:
#         if char == "A" or char == "a":
#             sumA += 1
#     if sumA < 2:
#         print("Try agian")
#         sumA = 0
# print(text)

# 
# first way 
# text = "hello world" 
# isFound_O = False
# index = -1
# while not isFound_O:
#     index += 1
#     if text[index].lower() == "o":
#         isFound_O = True
# print(index)

# second  way 
# text = "helolo world"
# index = 0
# result = -1

#     #   Extraclass
# Ex1
# text = input("Enter text: ")
# count_a =0
# count_e = 0
# for char in text:
#     if char.lower()== "a":
#         count_a += 1
    
#     elif char.lower()== "e":
#         count_e += 1
# print(count_e)
# print(count_a)


# text = "Mengheang"
# result = ""
# for char in text:
#     if char.lower() == "e" or   char.lower()== "a":
#         result += "x"
#     else:
#         result+= char
# print(result)

# isfound =False
# index = 0
# result = ""
# while not isfound:
#     text = input("Enter text: ")
#     index +=1
#     if text(index) != "a":
#         index == result
#     elif text(index).lower() == "a":
#         isfound = True
#         Ex1
# text = input("Enter text: ")
# for char in text:
#     print(char)


# Ex2 - String
# Enter text and display number of letter

# text= input("Enter text: ")
# for i in range(len(text)):
#     print(i)

# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter

# text = input("Enter text: ")
# isfound = False
# i =0
# while i <len(text):
#     if text[i].isupper():
#         print("Yes")
#         isfound= True
#     i += 1  
# if not isfound:
#     print("NO")
#     i += 1

# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)

# Q1
# text = ("3 4 5 6")
# for i in range(len(text)):
#     if text[i] != " ":
#        print(text[i])
# Q2
# text = input("Enter text: ")
# sum = 0
# for i in range(len(text)):
#     sum += int(text[i])
# print(sum)
   
# or
# text = input("Enter your number here : ")
# sum = 0
# letter = ""
# for i in range(len(text)):
#     if text[i] == " ":
#         sum += ""
#     else:
#         letter += text[i]
#         sum += int(text[i])
# print(letter)
# print("Total :",sum)



# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 

# Q1
# text = "454639"
# count_odd = 0
# count_even =0
# for i in range(len(text)):
#     if i%2 ==0:
#         count_odd += 1
#     elif i%2 ==1:
#         count_even +=1
# print(count_odd)
# print(count_even)

# Q2
# text = input("Enter text: ")
# total= 0
# for i in range(len(text)):
#     total+= int(text[i])
# print(total)

# Q3
# text = input("Enter text: ")
# count_even =0
# for i in range(len(text)):
#     if int(text[i])% 2 == 0:
#         count_even += int(text[i])
#         print(count_even)

# Q4
# text = input("Enter text: ")
# lastindex= len(text) -1
# result =""
# for i in range(len(text)):
#     result += text[lastindex-i]
# print(result)

# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"

# num = int(input("Enter text: "))
# if num% 2 == 0:
#     print("even")
# else:
#     print("odd")

# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20


# isfound_number = False
# while not isfound_number:
#     number = int(input("Enter number : "))
#     if number >= 10 and number <=20:
#         print("Continue")
#     else:
#         isfound_number = True
# print("Out of range")



# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8

# Q1
# text = input("Enter text: ")
# count_eight =0
# for i in range(len(text)):
#     if text[i]=="8":
#         count_eight += 1
#         print(count_eight)

# Q2
# text = input("Enter text: ")
# isfound =False
# index = 0
# result=""
# while not isfound:
#    index+=1
#    if text[index] == "8":
#       isfound =True
#       result =index
# print(result)

# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"

# Q1
# text = input("enter text:")
# space = ""
# for i in range(len(text)):
#     if text[i]  != "":
#         space += text[i] + ""
# print(text)

# Q2
# text = "3 4 5 6"
# result = ""
# for i in range (len(text)):
#     if text[i]!=" ":
#        result += str(int(text[i])*2) + " "
# print(result)

# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
print("Please enter your number : ")
bigest_number = 0
smailest_number = 0
for i in range(5):
    number = int(input("Enter number : "))
    if bigest_number == 0 and smailest_number == 0:
        bigest_number = number
        smailest_number = number
    else:
        if number > bigest_number:
            bigest_number = number
        if number < smailest_number:
            smailest_number = number
print("Bigest number : ", bigest_number)
print("Smaillest number : ", smailest_number)

    










