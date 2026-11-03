# Program 2: Simple LLM Type Classifier

print("LLM Type Classifier")
print("-------------------")

print("1. GPT-style Generative Model")
print("2. BERT-style Encoder Model")
print("3. T5-style Encoder-Decoder Model")
print()

choice = int(input("Enter the model type number: "))

print("\nModel Information:")

if choice == 1:
    print("Model Type: Generative")
    print("Architecture: Decoder-only")
    print("Main Purpose: Text generation")
    print("Example: GPT")
    print("Input: Text prompt")
    print("Output: Generated text")

elif choice == 2:
    print("Model Type: Encoder")
    print("Architecture: Encoder-only")
    print("Main Purpose: Understanding text")
    print("Example: BERT")
    print("Input: Text")
    print("Output: Representation")

elif choice == 3:
    print("Model Type: Encoder-Decoder")
    print("Architecture: Encoder + Decoder")
    print("Main Purpose: Text transformation")
    print("Example: T5")
    print("Input: Text")
    print("Output: Transformed text")

else:
    print("Invalid choice")

print("\nComparison:")
print("GPT -> Generation")
print("BERT -> Understanding")
print("T5 -> Transformation")

print("\nLLM classification completed.")