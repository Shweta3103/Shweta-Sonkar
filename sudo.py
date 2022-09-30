
inputfile=open('/home/user/Documents/project codes/pythonProject/sudoku_input_file.txt',mode='r')
for lines in inputfile:
    print(lines)
    

outputfile=open('/home/user/Documents/project codes/pythonProject/sudoku_output_file.txt',mode='w')
for lines in inputfile:
    outputfile.write(lines)
outputfile.close()
def string_to_list(inputfile = None):
    result=[]
    inputfile.seek(0, 0)
    for line in inputfile:
        temp = []
        line = line.strip()

        l1 = line.split(",")
        for l in l1:
            if l != '':
                temp.append(int(l))
    result.append(temp)
    print(result)
    return result
   
string_to_list(inputfile)


