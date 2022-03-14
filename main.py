import sys
num = sys.argv
key = int(num[1])

all_letters = []
answer_string = ""
blocks = []
ten_per_line = []
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

#print(all_letters)
for letters in all_letters:
    if len(blocks) <= 4:
        blocks.append(letters)

    else:
        seperated.append(blocks)
        blocks = []
        blocks.append(letters)
    
    
        
        

print(seperated)
stdout_fileno = sys.stdout

# logic for correct block output
for blocks in seperated:
    blocks = "".join(blocks)
    #ten_per_line.append(blocks)

    #rint(blocks, len(ten_per_line), ten_per_line,answer_string)
    if len(ten_per_line) < 10:
        ten_per_line.append(blocks)
        answer_string += blocks + " "
    else:
        answer_string += "\n" + blocks + " "
        
        ten_per_line = []
        ten_per_line.append(blocks)


print(answer_string)
    
    #stdout_fileno.write(blocks + " ")

