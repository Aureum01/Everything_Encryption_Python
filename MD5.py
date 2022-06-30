print("\tMD5 Encryption")

print("\n--------------------------------------------")


import hashlib 

change = input("Input what you would like to encode into MD5, here: ")

result = hashlib.md5(change.encode())

print("Result : ", end ="")
print(result.hexdigest())
