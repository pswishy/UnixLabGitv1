import sys
num = sys.argv
key = int(num[1])

all_letters = []

blocks = []
seperated = []
for line in sys.stdin:
    phrase = line
    break

for chars in phrase:
    chars = chars.upper()
    if ord(chars) >= 65 and ord(chars) <= 90: #characters that need to be encrypted 
        #print(ord(chars))
        if ord(chars) + key <= 90: # character in valid range
            #print(chr(ord(chars) + key ))
            all_letters.append(chr(ord(chars) + key ))

        else:
            #print(chr(ord(chars) - 26 + key)) # change value
            all_letters.append(chr(ord(chars) + key ))

for letters in all_letters:

    if len(blocks) <= 5:
        blocks.append(letters)
    
    else:
        seperated.append(blocks)
        blocks = []

print(seperated)


