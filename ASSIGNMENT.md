ASSIGNMENT-3 
'''what is r+, w+, a+ and Create a calculator where the values and operators need to be given by the user and store the values in the file''' 

with open("file.txt", "w+") as f:
 f.write("hi"\n")
 f.write("i am sowmya\n")
 f.write("welcome to my pc in")
 f.seek(0)        
 lines.read() 
 print(lines)

with open('file.txt', 're') as f:
 f.write("welcome")

with open("File.txt", 'a+') as f:
 f.write("i am starting new project").
 f.seek(0)
 lines=f.readlines() 
 print(lines)


CALCULATOR

def sum():
 a=int(input("enter the num1- "))
 b-int(input("enter the nut-"))
 print("sum", ab) 
 with open('calculator.txt',"a") as f:
   f.write(f"\n sum of {a} and {b} is {a+b}\n")

def sub(b):
  a=int(input("enter the num1- "))
  b=int(input("enter the num1- "))
  print("sub",a-b)
  with open('calculator.txt',"a") as f:
   f.write(f"\n subtraction of {a} and {b} is {a-b}\n")
         
def mul():
 a=int(input("enter the num1- ")) 
 b=int(input("enter the numi- "))
 print("mul",a*b)
 with open("calculator.txt","a") as f:
   f.write(f"\n multiplication of {a} and {b} is {a*b}\n")

def div():
 a=int(input("enter the num1- "))
 b=int(input("enter the num1- "))
 print("div", a/b)
 with open("calculator.txt","a") as f:
  f.write(f"\n division at {a} and {b} is {a/b}\n")
         
sum()
div()
