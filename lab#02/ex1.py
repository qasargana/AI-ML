try:
    x=int (input("Enter a number"))
    z=int (input('Enter a number'))
    y= z/x
    print('Result:',y)
except ValueError:
    print('please enter a valid integer')
except ZeroDivisionError:
    print('cannot divide by zero')
except Exception as e:
    print('An error occur')
    