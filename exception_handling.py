try:
    a=b
except:
    print("the variable is not assigned")

try:
    a=b
except Exception as e:
    print(e)

try:
    result = 1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print("the real exception is caught?") # won't execute since the actual exception is not Zerodivsion

try:
    result = 1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print("the real exception is caught?")
except Exception as e:
    print(e)
    print("this is the Main exception which will always run") # will handle all types and so generally run

try:
    result = 1/2
    a=b
except NameError as ex:
    print(ex)
    print("the real exception is caught?") # this time it's caught
except Exception as e:
    print(e)
    print("this is the Main exception which will always run") # so general exception won't run now

# try, except, else and finally

x = int(input("enter the number to check"))
try:
    res = 10/x
    print(res)
except ValueError as v:
    print(v)
except TypeError as t:
    print(t)
except Exception as e:
    print(e)
else:
    print(" the try block is run without error")
finally:
    print("all the resources will be closed")

try:
    file =  open("OOPS.py",'r')
    content = file.read()
    a=b
except FileNotFoundError as ex:
    print(ex)
finally: # this won't execute since the exception is not caught actually
    if 'file' in locals() or not file.closed():
        print("file close") 
