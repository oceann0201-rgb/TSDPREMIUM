from PIL import Image
import os

poster_path = "assets/tds-poster.jpg"
img = Image.open(poster_path)
width, height = img.size
print(f"Original poster dimensions: {width} x {height}")

# 1. Product 1 (Left card - Angle 45):
# Looking at the 576x1024 poster:
# The image frame for left card is located around x: 25 to 286, y: 522 to 723
p1_box = (25, 522, 286, 723)
p1 = img.crop(p1_box)
p1.save("assets/product-1.jpg", "JPEG", quality=95)
print("Saved assets/product-1.jpg:", p1.size)

# 2. Product 2 (Right card - Front/Top view):
# The image frame for right card is located around x: 295 to 552, y: 522 to 723
p2_box = (295, 522, 552, 723)
p2 = img.crop(p2_box)
p2.save("assets/product-2.jpg", "JPEG", quality=95)
print("Saved assets/product-2.jpg:", p2.size)

# 3. Hero Shoes (Top presentation):
# x: 0 to 576, y: 0 to 388
hero_box = (0, 0, 576, 388)
hero = img.crop(hero_box)
hero.save("assets/hero-banner.jpg", "JPEG", quality=95)
print("Saved assets/hero-banner.jpg:", hero.size)

# 4. Hero Shoes Only (The pair of slippers on the marble pedestal):
# x: 240 to 570, y: 110 to 380
shoes_box = (240, 110, 570, 380)
shoes = img.crop(shoes_box)
shoes.save("assets/hero-shoes-closeup.jpg", "JPEG", quality=95)
print("Saved assets/hero-shoes-closeup.jpg:", shoes.size)

# 5. Footer Banner (Bottom banner):
# x: 25 to 552, y: 875 to 995
banner_box = (25, 875, 552, 995)
banner = img.crop(banner_box)
banner.save("assets/footer-banner.jpg", "JPEG", quality=95)
print("Saved assets/footer-banner.jpg:", banner.size)

# Also copy to mini-shop-next
dest_dir = "../mini-shop-next/public/assets/images/banner"
os.makedirs(dest_dir, exist_ok=True)
p1.save(os.path.join(dest_dir, "product-1.jpg"), "JPEG", quality=95)
p2.save(os.path.join(dest_dir, "product-2.jpg"), "JPEG", quality=95)
hero.save(os.path.join(dest_dir, "hero-banner.jpg"), "JPEG", quality=95)
shoes.save(os.path.join(dest_dir, "hero-shoes-closeup.jpg"), "JPEG", quality=95)
banner.save(os.path.join(dest_dir, "footer-banner.jpg"), "JPEG", quality=95)
print("Copied all assets to Next.js project as well.")
