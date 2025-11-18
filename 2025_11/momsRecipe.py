"""

Recipe: {"butter": 4, "chicken thigh": 8, "garam masala": 1, "cumin powder": 2, "tomatoes": 4}
At home: {"salt": 1, "pepper": 1, "garam masala": 1, "heavy cream": 2, "butter": 2}
Grocery list: {"cumin powder": 2, "tomatoes": 4, "chicken thigh": 8, "butter": 2}

We ran out of chicken thigh, and this recipe calls for 8, so grab 8 of the biggest ones, sweetie.
We don't usually cook with cumin powder, so get 2, honey.
Pick up 4 tomatoes because we don't have any at home, dear.
Pick up 2 butter because we only have 2 at home, and the recipe calls for 4, sweetheart.
You can't substitute butter with heavy cream, sweetie. It'll mess up the flavor profile.
We don't need the salt and pepper at home. Let's set those aside, little one.
Don't include anything you're getting for yourself. That's our little secret.

Explore:

Plan

traverse the recipe
    if the ingredient exists in the ingredients at home:
        save the at grocerylist (recipe - athome)
    else:
        save at grocery list (what the recipe calls for)

"""


def get_grocery_list(recipe_ingredients: dict, ingredients_at_home:dict) -> dict:

    grocerylist = {}

    for ingredient in recipe_ingredients:
        count = recipe_ingredients[ingredient] - ingredients_at_home.get(ingredient, 0)

        if  count > 0:
            grocerylist[ingredient] = count


    return grocerylist

# Test Case 1: No ingredients anywhere
recipe_1 = {}
home_1 = {}
grocery_list_1 = {}
print(get_grocery_list(recipe_1, home_1) == grocery_list_1)

# Test Case 2: No ingredients at home
recipe_2 = {"eggs": 2, "pork loin chops": 8, "panko breadcrumbs": 1, "flour": 1}
home_2 = {}
grocery_list_2 = {"eggs": 2, "pork loin chops": 8, "panko breadcrumbs": 1, "flour": 1}
print(get_grocery_list(recipe_2, home_2) == grocery_list_2)

# Test Case 3: Some ingredients at home
recipe_3 = {"butter": 4, "hickory wood chips": 8, "paprika": 1, "beef brisket": 10, "brown sugar": 2}
home_3 = {"salt": 1, "pepper": 1, "paprika": 1, "butter": 2}
grocery_list_3 = {"beef brisket": 10, "brown sugar": 2, "hickory wood chips": 8, "butter": 2}
print(get_grocery_list(recipe_3, home_3) == grocery_list_3)

# Test Case 4: All ingredients at home
recipe_4 = {"butter": 2, "salmon fillets": 4, "lemon": 1, "oregano": 2, "parsley": 2}
home_4 = {"butter": 2, "salmon fillets": 4, "lemon": 1, "oregano": 2, "parsley": 2}
grocery_list_4 = {}
print(get_grocery_list(recipe_4, home_4)== grocery_list_4)

# Test Case 5: Unneeded ingredients at home
recipe_5 = {"butter": 4, "chicken drumstick": 8, "garlic": 1, "rosemary": 2, "onion": 4}
home_5 = {"salt": 1, "pepper": 1, "garlic": 2, "heavy cream": 2, "butter": 6, "onion": 6}
grocery_list_5 = {"rosemary": 2, "chicken drumstick": 8}
print(get_grocery_list(recipe_5, home_5) == grocery_list_5)

# Test Case 6: Mom's spaghetti
recipe_6 = {"pasta": 1, "tomato sauce": 1, "garlic": 1, "oregano": 10, "meatball": 20, "butter": 8}
home_6 = {"pasta": 100, "tomato": 1, "butter": 5}
grocery_list_6 = {"tomato sauce": 1, "garlic": 1, "oregano": 10, "meatball": 20, "butter": 3}
print(get_grocery_list(recipe_6, home_6) == grocery_list_6)