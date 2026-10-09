import os
from PIL import Image

for fname in ["figure_1_original", "figure_2_original", "figure_6_original"]:
    png_path = f"{fname}.png"
    if not os.path.exists(png_path):
        continue
    img = Image.open(png_path)
    # Convert RGBA or RGB
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # getbbox for non-white/non-transparent
    # background is white or transparent
    # Let's crop based on alpha or bounding box
    # If background is pure white #ffffff:
    bg = Image.new(img.mode, img.size, (255, 255, 255, 255))
    diff = Image.eval(img, lambda a: 255 - a if a > 250 else 0)
    
    # Find bounding box of content
    bbox = img.getbbox()
    print(f"{fname}: original size={img.size}, bbox={bbox}")
    
    # Crop with 20px padding
    # Let's find tight bbox by scanning pixels
    import numpy as np
    arr = np.array(img)
    # content is where it is not pure white (e.g. RGB < 250)
    mask = (arr[:, :, 0] < 250) | (arr[:, :, 1] < 250) | (arr[:, :, 2] < 250)
    coords = np.argwhere(mask)
    if len(coords) > 0:
        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0) + 1
        pad = 25
        x0 = max(0, x0 - pad)
        y0 = max(0, y0 - pad)
        x1 = min(img.width, x1 + pad)
        y1 = min(img.height, y1 + pad)
        cropped = img.crop((x0, y0, x1, y1))
        cropped.save(f"{fname}_cropped.png")
        print(f"Saved cropped {fname}_cropped.png: size={cropped.size}")
    else:
        img.save(f"{fname}_cropped.png")
