from cryptosteganography import CryptoSteganography
import base64

crypto_steganography = CryptoSteganography(base64.b64decode(b'V+QQEMfkRgUXVy8d8aI93UfMI9auulGkco2Zm7Gs2bc+pFS1hgR7+ppKqHgyh3XeLGpUggbuAMU=').decode())

secret = crypto_steganography.retrieve('c1.jpg')

print(secret)
# My secret message