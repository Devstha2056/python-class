"""5"""
 


"""d = int(input('enter the day:'))
day=int(d)
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")"""


# import datetime

# b = datetime.datetime.today()
# print(b)
# # print(b.strftime('%A'))

# a = datetime.datetime.now()
# print(b.strftime('%A'),a.strftime('%H:%M:%S'))


# class A:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class B(A):
#     def __init__(self, fname, lname, address):
#         A.__init__(self, fname, lname)  
#         self.address = address

#     def printaddress(self):
#         print(self.address)

# class C(B):
#     def __init__(self, fname, lname, address):
#         B.__init__(self, fname, lname, address)  


# x = B("Prami", "Olsen", "Kathmandu")

# x.printname()        
# x.printaddress()  



# class A:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class B(A):
#     def __init__(self, fname, lname, address):
#         super().__init__(fname, lname)  
#         self.address = address

#     def printaddress(self):
#         print(self.address)

# class C(B):
#     def __init__(self, fname, lname, address):
#         super().__init__( fname, lname, address)  


# x = B("Prami", "Olsen", "Kathmandu")

# x.printname()        
# x.printaddress()


# class Person:
#     def __init__(self, name, age):
#         self.name = name      # attribute
#         self.age = age        # attribute

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # 🔸 Create an object of the class
# person1 = Person("Devendra", 25)

# # 🔸 Access method using object
# person1.greet()



# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# user_input = int(input("Enter a number to check if it's prime: "))
# if is_prime(user_input):
#     print(f"{user_input} is a prime number.")
# else:
#     print(f"{user_input} is not a prime number.") 


# def is_prime(i,j):
#     if i <= 1:
#         return False
#     for n in range(2, i):
#         if i % n == 0:
#             return False
#     return True

# for i in range(2, 101):
#     if is_prime(i, 0):
#         print(f"{i} is a prime number.")

# user_input = int(input("Enter a number to check if it's prime: "))
# if is_prime(user_input, 0):
#     print(f"{user_input} is a prime number.")
# else:     
#     print(f"{user_input} is not a prime number.")       


def print_rose():   
    print("        _ _")
    print("      _{ ' }_")
    print("     { `.!.` }")
    print("     `-..-.-'") 
    print("       /   \\")
    print("      |     |")
    print("      |     |")
    print("       \\   /")
    print("        `-'")    
if __name__ == "__main__":
    print_rose()  