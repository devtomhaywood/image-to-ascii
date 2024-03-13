from PIL import Image


path = "media/github.jpg"

# Ascii character brightness intensity
ascii = ["@", "%", "#", "*", "+", "=", "-", ":", "."]


# Resize image and keep aspect ratio
im = Image.open(path)
im.thumbnail((100,100), Image.LANCZOS)
im = im.convert("L")
im.save("new_target", "JPEG")
width, height = im.size

pixels = im.getdata()

characters = ""
for pixel in pixels:
	# 255//29 = 9. There are 9 levels of darkness in our ascii char list.
	# This quickly finds which one is most appropriate.
	val = int(pixel//29)
	characters += "".join(ascii[val])


chars_range = 0
for i in range(height):
	print(characters[chars_range:chars_range+width])
	chars_range += width



