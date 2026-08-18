def main():
    # Part 1: Initialize default starting values (Indented 4 spaces inside main)
    serving_cost = 1.00
    labor_rate = 7.50
    shop_rental = 800
    utilities = 150
    advertising = 100
    servings_per_month = 1000
    selling_price = 4.00

    # Part 2: Main menu loop (Indented 4 spaces inside main)
    while True:
        print("\nExpenses: ")
        print(f"1. Cost per serving: {serving_cost}")
        print(f"2. Labor rate per hour: {labor_rate}")
        print(f"3. Shop rental per month: {shop_rental}")
        print(f"4. Utilities per month: {utilities}")
        print(f"5. Advertising budget per month: {advertising}")
        print("\nIncome:")
        print(f"6. Selling price (each): {selling_price}")
        print(f"7. Servings sold per month: {servings_per_month}")
        print("\nAnalysis:")
        print("8. Profit/Loss Calculation")
        # Part 3: Get user input selection (Indented 8 spaces)
        try:
            selection = int(input("\nEnter Selection (0 to Exit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Part 4: Handle menu choices to modify expenses (Indented 8 spaces)
        if selection == 0:
            print("Exiting program.")
            break
        elif selection == 1:
            serving_cost = float(input("Enter cost per serving: "))
        elif selection == 2:
            labor_rate = float(input("Enter labor rate per hour: "))
        elif selection == 3:
            shop_rental = float(input("Enter shop rental per month: "))
        elif selection == 4:
            utilities = float(input("Enter utilities per month: "))
        elif selection == 5:
            advertising = float(input("Enter advertising budget per month: "))
        elif selection == 6:
            selling_price = float(input("Enter selling price (each): "))
        elif selection == 7:
            servings_per_month = float(input("Enter servings sold per month: "))
        elif selection == 8:
            labor_hours = 8 * 6 * 4.33
            total_revenue = servings_per_month * selling_price
            total_expenses = (servings_per_month * serving_cost) + (labor_hours * labor_rate) + shop_rental + utilities + advertising
            profit_loss = total_revenue - total_expenses
            print(f"Profit / Loss: {profit_loss}")
        else:
            print("Invalid selection. Please choose a valid menu option.")

if __name__ == "__main__":
    main()
