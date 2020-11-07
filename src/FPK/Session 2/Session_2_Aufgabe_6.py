alter = int(input("Wie alt bist du Kerle?"))
print("Der Junge ist", alter)

if alter < 14:
    print("Du darfst noch nicht Mofa fahren")
elif alter >= 14 and alter < 16:
    print("Du darfst Mofa fahren aber nicht Moped")
elif alter >= 16 and alter < 18:
    print("Du darfst Moped fahren aber kein Auto")
else:
    print("Du darfst endlich Auto fahren")

