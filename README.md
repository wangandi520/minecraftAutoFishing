# 中文

## 使用方法

我的世界java版1.17.1，语言改成English(US)，双击运行minecraftAutoFishing.py后，拿鱼竿右键抛出，等待即可

## 需要安装2个文件：

pip3 install pytesseract

https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0.20190623.exe

安装第二个文件后，修改这个文件：

"C:\Users\30204\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytesseract\pytesseract.py"

中的tesseract_cmd，改成下面的形式，根据你的exe文件路径

tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# English

## How to use

run minecraft java 1.17.1, change language to English(US), run minecraftAutoFishing.py, in game, right click your fishing rod

## need install

pip3 install pytesseract

https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0.20190623.exe

after install second .exe, modify this file

"C:\Users\30204\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytesseract\pytesseract.py"

tesseract_cmd，according to your install path

tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'