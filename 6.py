# Program 6: Simple Semantic Search

documents = [
    "Python is a programming language",
    "Machine learning uses data",
    "Football is a popular sport",
    "Artificial intelligence uses machine learning",
    "Python is useful for artificial intelligence"
]

query = input("Enter your search query: ").lower()

query_words = set(query.split())

print("\nSearch Results")
print("--------------")

results = []

for document in documents:

    words = set(document.lower().split())

    # Find common words
    common_words = query_words.intersection(words)

    score = len(common_words)

    results.append((score, document))

# Sort results
results.sort(reverse=True)

for score, document in results:

    print("\nDocument:", document)
    print("Similarity score:", score)

print("\nBest matching document:")

best_score = results[0][0]
best_document = results[0][1]

if best_score > 0:
    print(best_document)
    print("Score:", best_score)

else:
    print("No matching document found.")

print("\nSemantic search completed.")