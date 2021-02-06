fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)

# apple
# banana
# cherry

string = "banana"
for char in string:
    print(char)
# b
# a
# n
# a
# n
# a

fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    if fruits == "banana":
        break
    print(fruits)
# apple


fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    if fruits == "banana":
        continue
    print(fruits)
# apple
# cherry


fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)
else:
    print("Finally Finished!")

# apple
# banana
# cherry
# Finally Finished!


adjectives = ["small", "big"]
fruits = ["apple", "banana", "cherry"]
for adjectives in adjectives:
    for fruit in fruits:
        print(adjectives, fruit)
# small apple
# small banana
# small cherry
# big apple
# big banana
# big cherry




