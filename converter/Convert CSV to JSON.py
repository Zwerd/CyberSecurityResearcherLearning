
#this script convert csv file to json format
import os
import stat

os.mknod('c1p1-conv2.csv', 0600|stat.S_IRUSR)

original_file = open("c1p1.csv","r")
converted_file = open("c1p1-conv.csv","w")
#line1 = original_file.readline()
all_list =[]

def file_len(fname):
    with open(fname) as f:
        print enumerate(f)
        for loop, l in enumerate(f):
            pass
    return loop + 1

def first_line_list(line1):
    word = ''
    list1 = []
    for loop in range(len(line1)):
        if line1[loop] == ",":
            list1.append(word)
            word = ''
            continue
        word += line1[loop]
    return list1

for loop in range(file_len("c1p1.csv")):
    all_list.append(first_line_list(original_file.readline()))


converted_file.write(all_list)
print all_list
print 'this is all'
