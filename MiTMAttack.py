from random import randint

Ps = int(input("Enter the value of prime number P: "))
Gs = int(input("Enter the value of primitive root Gs: "))

g = int(input("Enter the private key g chosen by Alice: "))

m = randint(1, Ps - 1)
print('Attacker\'s Private Key m is: %d' % m)

p = int(pow(Gs, g, Ps))
a = int(pow(Gs, m, Ps))
h = int(input("Enter the private key h chosen by Bob: "))

b = int(pow(Gs, m, Ps))
K_A_attacker = int(pow(b, g, Ps))
K_B_attacker = int(pow(a, h, Ps))

print('Attacker\'s Secret key for Alice is : %d' % K_A_attacker)
print('Attacker\'s Secret key for Bob is : %d' % K_B_attacker)
