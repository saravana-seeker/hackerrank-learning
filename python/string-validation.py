#isalum()
#isalpha
#isdigit
#islower
#isupper()

string=str(input())
print(any(c.isalnum() for c in string))
print(any(c.isalpha() for c in string))
print(any(c.isdigit() for c in string))
print(any(c.islower() for c in string))
print(any(c.isupper() for c in string))


        