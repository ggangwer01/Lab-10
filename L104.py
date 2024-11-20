#the authors are Gwyneth and Victoria

red_velvet_ingredients = {"flour": "2 cups", "cocoa powder": "1 tbsp", "baking soda": "1 tsp","salt": "1/2 tsp", "sugar": "2 cups", "butter": "1 cup","eggs": "2","buttermilk": "1 cup","red food coloring": "2 tbsp","vanilla extract": "1 tsp","vinegar": "1 tsp"}
lemon_cake_ingredients= {"flour": "2 cups", "baking powder": "1 1/2 tsp", "salt": "1/2 tsp","sugar": "1 1/2 cups","butter": "1/2 cup", "eggs": "3","buttermilk": "1/2 cup","lemon juice": "2 tbsp","vanilla extract": "1 tsp"}

similar_ingredients=[]
for ingredient in red_velvet_ingredients:
    if ingredient in lemon_cake_ingredients:
        similar_ingredients.append(ingredient)
print(similar_ingredients)
