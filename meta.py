import sys

def meta():

    loop = 0
    string = sys.argv[1]   
    for c in string:
        print(c + " ", end="")
    print('\n')
    for x in string:
        if (loop <= 0) == False:
            print(x + '\n')
        else:
            pass
        loop += 1
        
meta()

"""
Terminal: python3.5 %path_to_file% META
Output:
M E T A 

E

T

A


"""
