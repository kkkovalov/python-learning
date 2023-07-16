list_comp = [x ** 2 for x in range(7) if x % 2 == 0]

for x in list_comp:
    print(x)

print("generators: ")
gen_exp = ( x*2 for x in range(1,6))

for x in gen_exp:
    print(x)