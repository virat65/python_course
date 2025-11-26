# text = input("Enter a sentence: ").strip().split()

# # Last word completely
# last_word = text[-1]

# # First letter of all previous words
# first_letters = [word[0] for word in text[:-1]]

# # Final output
# result = " ".join(first_letters) + " " + last_word

# print(result)




sentence = input("Enter a sentence: ").strip()

words = sentence.split()

output = ""

# Loop through each word
for i in range(len(words)):
    # If it's not the last word → print only first letter
    if i != len(words) - 1:
        output += words[i][0] + " "
    else:
        # If it is the last word → print full word
        output += words[i]

print(output)
