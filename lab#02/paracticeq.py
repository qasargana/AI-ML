try: 
     x=int (input("Enter a number"))
     if x < 0:
        raise ValueError("Input value must be non-negative.")
     print('Entered a number:', x)
except ValueError as e:
    # print('Error:', e)
     print("Custom error caught:", e)