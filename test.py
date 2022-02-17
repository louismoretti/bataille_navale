import random

l = [random.randint(0,100) for i in range(10)]

def tri_insertion(tab):
    for i in range(1,len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = x
    return tab

print(tri_insertion(l))