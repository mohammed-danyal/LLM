# Program 3: Dataset Text Preprocessing

dataset = [
    "Hello World!",
    "Python is easy to learn.",
    "Machine Learning is interesting.",
    "LLMs can generate text.",
    "Python is used in AI."
]

print("Original Dataset")
print("----------------")

for sentence in dataset:
    print(sentence)

cleaned_dataset = []

print("\nPreprocessed Dataset")
print("--------------------")

for sentence in dataset:

    # Convert to lowercase
    sentence = sentence.lower()

    # Remove punctuation
    punctuation = ".,!?;:"
    for symbol in punctuation:
        sentence = sentence.replace(symbol, "")

    # Remove extra spaces
    sentence = " ".join(sentence.split())

    cleaned_dataset.append(sentence)

for sentence in cleaned_dataset:
    print(sentence)

# Tokenize dataset
print("\nTokens")
print("------")

all_tokens = []

for sentence in cleaned_dataset:
    tokens = sentence.split()

    for token in tokens:
        all_tokens.append(token)

print(all_tokens)

print("\nTotal sentences:", len(cleaned_dataset))
print("Total tokens:", len(all_tokens))
print("Unique tokens:", len(set(all_tokens)))

print("\nDataset preprocessing completed.")