s = "0123456789"
print(s[2:4]) # slice from 2 to 4 (4 not included)
print(s[5:9])
print(s[:6])
print(s[4:])
print(s[:])
print(s[3::2])
print(s[:5:2])
print(s[1::2]) # 13579
print(s[::10])

# check for palindrome
print(s==s[::-1])

