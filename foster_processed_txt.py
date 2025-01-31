import pathlib
import os
import re

# Open the input file in read mode
with open('/Users/lindsayfoster/Projects/datafun-03-analytics/example_data/pg8905.txt', 'r') as file:
    content = file.read()

# Replace 'sun' with 'moon' in a case-insensitive way
content = re.sub(r'sun', 'moon', content, flags=re.IGNORECASE)

# Write the modified content to a new output file
with open('moon.txt', 'w') as file:
    file.write(content)

print("Word replacement complete. 'sun' has been replaced with 'moon' and saved to 'moon.txt'.")
