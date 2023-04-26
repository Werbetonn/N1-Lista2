print("Digite 5 números: ")

nums = []
for i in range (5):
    num = int(input())
    nums.append(num)

nnum = int(input("adcione um outro número:"))
nums.append(nnum)
print("Os números informados foram:", nums)