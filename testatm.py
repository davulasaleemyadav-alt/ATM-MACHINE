from models import atm

bric = atm.ATM.retrieve(1)

# bric.deposit_cash(1, 19283, 47839, "savings")

# print(bric.check_balance(19283, "savings"))

# print(bric.check_balance(59483, "checking"))

print("Before transfer")
print(bric.check_balance(37566, "savings"))
print(bric.check_balance(39281, "checking"))

bric.transfer_balance(50, 39281, 37566, "checking")

print("After transfer")
print(bric.check_balance(37566, "savings"))
print(bric.check_balance(39281, "checking"))