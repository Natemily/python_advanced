timur, ruslan = input(), input()
if (
timur == "камень" and ruslan == "ножницы" 
or timur == "ножницы" and ruslan == "бумага" 
or timur == "бумага" and ruslan == "камень"
):
    print("Тимур")
elif timur == ruslan:
    print("ничья")
else: 
    print("Руслан")