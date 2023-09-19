a=input("Enter the first character:")
b=input("Enter the second character:")

if sorted(a.lower())==sorted(b.lower()):
    print("Anagram")
else:
    print("Not an anagram")