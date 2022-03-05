1. Download tesseract install from:
   https://github.com/UB-Mannheim/tesseract/wiki

2. Install or copy the tesseract folder to the folder where the CSI_Image_Rec.py file is
    run pip install pytesseract

3. Run it by passing a full local path to an image to the .py file:
   python c:\CSI_image\CSI_Image_Rec.py F:\archive\pictures\_2015\Image.jpg


4. add to registry for right click menu:
   Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\CSI Image Rec
   Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\*\shell\CSI Image Rec\command -> C:\ffmpeg\bin\imagerec\runitpath.bat "%1"


![alt text](https://raw.githubusercontent.com/n0x5/CSI-Image-Viewer-with-OCR/main/csi.jpg)