# Converting String to binary 
# Using join() + ord() + format() 
# initializing string  
test_str = input("What string would you like to enter?: ")

print(test_str)

print("-----------------------------------")
  
# using join() + ord() + format() 
# Converting String to binary 
res = ''.join(format(ord(i), 'b') for i in test_str) 
  
# printing result  
print("Binary Result: " + str(res)) 
