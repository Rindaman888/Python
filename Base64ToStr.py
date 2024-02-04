import base64

def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))
def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

encode = "VGhlIGZsYWcgaXMgY3J5cHRve3RoZV9lbmMwZDMxbmdfMXNfbjB0X1MzY3IzN30="
decode = base64ToString(encode)
print(decode)

