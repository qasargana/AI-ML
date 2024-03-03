def add(a,b):
    return a + b
def factorial(n):
    if n == 0 :
        return 1
    else :
        return n * factorial (n-1)
numbers=[1,2,3,4,5]
doubled_numbers=list(map(lambda x:x * 2,numbers))
print('doubled numbers:', doubled_numbers)

even_numbers=list(filter(lambda x:x%2 == 0, numbers))
print("even numbers:", even_numbers)
squares = [x ** 2 for x in numbers]
print("squares:",squares)