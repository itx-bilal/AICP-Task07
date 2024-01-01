NUM_CHARITIES = 3

def setup_donation_system():
    charities = []
    totals = [0] * NUM_CHARITIES

    for i in range(NUM_CHARITIES):
        charity_name = input(f"Enter the name of Charity {i+1}: ")
        charities.append(charity_name)

    print("\nCharities:")
    for i, charity in enumerate(charities, start=1):
        print(f"{i}. {charity}")

    choice = int(input("\nEnter the number of the chosen charity (1, 2, or 3): "))
    shopping_bill = float(input("Enter the customer's shopping bill: "))

    if 1 <= choice <= NUM_CHARITIES:
        donation = shopping_bill * 0.01
        totals[choice - 1] += donation
        print(f"\nDonation of ${donation} recorded for {charities[choice - 1]}.\n")
    else:
        print("Error: Invalid charity choice. Donation not recorded.\n")
    return charities, totals

def record_and_total_donation(charities, totals):
    while True:
        choice = int(input("Enter the number of the chosen charity (1, 2, or 3), or -1 to show totals: "))

        if choice == -1:
            sorted_totals = sorted(enumerate(totals, start=1), key=lambda x: x[1], reverse=True)
            grand_total = sum(totals)
            print("\nCharities and Totals (in descending order):")
            for index, total in sorted_totals:
                print(f"{charities[index - 1]}: ${total}")

            print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total}\n")
            break
        elif 1 <= choice <= NUM_CHARITIES:
            shopping_bill = float(input("Enter the customer's shopping bill: "))
            donation = shopping_bill * 0.01
            totals[choice - 1] += donation
            print(f"Donation of ${donation} recorded for {charities[choice - 1]}.\n")
        else:
            print("Error: Invalid charity choice. Donation not recorded.\n")

charities, totals = setup_donation_system()

record_and_total_donation(charities, totals)

record_and_total_donation(charities, totals)
