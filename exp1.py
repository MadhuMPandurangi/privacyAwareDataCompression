import zlib  
import binascii  
  
value =b'WelcometoJavaTpoint'
  
compressed_data = zlib.compress(value)  

print('Original data: ' +  value.decode())  
print('Compressed data: ' + binascii.hexlify(compressed_data).decode())  

