
"""
To run

python3 file_split.py sample.txt number_of_lines

"""

import sys

def read_and_split(filename,num_of_lines):
    with open("{}".format(filename),"r") as f:
        lines = f.readlines()
        start = 0
        jump = num_of_lines
        while True:
            # we add the first set of `num_of_lines` lines and yield it
            yield lines[start:jump]
            # then keep on progressing along the lines list by adding `num_of_lines` to it
            start += num_of_lines
            jump  += num_of_lines
            # this one is for the last part
            # this checks if we are near to the end of the file
            # dumps the remaining lines 
            if (len(lines)-jump) <= num_of_lines:
                yield lines[jump:]
                break

def write_file_to_multiple_files(filename,num_of_lines):
    # read file and split into list
    print("Running...")
    num_of_lines = int(num_of_lines)
    hold = list(read_and_split(filename,num_of_lines))
    for lines_list in range(len(hold)):
        with open("{}-part{}.txt".format(num_of_lines,lines_list),"w") as final_file:
            lines_in_file = ""
            for lines in hold[lines_list]:
                lines_in_file += lines
            final_file.write(lines_in_file)
    print("Done...{} was splitted into {} text files".format(filename,len(hold)))

file_name = sys.argv[1]
lines_per_file = sys.argv[2]

if __name__ == "__main__":
    write_file_to_multiple_files(file_name,lines_per_file)
