# Assignment 6.5

# str = 'X-DSPAM-Confidence: 0.8475'
# ipos = str.find(':')
# piece = str[ipos+2:]
# value = float(piece)
# print(value)

numbers = []

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        x = float(sval)
    except:
        print("Invalid input")
        continue
    numbers.append(x)

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers were entered")






