#Assignment7

#pip install pyqrcode

import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/@shivanandsanglage5417"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
#Scalable Vector Graphics
url.svg("ShivanandDevOpsQR.svg", scale = 8) 