timur, ruslan = input(), input()
if (
(timur == "камень" and (ruslan == "ножницы" or ruslan == "ящерица")) 
or (timur == "ножницы" and (ruslan == "бумага" or ruslan == "ящерица")) 
or (timur == "бумага" and (ruslan == "камень" or ruslan == "Спок"))
or (timur == "ящерица" and (ruslan == "Спок" or ruslan == "бумага"))
or (timur == "Спок" and (ruslan == "ножницы" or ruslan == "камень"))
):
    print("Тимур")
elif timur == ruslan:
    print("ничья")
else: 
    print("Руслан")