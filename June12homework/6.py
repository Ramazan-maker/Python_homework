class Recipe:
    def __init__(self, name, ingredients, preparation_time, cuisine, difficulty_level, is_vegetarian):
        self.name = name
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cuisine = cuisine
        self.difficulty_level = difficulty_level
        self.is_vegetarian = is_vegetarian

    def cook(self):
        print(f"Recipe for {self.name} is being cooked.")

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Added {ingredient} to the recipe.")

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
        print(f"Removed {ingredient} from the recipe.")

    def check_difficulty(self):
        if self.difficulty_level == "Easy":
            print("This recipe is easy to make.")
        elif self.difficulty_level == "Medium":
            print("This recipe has a medium difficulty level.")
        else:
            print("This recipe is difficult to make.")


recipe1 = Recipe("Spaghetti Bolognese", ["Pasta", "Tomato Sauce", "Ground Beef", "Onion"], 30, "Italian", "Medium", False)
recipe2 = Recipe("Vegetable Stir-Fry", ["Broccoli", "Carrots", "Bell Peppers", "Soy Sauce"], 20, "Asian", "Easy", True)

recipe1.cook()
recipe1.add_ingredient("Garlic")
recipe2.remove_ingredient("Carrots")
recipe2.check_difficulty()