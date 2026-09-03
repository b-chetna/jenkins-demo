import sys
def add(a,b):
    return a+b
if __name__=="__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[1])
    result = add(a,b)
    print("============================")
    print("         Addition           ")
    print("============================")
    print(f"Number 1 : {a}")
    print(f"Number 2 : {b}")
    print(f"Sum : {result}")