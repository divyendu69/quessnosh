class MessApp:
    def __init__(self):
        self.menu = {
            "Monday": ["Spaghetti", "Salad", "Garlic Bread"],
            "Tuesday": ["Chicken Curry", "Rice", "Naan"],
            "Wednesday": ["Grilled Fish", "Steamed Vegetables", "Mashed Potatoes"],
            "Thursday": ["Pasta Primavera", "Caesar Salad", "Breadsticks"],
            "Friday": ["Beef Stir-Fry", "Fried Rice", "Spring Rolls"]
        }
        self.weekly_vote = {}

    def display_menu(self):
        print("------ Weekly Menu ------")
        for day, items in self.menu.items():
            print(f"{day}: {', '.join(items)}")

    def vote_menu(self, day, vote):
        if day in self.menu.keys() and vote in self.menu[day]:
            if day in self.weekly_vote:
                self.weekly_vote[day].append(vote)
            else:
                self.weekly_vote[day] = [vote]
            print("Vote recorded successfully!")
        else:
            print("Invalid day or menu item.")

    def get_feedback(self):
        feedback = input("Please provide your feedback: ")
        # You can implement logic to store feedback in a database or file here
        print("Thank you for your feedback!")

# Example usage:
app = MessApp()

# Display the menu
app.display_menu()

# Vote for a menu item
app.vote_menu("Monday", "Spaghetti")

# Provide feedback
app.get_feedback()
