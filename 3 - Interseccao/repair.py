import json
from pprint import pprint

# Read in the file contents as text
with open('titles_result.json',encoding="utf-8") as f:
    invalid_json = f.read()

# Replace all ' with "
invalid_json = invalid_json.replace("'",'')
invalid_json = invalid_json.replace("'",'')

valid_json = invalid_json.replace("'", '"')



# Verify that the JSON is valid now and this doesn't raise an exception
json.loads(valid_json,encoding="utf-8")

pprint(valid_json)

# Save the modified text back to the file
with open('title_result_valid.json', 'w',encoding="utf-8") as f:
    f.write(valid_json)