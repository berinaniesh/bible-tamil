import sys
from PIL import Image, ImageColor, ImageDraw, ImageFont

bg_color = ImageColor.getrgb("#2f8245")
text_color = ImageColor.getrgb("white")
width = 1920
height = 1080

if len(sys.argv) > 1:
    try:
        bg_color = ImageColor.getrgb(sys.argv[1])
        print(f"Background color set to {bg_color}.")
    except:
        print(
            f"The first argument could not be converted into a color for the background and so falling back to the default color {bg_color}."
        )

if len(sys.argv) > 2:
    try:
        text_color = ImageColor.getrgb(sys.argv[2])
        print(f"Text color set to {text_color}")
    except:
        print(
            f"The second argument could not be converted into a color for the text and so falling back to the default color {text_color}"
        )

# Create a new image
image = Image.new(mode="RGBA", size=(width, height))
# Create the draw object
draw = ImageDraw.Draw(image)
draw.rectangle([0, 0, width, height], fill="white")

font = ImageFont.truetype("font.ttf", size=35)
draw.text(xy=(40, 110), text="பின்பு தேவன்; ஜலத்தின் மத்தியில் ஆகாயவிரிவு உண்டாகக்கடவது என்றும், அது ஜலத்தினின்று ஜலத்தைப் பிரிக்கக்கடவது என்றும் சொன்னார்.", fill="black", font=font)
image.save("logo.png")

