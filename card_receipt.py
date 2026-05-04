# Simple card payment receipt
name = input("Cardholder name: ")
amount = float(input("Amount to charge: "))
card = input("Card number (enter full or last 4 digits): ")

# mask card number leaving last 4 digits
masked = ('*' * max(0, len(card)-4)) + card[-4:]

print("\n--- Payment Receipt ---")
print("Name:", name)
print("Card:", masked)
print(f"Amount: ${amount:.2f}")
print("Status: Approved")
print("------------------------")
