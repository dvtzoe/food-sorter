from food import main


def test_main():
    assert (
        main("rating")
        == """1. Boat Noodles, 4.8 stars, 30 min
2. Pad Thai House, 4.8 stars, 40 min
3. Chicken Rice, 4.6 stars, 15 min
4. Som Tam Corner, 4.6 stars, 25 min
5. Mango Rice, 4.2 stars, 25 min
"""
    )
    assert (
        main("time")
        == """1. Chicken Rice, 4.6 stars, 15 min
2. Som Tam Corner, 4.6 stars, 25 min
3. Mango Rice, 4.2 stars, 25 min
4. Boat Noodles, 4.8 stars, 30 min
5. Pad Thai House, 4.8 stars, 40 min
"""
    )
    assert main("TIME") == main("time")
    assert main("PRICE") == "Unknown option"
    assert main("") == "Unknown option"
