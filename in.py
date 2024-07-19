import json

# Example data (dictionary)
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Opening a file in write mode
with open('data.json', 'w') as f:
    json.dump(data, f)
