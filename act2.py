try:
    n=int(input("please enter a number- "))
    n1=int(input("please enter a number- "))
    div=n/n1
    print(div)

except ValueError :
    print("please enter numerical value- ")

except ZeroDivisionError:
     print("division by zero is not possible")

except Exception as x:
     print("Error occured-",x)

finally:
     print("I will print no matter what ")