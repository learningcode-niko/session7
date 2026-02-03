print(dir(""))
print(help("bob".capitalize))
print("bob".capitalize())
s = "Hello World"
print(s.upper())
print(s.lower())
print(help("bob".center))
print(s.center(30))
print(s.center(30,"*"))
# fake christmas tree
for i in range(10):
    s= ("*"*(2*i+1))
    print(s.center(50))
for i in range(3): # stump?
        print("***".center(50))

# find, finds the position of substring
s = "i see a cat. the cat is black. cats are nice"
print(s.find("cat"))
print(s.find("dog")) #-1 when it cannot find
pos=0
while True:
    pos = s.find("cat", pos)
    if pos == -1: # we can't find it
        break
    print(f"cat on position {pos}")
    pos += 1

print(s.count("cat"))
print(s.replace("cat","dog"))
print(s.split())



