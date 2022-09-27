
inputfile=open('/home/user/Documents/project codes/pythonProject/sudoku_input_file.txt',mode='r')
for lines in inputfile:
    print(lines)
    
outputfile=open('/home/user/Documents/project codes/pythonProject/sudoku_output_file.txt',mode='w')
for lines in inputfile:
    outputfile.write(lines)
outputfile.close()

def string_to_list(Str = None):
    lisst=str.split(",")
    return lisst


