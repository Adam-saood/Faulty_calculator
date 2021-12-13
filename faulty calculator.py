# I Design a calculator which will corrrectly solve all problem except the following ones:
# 45 * 3 = 555
# 56+9 = 77
# 56/6 = 4

print("Welcome to faulty calculator")
op = input("Enter operator: \n * , +  , / , - \n")
num1 = int(input("enter a first number: "))
num2 = int(input("Enter a second number: "))
if op=="*":
     if num1 * num2 == 45*3:
         print(num1,"*",num2,"=","555")
     else:
        print(num1,"*",num2,"=",int(num1)*int(num2))
if op=="+":
     if num1 + num2 == 56+9:
         print(num1,"+",num2,"=","77")
     else:
        print(num1,"+",num2,"=",int(num1)+int(num2))
if op=="-":
     if num1 * num2 == 45*3:
         print(num1,"-",num2,"=","555")
     else:
        print(num1,"-",num2,"=",int(num1)-int(num2))
if op=="/":
     if num1 / num2 == 56/9:
         print(num1,"/",num2,"=","4")
     else:
        print(num1,"/",num2,"=",int(num1)/int(num2))
else:

    print("❤️Thanks for using calculator")