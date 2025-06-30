try:
    purchase_amount = float(input("Enter the purchase amount: $"))


    if purchase_amount > 100:
        discount = 0.10 * purchase_amount
    else:
        discount = 0.05 * purchase_amount
    final_price = purchase_amount - discount
    print(f"Discount: ${discount:.2f}")
    print(f"Final price after discount: ${final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter a numeric value.")