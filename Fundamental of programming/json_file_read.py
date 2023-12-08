import json

# Open the JSON file
file = open("books.json")
# Load the file into a list of dictionaries
books = json.load(file)
file.close()

print(type(books)) # this is just a list of ...
print(type(books[0])) # dictionaries
print("---")

for key in books[0]: # book[0] is the first dictionary in the list
    print(key)
print("---")

for book in books:
    print("Author:", book["author"])
    print("Name:", book["title"])
    print("Genre:", book["genre"])
    print("Rating:", book["rating"])
    print()

