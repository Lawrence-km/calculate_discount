def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage to be applied
        
    Returns:
        float: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# Get input from user
try:
    original_price = float(input("Enter the original price: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display results
    if discount_percentage >= 20:
        print(f"\nDiscount of {discount_percentage}% applied!")
        print(f"Original price: ${original_price:.2f}")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"\nNo discount applied (discount less than 20%)")
        print(f"Price remains: ${final_price:.2f}")
        
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")
