# with open ('sample.txt ',"w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a simple file.\n")
# with open ("sample.txt", 'r') as file:
#     contents = file.read();
#     print ('file contents: ')
#     print(contents)
with open("abc.txt", "r") as file:
    lines=file.readlines()
    print('File content as list:')
    print(lines)


