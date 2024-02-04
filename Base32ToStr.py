import base64

word = "ONQWI43TMN4HUYY="
decode = base64.b32decode(word)
print("Base32 Decode:", decode)


