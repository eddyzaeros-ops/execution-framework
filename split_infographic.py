from PIL import Image

# Source composite image
composite_path = r"d:\JavaDO\執行框架\AI_Agent_Ecosystem_Architecture_4K.png"
fig_path = r"d:\JavaDO\執行框架\fig.png"
doc_path = r"d:\JavaDO\執行框架\doc.png"

img = Image.open(composite_path)
width, height = img.size

# Split coordinate:
# The upper diagram is from y=0 to y=1420 (the divider line is at 1425)
# The lower explanation panel is from y=1425 to y=height
split_y = 1425

# Crop 1: Upper diagram (fig.png)
fig_img = img.crop((0, 0, width, split_y))
fig_img.save(fig_path, "PNG", quality=100)
print(f"Saved fig.png: {fig_img.size} at {fig_path}")

# Crop 2: Lower Chinese explanation panel (doc.png)
doc_img = img.crop((0, split_y, width, height))
doc_img.save(doc_path, "PNG", quality=100)
print(f"Saved doc.png: {doc_img.size} at {doc_path}")
