# with open ('sample.txt ',"w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a simple file.\n")
# with open ("sample.txt", 'r') as file:
    # contents = file.read();
    # print ('file contents: ')
    # print(contents)
# with open("sample.txt", "r") as file:
#     lines=file.readlines()
#     print('File content as list:')
#     print(lines)
# Open a file in write mode
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")
# Open a file in read mode
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
# Open a file in append mode
with open('output.txt', 'w') as file:
    file.write("\nThis line is appended.")

with open('output.txt', 'r') as file:
    content = file.read()
    print(content)






