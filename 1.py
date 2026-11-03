# Program 1: Simple NLP Text Analyzer

text = input("Enter a paragraph: ")

# Convert text to lowercase
text = text.lower()

# Remove common punctuation
punctuation = ".,!?;:'\""
for symbol in punctuation:
    text = text.replace(symbol, "")

# Split text into words
words = text.split()

print("\n--- NLP TEXT ANALYZER ---")

# Display number of words
print("Total words:", len(words))

# Find unique words
unique_words = set(words)
print("Unique words:", len(unique_words))

# Display all words
print("\nWords:")
for word in words:
    print(word)

# Count word frequency
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word in frequency:
    print(word, ":", frequency[word])

# Find most frequent word
most_common = ""
highest_count = 0

for word in frequency:
    if frequency[word] > highest_count:
        highest_count = frequency[word]
        most_common = word

print("\nMost frequent word:", most_common)
print("Frequency:", highest_count)

# Count sentences
sentences = text.count(".") + text.count("!") + text.count("?")

print("Number of sentences:", sentences)

print("\nNLP analysis completed.")