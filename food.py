RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),
]


def by_rating(r: tuple[str, float, int]) -> tuple[float, int]:
    return -r[1], r[2]


def by_time(r: tuple[str, float, int]) -> tuple[int, float]:
    return r[2], -r[1]


def main(sort_by: str) -> str:
    sort_by = sort_by.lower()
    if sort_by == "rating":
        sorted_restaurants = sorted(RESTAURANTS, key=by_rating)
    elif sort_by == "time":
        sorted_restaurants = sorted(RESTAURANTS, key=by_time)
    else:
        print("Unknown option")
        return "Unknown option"

    out = ""
    for i, (name, rating, minutes) in enumerate(sorted_restaurants, start=1):
        line = f"{i}. {name}, {rating} stars, {minutes} min"
        print(line)
        out += line + "\n"
    return out


if __name__ == "__main__":
    sort_by = input("Sort by (rating/time):")
    main(sort_by)
