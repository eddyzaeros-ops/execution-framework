import win32com.client

pptx_path = r"d:\JavaDO\執行框架\專業領域AI解決方案評估報告.pptx"
ppt = win32com.client.Dispatch("PowerPoint.Application")
pres = ppt.Presentations.Open(pptx_path, WithWindow=False)
print("Initial slide count:", pres.Slides.Count)

custom_layout = pres.SlideMaster.CustomLayouts(7) # 空白版面

# 在倒數第二張（目前 Slide 34 後，即原附錄 Slide 35 前）插入 2 張
# 目前 Slide 34 是科研範式，Slide 35 是附錄
# 我們在 position 35 插入 Slide 35（標準與卡點），在 position 36 插入 Slide 36（評測矩陣），原本的附錄變為 Slide 37
s35 = pres.Slides.AddSlide(35, custom_layout)
s36 = pres.Slides.AddSlide(36, custom_layout)

print("Slide count after adding:", pres.Slides.Count)
pres.Save()
pres.Close()
ppt.Quit()
