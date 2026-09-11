from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(r"c:\Users\USER\Desktop\Vibecoding for money\imagi")
asset_dir = root / "Asset"
asset_dir.mkdir(exist_ok=True)

# Create a hero-style OG image that matches the page aesthetic.
img = Image.new("RGB", (1200, 630), "#F8F6EE")
draw = ImageDraw.Draw(img)

# subtle paper texture
for y in range(0, 630, 6):
    for x in range(0, 1200, 6):
        if (x + y) % 18 == 0:
            draw.rectangle((x, y, x + 1, y + 1), fill=(80, 80, 80, 20))

# main frame
frame = (42, 42, 1158, 588)
draw.rounded_rectangle(frame, radius=24, outline=(76, 76, 76), width=3, fill=(248, 246, 238))

# fonts
serif = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 84)
serif_small = ImageFont.truetype(r"C:\Windows\Fonts\georgia.ttf", 42)
sans = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 28)
mono = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 20)

# eyebrow
badge = (90, 82, 420, 118)
draw.rounded_rectangle(badge, radius=8, fill=(70, 0, 255))
draw.text((106, 88), "A STORY IN SEVEN BOOKS", font=mono, fill=(255, 255, 255))

# title lines
headline1 = "Why I'd love to build"
headline2 = "at imagi."

draw.text((82, 140), headline1, font=serif, fill=(41, 41, 41))
draw.text((82, 230), headline2, font=serif, fill=(70, 0, 255))

# subtitle
sub = "About a computer, a teacher, an AI, and why I ended up here."
draw.text((82, 320), sub, font=sans, fill=(41, 41, 41))

# bottom shelf area
shelf_y = 440
book_positions = [90, 200, 310, 420, 530, 640, 750]
book_colors = ["#4600FF", "#FF00FF", "#FAF578", "#2B6BFF", "#3DD68C", "#292929", "#4600FF"]

# create book shapes
for idx, (x, color) in enumerate(zip(book_positions, book_colors)):
    book_h = 150 + (idx % 3) * 18
    draw.rounded_rectangle((x, shelf_y - book_h, x + 76, shelf_y), radius=6, fill=color)
    draw.text((x + 24, shelf_y - book_h + 18), f"{idx + 1:02d}", font=mono, fill=(255, 255, 255))

draw.rectangle((90, shelf_y, 1110, shelf_y + 18), fill=(41, 41, 41))

# footer name
name = "PRAISE AKINDE — PRODUCT DESIGNER"
draw.text((90, 502), name, font=mono, fill=(90, 90, 90))

# CTA button
button = (1060, 488, 1138, 566)
draw.rounded_rectangle(button, radius=12, outline=(41, 41, 41), width=3, fill=(248, 246, 238))
draw.text((1086, 512), "▾", font=serif_small, fill=(41, 41, 41))

# save image
out_path = asset_dir / "og-image.png"
img.save(out_path)
print(f"Created {out_path}")
