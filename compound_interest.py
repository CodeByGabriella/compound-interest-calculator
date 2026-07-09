print("📈 Compound Interest Calculator")
print("-" * 35)

# Ask the user for information
principal = float(input("Enter your starting amount (£): "))
rate = float(input("Enter the annual interest rate (%): "))
years = int(input("How many years will the money be invested? "))

# Convert percentage to decimal
rate = rate / 100

# Calculate compound interest
final_amount = principal * (1 + rate) ** years
interest_earned = final_amount - principal

# Display the results
print("\nResults")
print("-" * 35)
print(f"Starting amount: £{principal:.2f}")
print(f"Final amount: £{final_amount:.2f}")
print(f"Interest earned: £{interest_earned:.2f}")