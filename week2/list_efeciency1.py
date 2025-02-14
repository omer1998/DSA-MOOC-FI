import time


def insertion(n):
    mylist=[]
    for i in range(1,n+1):
        mylist.append(i)
    return mylist

def deletion(list: list):
    
    for i in range(0,len(list)):
        list.pop()
    return list

def main():
    n=10**5
    
    start = time.time()
    list = insertion(n)
    end = time.time()
    print("time: ", end-start, "second")

    start = time.time()
    lis = deletion(list)
    print(lis)
    end = time.time()
    print("time: ", end-start, "second")


main()