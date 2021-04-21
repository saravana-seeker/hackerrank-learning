def min(s):
    s_length=len(s)
    kevin,stuart=0,0
    for i in range(s_length):
        if s[i] in "AEIOU":
            kevin+=(s_length-i)
        else:
            stuart+=(s_length-i)
        
    if kevin > stuart:
        print("Kevin",kevin)
    elif kevin < stuart:
        print("Stuart",stuart)
    else:
        print("Draw")

s=str(input())
min(s)