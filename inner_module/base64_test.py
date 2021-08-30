import base64

s = base64.b64encode(b'binary\x00string')
print(s)
s = base64.b64decode('YmluYXJ5AHN0cmluZw==')
print(s)

s = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s)

s = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(s)


