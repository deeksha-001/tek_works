#An e-commerce website gives free delivery if the total cart value is more than ₹500. Otherwise, a delivery charge of ₹50 is applied.
#Write a program that takes the cart total as input and prints the final amount payable.

total = int(input("enter price: "))

if(total > 500):
    print("total price: ",total)
else:
    print("total price: ",total + 50)