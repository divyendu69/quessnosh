import streamlit as st

class QuessNoshApp:
    def __init__(self):
        self.menu = {
            "Monday": ["Rajma Chawal", "Mixed Vegetable Sabzi", "Roti"],
            "Tuesday": ["Paneer Butter Masala", "Jeera Rice", "Naan"],
            "Wednesday": ["Aloo Gobi", "Dal Tadka", "Rice"],
            "Thursday": ["Chole Bhature", "Green Salad", "Pickle"],
            "Friday": ["Vegetable Biryani", "Raita", "Papad"]
        }
        self.weekly_vote = {}

    def display_menu(self):
        st.write("------ Weekly Menu ------")
        for day, items in self.menu.items():
            st.write(f"{day}: {', '.join(items)}")

    def vote_menu(self, day, vote):
        if day in self.menu.keys() and vote in self.menu[day]:
            if day in self.weekly_vote:
                self.weekly_vote[day].append(vote)
            else:
                self.weekly_vote[day] = [vote]
            st.write("Vote recorded successfully!")
        else:
            st.write("Invalid day or menu item.")

    def get_feedback(self):
        feedback = st.text_area("Please provide your feedback:")
        if st.button("Submit Feedback"):
            # You can implement logic to store feedback in a database or file here
            st.write("Thank you for your feedback!")

def main():
    st.title("QuessNosh: College Mess App")
    app = QuessNoshApp()

    st.sidebar.title("Menu Options")
    menu_option = st.sidebar.selectbox("Select an Option", ["Display Menu", "Vote for Menu", "Provide Feedback"])

    if menu_option == "Display Menu":
        app.display_menu()
    elif menu_option == "Vote for Menu":
        day = st.selectbox("Select a day", list(app.menu.keys()))
        vote = st.selectbox("Vote for a menu item", app.menu[day])
        if st.button("Vote"):
            app.vote_menu(day, vote)
    elif menu_option == "Provide Feedback":
        app.get_feedback()

if __name__ == "__main__":
    main()
