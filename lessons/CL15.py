my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for elem in my_list:
    new_list.append(elem)
# print(new_list)

pets: list[str] = ["Louie", "Bo", "Bear"]
for x in pets:
    if x[0] == "B":
        print(f"Good boy, {x}!")

idx: int = 0
while idx < len(pets):
    if pets[idx][0] == "B":
        print(f"Good boy, {pets[idx]}!")
    idx += 1

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
