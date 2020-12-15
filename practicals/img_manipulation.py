from PIL import Image

img = Image.open(r"C:\Users\user\Pictures\FAKE\image.jpg") # Open an image
img = img.crop((256, 256, 512, 512)) # Crop a part from the image
img = img.convert("L") # Convert to black and white
img.show() # Show image
