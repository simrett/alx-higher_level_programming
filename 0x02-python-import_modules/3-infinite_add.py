#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    narg = 0
    for i in range(1, len(sys.agrv)):
        narg += int(sys.argv[i])
    print("{}".format(narg))
