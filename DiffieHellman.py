Ps = int(input("Enter the value of prime number Ps: "))
Gs = int(input("Enter the value of primitive root Gs: "))

g = int(input("Enter the private key g chosen by Alice: "))
p = int(pow(Gs, g, Ps))

h = int(input("Enter the private key h chosen by Bob: "))
q = int(pow(Gs, h, Ps))

K_A = int(pow(q, g, Ps))
K_B = int(pow(p, h, Ps))

print('Alices Secret key is : %d' % K_A)
print('Bobs Secret key is : %d' % K_B)
