# Program 5: Simple Text Categorization

categories = {
    "Sports": ["football", "cricket", "match", "player", "goal"],
    "Technology": ["computer", "python", "software", "ai", "internet"],
    "Food": ["pizza", "rice", "burger", "food", "restaurant"]
}

text = input("Enter a sentence: ").lower()

words = text.split()

scores = {}

# Calculate score for every category
for category in categories:

    score = 0

    for word in words:

        if word in categories[category]:
            score += 1

    scores[category] = score

print("\nCategory Scores")
print("---------------")

for category in scores:
    print(category, ":", scores[category])

# Find best category
best_category = "Unknown"
highest_score = 0

for category in scores:

    if scores[category] > highest_score:
        highest_score = scores[category]
        best_category = category

print("\nPredicted Category:", best_category)

if highest_score == 0:
    print("No matching keywords found.")

else:
    print("Matching keywords found:", highest_score)

print("\nText categorization completed.")