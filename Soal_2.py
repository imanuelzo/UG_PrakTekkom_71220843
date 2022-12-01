a = input("Masukkan Kata: ")
palin = True
p_a = len(a)

for l in range(p_a//2):
    if (a[l] != a[p_a-l-1]):
        palin = False
        break
if palin:
    print ("Yes")
    print ("jikka dibalik", a)
else:
    print ("No")
    print ("jika dibalik: ", a)