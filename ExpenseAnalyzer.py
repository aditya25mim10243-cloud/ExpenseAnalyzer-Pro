import csv

import matplotlib.pyplot as plt

from datetime import datetime



class ExpenseTracker:

    def __init__(self, filename='expenses.csv'):

        self.filename = filename

        self.categories = ["Food", "Transport", "Subscription", "Shopping", "Others"]

        # Ensure file exists with headers

        try:

            with open(self.filename, 'x', newline='') as f:

                writer = csv.writer(f)

                writer.writerow(["Date", "Category", "Amount", "Description"])

        except FileExistsError:

            pass



    def add_expense(self, category, amount, description):

        date = datetime.now().strftime("%Y-%m-%d")

        with open(self.filename, 'a', newline='') as f:

            writer = csv.writer(f)

            writer.writerow([date, category, amount, description])

        print(f"✅ Success: Added ₹{amount} for {description}")



    def generate_report(self):

        data = {}

        try:

            with open(self.filename, 'r') as f:

                reader = csv.DictReader(f)

                for row in reader:

                    cat = row['Category']

                    amt = float(row['Amount'])

                    data[cat] = data.get(cat, 0) + amt

            

            if not data:

                print("No data found to plot!")

                return



            # Plotting

            plt.figure(figsize=(8, 6))

            plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=140)

            plt.title("Monthly Expense Breakdown")

            plt.tight_layout()

            plt.savefig('expense_chart.png') # Saves the chart for your report

            plt.show()

            print("📈 Chart generated and saved as 'expense_chart.png'")



        except FileNotFoundError:

            print("Please add some expenses first!")



def main():

    tracker = ExpenseTracker()

    while True:

        print("\n--- Expense Tracker Menu ---")

        print("1. Add Expense")

        print("2. Generate Visual Report")

        print("3. Exit")

        choice = input("Select an option (1-3): ")



        if choice == '1':

            print("\nCategories:", ", ".join(tracker.categories))

            cat = input("Enter Category: ").capitalize()

            amt = float(input("Enter Amount: "))

            desc = input("Enter Description: ")

            tracker.add_expense(cat, amt, desc)

        elif choice == '2':

            tracker.generate_report()

        elif choice == '3':

            break

        else:

            print("Invalid choice, try again.")



if __name__ == "__main__":

    main()
