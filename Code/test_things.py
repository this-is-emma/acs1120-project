from hashtable import HashTable


ht = HashTable()
ht.set('I', 1)
ht.set('V', 4)
ht.set('X', 9)

print('ht before: ',ht)

ht.set('V', 5)

print('ht after updating V: ',ht)
# ht.set('X', 10)

