# Program 7: Simple Prompt Engineering

print("Prompt Engineering Demonstration")
print("--------------------------------")

topic = input("Enter a topic: ")

print("\nChoose prompt type:")
print("1. Simple prompt")
print("2. Detailed prompt")
print("3. Expert prompt")

choice = int(input("Enter your choice: "))

if choice == 1:

    prompt = "Explain " + topic

    response = (
        "The topic " + topic +
        " is an important concept. "
        "It can be studied to understand its basic ideas."
    )

elif choice == 2:

    prompt = (
        "Explain " + topic +
        " in simple words with examples."
    )

    response = (
        topic +
        " can be understood by studying its definition, "
        "main concepts and practical examples."
    )

elif choice == 3:

    prompt = (
        "Act as an expert and explain " +
        topic +
        " with technical details."
    )

    response = (
        "As an expert, we can study " +
        topic +
        " by examining its architecture, "
        "working principles, applications and limitations."
    )

else:

    prompt = "Invalid prompt"
    response = "Invalid choice."

print("\nGenerated Prompt:")
print(prompt)

print("\nGenerated Response:")
print(response)

print("\nPrompt Engineering Concepts:")
print("1. Give clear instructions.")
print("2. Specify the required output.")
print("3. Provide context.")
print("4. Mention the target audience.")
print("5. Ask for examples.")

print("\nPrompt engineering completed.")