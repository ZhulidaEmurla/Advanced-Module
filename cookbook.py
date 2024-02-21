def cookbook(*args):
    recipes_by_cuisine = {}

    for recipe in args:
        name, cuisine, ingredients = recipe
        if cuisine not in recipes_by_cuisine:
            recipes_by_cuisine[cuisine] = []
        recipes_by_cuisine[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(recipes_by_cuisine.items(), key=lambda x: (-len(x[1]), x[0]))

    output = ""
    for cuisine, recipes in sorted_cuisines:
        output += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for recipe in sorted(recipes):
            name, ingredients = recipe
            output += f"  * {name} -> Ingredients: {', '.join(ingredients)}\n"

    return output if output else None


