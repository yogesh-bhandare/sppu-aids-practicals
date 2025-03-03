# Operation on the string

str1 = str(input("Enter the string: "))

# Find the word with the longest length
strl = str1.split()
longest_word = ""
max_length = 0

for word in strl:
    length = len(word)
    if length > max_length:
        max_length = length
        longest_word = word

print("a) The word with the longest length is:", longest_word)

# Determine the frequency of a character in the string
char = str(input("b) Enter the character whose frequency is to be determined: "))
char_count = str1.count(char)
print(f"'{char}' occurs {char_count} times in the string.")

# Check if the string is a palindrome or not
str1_clean = ''.join(filter(str.isalnum, str1.lower()))  # Remove non-alphanumeric characters and make lowercase
if str1_clean == str1_clean[::-1]:
    print("c) The string is a palindrome.")
else:
    print("c) The string is not a palindrome.")

# Display the index of the first appearance of a substring
substr = str(input("d) Enter the substring whose index is to be displayed: "))
substr_index = str1.find(substr)
if substr_index != -1:
    print(f"'{substr}' first appears at index {substr_index}.")
else:
    print(f"'{substr}' does not appear in the string.")

# Count the occurrence of each word in the string
word_counts = {}
for word in strl:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("e) Word frequencies in the string:")
for word, count in word_counts.items():
    print(f"'{word}': {count} times")
