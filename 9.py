# Program 9: Simple Multimodal Application

print("Multimodal AI Application")
print("-------------------------")

print("This program combines text and image information.")

text = input("\nEnter text about the image: ").lower()

print("\nSelect image type:")
print("1. Animal")
print("2. Vehicle")
print("3. Food")
print("4. Nature")

image_choice = int(input("Enter image type: "))

if image_choice == 1:
    image_type = "animal"

elif image_choice == 2:
    image_type = "vehicle"

elif image_choice == 3:
    image_type = "food"

elif image_choice == 4:
    image_type = "nature"

else:
    image_type = "unknown"

print("\n--- Multimodal Analysis ---")

print("Text input:", text)
print("Image type:", image_type)

# Combine text and image information
if image_type == "animal":

    if "dog" in text:
        result = "The image probably contains a dog."

    elif "cat" in text:
        result = "The image probably contains a cat."

    else:
        result = "The image contains an animal."

elif image_type == "vehicle":

    result = "The image contains a vehicle."

elif image_type == "food":

    result = "The image contains food."

elif image_type == "nature":

    result = "The image contains a natural scene."

else:

    result = "Unable to identify the image."

print("\nAI Response:")
print(result)

print("\nMultimodal processing completed.")
