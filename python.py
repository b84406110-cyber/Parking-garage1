print("=== Parking Garage Calculator ===")

print("Enter day type: weekday, weekend, holiday")
print("Type 'done' when finished entering hours.")

total = 0.0

while True:
    day_type = input("\nEnter day type for 1 hour: ").strip().lower()

    if day_type == "done":
        break

    if day_type == "weekday":
        price = 8.00
    elif day_type == "weekend":
        price = 6.00
    elif day_type == "holiday":
        price = 5.00
    else:
        print("Invalid day type! Try again.")
        continue

    total += price

    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")


print("\n=== Parking Summary ===")

print(f"Subtotal: ${total:.2f}")

discount = 0.0

if total >= 50.00:
    discount = 7.00

print(f"Frequent Parker Discount: -${discount:.2f}")

final_total = total - discount

print(f"Final Total: ${final_total:.2f}")

print("Thank you for parking with us!")
