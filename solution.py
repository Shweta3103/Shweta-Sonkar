import sys
import time

SIZE = 9

def files_to_list (inputfile = None):
    if inputfile is None:
        print ("Inputfile is invalid, please give valid input")
        sys.exit(0)
    result = []
    inputfile.seek(0,0)
    for line in inputfile:
        tmp =[]
        line = line.strip().split(",")
        tmp = list(map (lambda x:int(x), line))
        result.append(tmp)
    return result



def get_column_list (sudoku_2D_list, col):
    tmp = [row[col] for row in sudoku_2D_list]
    return tmp

def get_lower_index (idx = None):
    return int (idx/3)

def get_home_list (sudoku_2D_list, row, col):
    r_idx = 3 * get_lower_index (row)
    c_idx = 3 * get_lower_index (col)
    result = []

    for i in range (r_idx, r_idx + 3):
        for j in range (c_idx, c_idx + 3):
            result.append(sudoku_2D_list[i][j])
    return result


def fill_possible_value (sudoku_2D_list, row, col):
    if (sudoku_2D_list[row][col] != 0):
        print ("Not needed to update given value")

    possible_solution = []
    for val in range(1, 10):
        if val in sudoku_2D_list[row]:
            # val cannot be filled at row, col position as it exit the given row
            continue

        if val in get_column_list (sudoku_2D_list, col):
            # val cannot be filed at row, col position as it exist at the given column 
            continue

        if val in get_home_list (sudoku_2D_list, row, col):
            # val cannot be filled at row, col position as it exist at the given home
            continue

        # reach here means val can be filled if only single possible input available
        possible_solution.append (val)

    if len(possible_solution) == 1:
        print ("Filling {} at r={},c={} out of {}".format(possible_solution[0], row, col, possible_solution))
        # value to be updated only when single solution is available
        sudoku_2D_list[row][col] = possible_solution[0]
    else:
        print ("Multiple solution at r={},c={} out of {}".format(row, col, possible_solution))


def check_zero_presence (sudoku_2D_list):
    for x in sudoku_2D_list:
        if 0 in x:
          return False
    return True

def update_sudoku_solution (sudoku_2D_list = None):
    if sudoku_2D_list is None:
        print ("list is empty")
        sys.exit(0)

    sudoku_puzzle_complete = 0
    while (sudoku_puzzle_complete == 0):
        for i in range (0, SIZE):
            for j in range (0, SIZE):
                if sudoku_2D_list[i][j] == 0:
                    fill_possible_value (sudoku_2D_list, i, j)
        rc = check_zero_presence (sudoku_2D_list)
        if rc == False:
           ''' meaning we have some more block to fill '''
           sudoku_puzzle_complete = 0
        else:
           sudoku_puzzle_complete = 1
        

def print_output (sudoku_2D_list, outputfile):
    outputfile.write("\n-----------------------\n")
    for i in range(0, 9):
        for j in range (0, 9):
            val = sudoku_2D_list[i][j]
            outputfile.write( str(val))
            outputfile.write(" ")
            if j%3 == 2:
                outputfile.write("| ")
        if (i%3 == 2):
            outputfile.write("\n-----------------------\n")
        else:
            outputfile.write("\n")
            


if __name__ == "__main__":
    ''' update file path according '''
    inputfile = open('./sudoku_input_file.txt',mode='r')
    for lines in inputfile:
       print(lines)    

    print("==================== OUTPUT ================")

    sudoku_2D_list = files_to_list (inputfile)

    update_sudoku_solution (sudoku_2D_list)

    outputfile=open('./sudoku_output_file.txt',mode='w')
    print_output (sudoku_2D_list, outputfile)
    outputfile.close()
