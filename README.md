<p align="center">

<img width="724" height="414" alt="RSA" src="https://github.com/user-attachments/assets/4a7f33dc-4da9-40bf-baf1-4e73a865296a" />


</p>

# 🔐 Déchiffrement RSA CTF

Script Python **simple et pédagogique** pour déchiffrer un RSA **volontairement faible**, typique des challenges **CTF**.

Ce programme permet de retrouver le message clair à partir de :
- **N** : module RSA  
- **e** : exposant public  
- **c** : message chiffré  

⚠️ Fonctionne uniquement lorsque le **module RSA est pair** (`p = 2`).

---

## 🧠 Principe

Quand le module RSA est pair :
- `p = 2`
- `q = N / 2`
- `φ(N) = q - 1`

Il est alors possible de calculer la clé privée et de déchiffrer le message.

Ce script automatise ces étapes sans dépendance externe.

---

## 🚀 Utilisation

```bash
python3 RSA.py
