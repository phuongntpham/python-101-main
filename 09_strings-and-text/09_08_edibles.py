# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
#print(s.find("apple"))
apple = s[7:(7+len("apple"))]
print(apple)
#print(s.find("egg"))
egg = s[26:26+len("egg")]
print(egg)
#print(s.find("butter"))
butter = s[57:57+len("butter")]
print(butter)
#print(s.find("flour"))
flour = s[68:68+len("flour")]
print(flour)
print("apple pie")