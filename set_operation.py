my_string = "aavvccccddddeee"

# converting the string to a set
temp_set = set(my_string)
print(temp_set)

# stitching set into a string using join
new_string = ''.join(temp_set)

print(new_string)
