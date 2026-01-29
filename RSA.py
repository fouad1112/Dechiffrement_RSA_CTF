module = int(input("Entre le module N : "), 0)
exposant = int(input("Entre l'exposant e : "), 0)
chiffre = int(input("Entre le message chiffré c : "), 0)

if module % 2 != 0:
    print("Erreur : le module doit être pair")
    exit()

premier = 2
second = module // 2
phi = second - 1

cle_privee = pow(exposant, -1, phi)
message = pow(chiffre, cle_privee, module)

donnees = message.to_bytes((message.bit_length() + 7) // 8, "big")
print(donnees)

try:
    print(donnees.decode())
except:
    pass
