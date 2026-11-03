# Program 10: Simple Image Feature Analyzer

from PIL import Image

print("Simple Image Feature Analyzer")
print("-----------------------------")

path = input("Enter image path: ")

try:

    image = Image.open(path)

    print("\nImage Information")
    print("-----------------")

    print("File:", path)

    width, height = image.size

    print("Width:", width)
    print("Height:", height)

    print("Image mode:", image.mode)

    print("Number of pixels:", width * height)

    # Calculate aspect ratio
    aspect_ratio = width / height

    print("Aspect ratio:", round(aspect_ratio, 2))

    # Convert image to RGB
    image = image.convert("RGB")

    # Get pixel information
    pixels = list(image.getdata())

    print("Total pixels:", len(pixels))

    # Calculate average RGB values
    red = 0
    green = 0
    blue = 0

    for pixel in pixels:

        red += pixel[0]
        green += pixel[1]
        blue += pixel[2]

    red = red / len(pixels)
    green = green / len(pixels)
    blue = blue / len(pixels)

    print("\nAverage RGB Values")
    print("------------------")

    print("Red:", round(red, 2))
    print("Green:", round(green, 2))
    print("Blue:", round(blue, 2))

    print("\nImage analysis completed.")

except FileNotFoundError:

    print("Image file not found.")

except Exception as error:

    print("Error:", error)
