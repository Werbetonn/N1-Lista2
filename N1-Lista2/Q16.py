nums = []

for i in range(10):
    num = int(input("Digite um número: "))
    nums.append(num)

dobro = []
for num in nums:
    dobro.append(num * 2)

print("A nova lista é:", dobro)