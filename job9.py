nom = "ballon"
prix = "19.99"
quantité = int("12")
print(f"====Inventaire====")
print(f"Produit : {nom}")
print(f"Prix du {nom} : {prix}")
print(f"Stock dispo: {quantité}")
nombre = int(input("Combien souhaitez-vous en acheter ? "))
if nombre > quantité:
    print("stock insuffisant")
else:
     quantité=quantité-nombre
     print(f"Stock restant:{quantité}")



prix_initial = 19.99
augmentation = 10

prix_final = prix_initial * (1 + augmentation / 100)
print(f"Nouveaux prix après augmentation de {augmentation}% : {prix_final:.2f} €")
