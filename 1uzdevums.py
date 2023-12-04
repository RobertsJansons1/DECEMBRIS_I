ievadits_sk = int(input("Ievadi skaitli!: "))
summa = 0

for i in range(1, ievadits_sk + 1):
    summa += i

print(f"Saskaitot katru ciparu starp 1 un {ievadits_sk} ir: {summa}")