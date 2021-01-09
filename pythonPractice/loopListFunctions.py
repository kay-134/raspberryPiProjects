foods = ["Pizza", "Ice Cream", "Mochi"]

for food in foods:
    if len(food) > 5:
        print("This food has a long name!")

    else:
        print("This food's name has a length of: " + str(len(food)))