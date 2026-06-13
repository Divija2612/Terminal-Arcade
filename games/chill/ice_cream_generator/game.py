import random

AUTHOR = "Divija2612"

def run():
    print(f"🍦 Welcome to Ice Cream Machine by {AUTHOR}!")

    ingredients = [
        "Chocolate",
        "Vanilla",
        "Banana",
        "Cookie",
        "Strawberry",
        "Caramel",
        "Mint",
        "Mango"
    ]

    flavor1, flavor2 = random.sample(ingredients, 2)

    print("\nYour generated ice cream flavor:")
    print(f"{flavor1} + {flavor2}")