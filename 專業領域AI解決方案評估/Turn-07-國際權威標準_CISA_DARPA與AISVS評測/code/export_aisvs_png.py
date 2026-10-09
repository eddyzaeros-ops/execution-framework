import win32com.client

pptx_path = r"d:\JavaDO\執行框架\專業領域AI解決方案評估報告.pptx"
ppt = win32com.client.Dispatch("PowerPoint.Application")
pres = ppt.Presentations.Open(pptx_path, WithWindow=False)

pres.Slides(35).Export(r"C:\Users\calsa\.gemini\antigravity\brain\28a9aa16-b3e0-4c1d-96fd-c10c45994241\scratch\r13\slide35_aisvs.png", "PNG", 1920, 1080)
pres.Slides(36).Export(r"C:\Users\calsa\.gemini\antigravity\brain\28a9aa16-b3e0-4c1d-96fd-c10c45994241\scratch\r13\slide36_aisvs.png", "PNG", 1920, 1080)

pres.Close()
ppt.Quit()
print("Exported slide 35 and 36 successfully")
