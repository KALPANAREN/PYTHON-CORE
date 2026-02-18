# read entire file
with open('example.txt','r') as rf:
    content = rf.read()
    print(content)

# read file line by line

with open('example.txt','r') as file:
    for line in file:
        print(line.strip())

#open new file for writing it

with open('example1.txt','w') as file:
    file.write('Hello Orgnaic World\n')
    file.write('this is the dream line')


#overwriting an existing file

with open('example1.txt','w') as file:
    file.write("let us the pedal for the dream\n")
    file.write("let us make sure we achieve it so soon\n")
    file.write("imagine a bite  of natural ripened fruits and natural forest u dream to build")

# write without overwriting

with open('example1.txt','a') as file:
    file.write("\nthis must be the destination to this life")

#writing list of lines to a file

lines = ['\nfirst line\n','second line\n','third line\n']
with open('example1.txt','a') as file:
    for line in lines:
        file.write(line) #file.writelines(lines) is also same

# work with binary file

binary_data = b'\x01\x02\x03\x04\x05'
with open('binary_file.bin','wb') as file:
    file.write(binary_data)

# reading binary file

with open('binary_file.bin','rb') as file:
    content = file.read()
    print(content)

# copying content from one file to another file

with open('example1.txt') as source:
    content = source.read()

with open('orglife.txt','w') as destination:
    destination.write(content)

# writing and reading a new file

with open('mydestination.txt','w+') as file:
    file.write("imagine diving into the well\n")
    file.write("imagine the ventilation of the manduva style\n")
    file.write("imagine the entry through the jasmine gate")

    # move the cursor to the begining of the file since the cursor is left at the line as line
    file.seek(0)
    # file.seek(20) moves the cursor to 20th character
    data = file.read()
    print(data)
# assignment- read a file and print no of lines, words and characters in that file


