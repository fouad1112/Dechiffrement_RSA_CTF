<p align="center">
  <img src="https://github.com/fouad1112/Dechiffrement_RSA_CTF/issues/1#issue-3872342957" width="650">
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
