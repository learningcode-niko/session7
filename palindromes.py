s = "A man, a plan, a canal, Panama!"
s1 = "Yo? Banana Boy!"
s3 = "A nut for a jar of tuna"
s4 = "Racecar"

# step 1: Remove Punctuation
# step 2: remove spaces
# step 3: convert to upper / lower case
# step 4: compare with the reversed order
# step 5: Profit!

punctuation = "!./?-"
for p in punctuation:
    s1 = s1.replace(p,"") # removing punctuation
print(s1)

# now spaces
s1 = s1.replace(" ","")
print(s1)

# now lower space
s1 = s1.lower()
print(s1)

if s1 == s1[::-1]:
    print(f"{s1} = Is a palindrome")
else:
    print(f"{s1} = Is not a palindrome")

if s == s[::-1]:
    print(f"{s} = Is a palindrome")
else:
    print(f"{s} = Is not a palindrome")