#python2
if __name__ == '__main__':
    N = int(input())
    l=[]

    for i in range(0,N):
        word=raw_input().split()
        if word[0] == "insert":
            l.insert(int(word[1]),int(word[2]))
        elif word[0] == "print":
            print(l)
        elif word[0] == "remove":
            l.remove(int(word[1]))
        elif word[0] =="append":
            l.append(int(word[1]))
        elif word[0] =="sort":
            l.sort()
        elif word[0] =="pop":
            l.pop()
        elif word[0] =="reverse":
            l.reverse()