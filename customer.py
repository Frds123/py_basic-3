purchase_amount = float(input("Enter the purchase amount in taka: "))
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ")

discount = 0
free_item = ""

if purchase_amount >= 1000 and age < 50:
    if gender.lower() == "male":
        free_item = "cake"
    elif gender.lower() == "female":
        free_item = "chocolate"

    payment_method = input("Enter payment method (cash/card): ")
    if payment_method.lower() == "cash":
        discount = 0.1
    elif payment_method.lower() == "card":
        discount = 0.2

payable_amount = purchase_amount - (purchase_amount * discount)

print("Free Item: ", free_item)
print("Payable Amount: ", payable_amount)
