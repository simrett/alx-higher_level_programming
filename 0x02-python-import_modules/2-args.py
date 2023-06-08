#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    varg = len(sys.argv)
    print("{} ".format(varg - 1), end='')
    if varg == 1:
        print("arguments.")
    elif varg > 1:
        if varg == 2:
            print("argument:")
        elif varg > 2:
            print("arguments:")
        for i in range(varg - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
