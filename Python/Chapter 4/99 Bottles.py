# Write code below 💖
bottles = 99

while bottles > 0:
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer")
    print("Take one down, pass it around")
    
    bottles -= 1
    
    if bottles > 0:
        print(f"{bottles} bottles of beer on the wall\n")
    else:
        print("No more bottles of beer on the wall!\n")
