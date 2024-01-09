
presents = ["auto", "pc", "panenka", "vysavač", "jídlo", "auto", "vysavač"]
names = ["Petr", "Marie", "Káťa", "Maminka", "Ivan"]


unique_presents = set(presents)
print(unique_presents)

name_to_present = dict(zip(names, presents))

for name, presents in zip(names, presents):
    print(f"{name} dostane {presents}")


user_input = input("Zadej jméno: ")


if user_input in name_to_present:
    selected_present = name_to_present[user_input]
    print(f"{user_input} dostane {selected_present}")
else:
    print(f"Omlouváme se, ale pro '{user_input}' nemáme doporučení na dárek.")

