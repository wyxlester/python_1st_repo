name = input("Hello, what is your name? ")
print(f"Hello, {name}")

my_data = {
    "birthday": "12 Jul 1991",
    "country": "Singapore",
    "passion": "Poker, Startup, Technology"
}

# Iterate through the dictionary and break after the first iteration
for key, value in my_data.items():
    print(f"{key}: {value}")
