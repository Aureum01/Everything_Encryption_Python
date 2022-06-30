import hashlib

#Title 
print("\tString to SHA512 Converter")

#Enter string
print("--------------------------------------------")
question = input("Type here to convert to SHA512: ")
print("\n------------------------------------------")

#Convert string to SHA512
hash = hashlib.sha512( str( input ).encode("utf-8") ).hexdigest()
print(hash)

