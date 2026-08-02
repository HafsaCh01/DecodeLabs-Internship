"""
AI Recommendation Logic - Clothing Recommendation System
Takes user preferences and recommends items using similarity matching.
"""


CATALOG = [
    {"id": 1, "name": "Denim Jacket", "category": "outerwear", "style": "casual", "color": "blue", "price": 45},
    {"id": 2, "name": "Formal Blazer", "category": "outerwear", "style": "formal", "color": "black", "price": 80},
    {"id": 3, "name": "Graphic Tee", "category": "top", "style": "casual", "color": "white", "price": 20},
    {"id": 4, "name": "Silk Shirt", "category": "top", "style": "formal", "color": "white", "price": 55},
    {"id": 5, "name": "Ripped Jeans", "category": "bottom", "style": "casual", "color": "blue", "price": 40},
    {"id": 6, "name": "Formal Trousers", "category": "bottom", "style": "formal", "color": "black", "price": 50},
    {"id": 7, "name": "Hoodie", "category": "top", "style": "casual", "color": "grey", "price": 35},
    {"id": 8, "name": "Evening Gown", "category": "outerwear", "style": "formal", "color": "red", "price": 120},
    {"id": 9, "name": "Sneakers", "category": "footwear", "style": "casual", "color": "white", "price": 60},
    {"id": 10, "name": "Oxford Shoes", "category": "footwear", "style": "formal", "color": "black", "price": 90},
]


def get_user_preferences():
    """Take user input for preferences."""
    print("Tell us your preferences:\n")

    style = input("Preferred style (casual/formal): ").strip().lower()
    color = input("Preferred color (or press Enter to skip): ").strip().lower()
    category = input("Category interested in (top/bottom/outerwear/footwear, or Enter to skip): ").strip().lower()

    max_price_input = input("Max budget (or press Enter to skip): ").strip()
    max_price = float(max_price_input) if max_price_input else None

    return {
        "style": style,
        "color": color,
        "category": category,
        "max_price": max_price,
    }


def similarity_score(item, prefs):
    """
    Score an item based on how well it matches user preferences.
    Each matching attribute adds weighted points.
    """
    score = 0

    if prefs["style"] and item["style"] == prefs["style"]:
        score += 3

    if prefs["color"] and item["color"] == prefs["color"]:
        score += 2

    if prefs["category"] and item["category"] == prefs["category"]:
        score += 2

    if prefs["max_price"] is not None:
        if item["price"] <= prefs["max_price"]:
            score += 1
        else:
            score -= 2  

    return score


def recommend_items(catalog, prefs, top_n=5):
    """Match preferences using scoring logic and return top N ranked items."""
    scored_items = []

    for item in catalog:
        score = similarity_score(item, prefs)
        if score > 0:
            scored_items.append((score, item))

    scored_items.sort(key=lambda x: (-x[0], x[1]["price"]))

    return scored_items[:top_n]


def display_recommendations(results):
    """Display the recommended items nicely."""
    if not results:
        print("\nNo matching recommendations found. Try broadening your preferences.")
        return

    print("\n" + "=" * 45)
    print("       YOUR RECOMMENDED ITEMS")
    print("=" * 45)

    for rank, (score, item) in enumerate(results, start=1):
        print(f"\n{rank}. {item['name']}")
        print(f"   Category : {item['category']}")
        print(f"   Style    : {item['style']}")
        print(f"   Color    : {item['color']}")
        print(f"   Price    : ${item['price']}")
        print(f"   Match Score : {score}")

    print("\n" + "=" * 45)


def main():
    print("=" * 45)
    print("   AI RECOMMENDATION SYSTEM - CLOTHING")
    print("=" * 45 + "\n")

    while True:
        prefs = get_user_preferences()
        results = recommend_items(CATALOG, prefs)
        display_recommendations(results)

        again = input("\nSearch again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for using the recommendation system!")
            break
        print()


if __name__ == "__main__":
    main()