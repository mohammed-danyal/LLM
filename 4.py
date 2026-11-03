# Program 4: Simple Next Word Prediction

sentences = [
    "python is easy",
    "python is powerful",
    "python is popular",
    "machine learning is powerful",
    "machine learning is interesting",
    "deep learning is interesting"
]

# Create dictionary
model = {}

print("Training simple language model...")

for sentence in sentences:
    words = sentence.split()

    for i in range(len(words) - 1):

        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in model:
            model[current_word] = []

        model[current_word].append(next_word)

print("Training completed.")

print("\nLearned Model:")
for word in model:
    print(word, "->", model[word])

word = input("\nEnter a word: ")

if word in model:

    predictions = model[word]

    print("\nPossible next words:")

    for prediction in predictions:
        print(prediction)

    # Count occurrences
    counts = {}

    for prediction in predictions:
        counts[prediction] = counts.get(prediction, 0) + 1

    best_word = max(counts, key=counts.get)

    print("\nPredicted next word:", best_word)

else:
    print("Word not found in training data.")

print("\nPrediction completed.")