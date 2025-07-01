item_prices = [8.0, 4.0, 6.5]
quantities = [3, 5, 2]
discount_rate = 12  
tax_rate = 7        

total = sum(p * q for p, q in zip(item_prices, quantities))

discounted_total = total - (total * discount_rate / 100)

final_total = discounted_total + (discounted_total * tax_rate / 100)

print(f"Final Total: ${final_total:.2f}")
