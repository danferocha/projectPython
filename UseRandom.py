import random


#print("Gerando números aleatórios 1 a 25: ")

#for i in range(1,15):
#   a = random.randint(1,25)
#   print(a)

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print("LISTA DE 0 A 25: ")
print(l)
n = random.shuffle(l)
for i in range (1,25):

s = random.randint (l)
print(" Sequência embaralhada com o uso da função RANDOM.SHUFFLE: ")

print(n)
print(s)


print(random)
