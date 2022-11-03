import numpy as np


from scipy import stat

print("Qno. 1: Find the mean of this particular dataset")

Warda_k = [99, 86 , 87 , 88 , 384 , 86 , 103 , 87 , 94 , 78 , 77 , 85 , 86]
me = np.mean(Warda_k)
print(me)


print("Qno. 2: Find the median of the dataset of odd value?")

warda_1 = [77, 78, 85,86,86,86,87,34,88,94,99,103,111]

med = np.median(warda_1)
print(med)

# even value

K_warda = [77, 78, 85,86,86,86,87,87,88,94,99,103]

even = np.median(K_warda)
print(even)

print("Qno. 3: Find the mode of the dataset, hence we use Warda_1 dataset")

sp = stat.mod(warda_1)
print(sp)



print("How to do standard derivation in python?")

W_khurshid = [99, 86 , 7 , 33 , 11 , 80 , 999 , 833]
st = np.std(W_khurshid)
print(st)

print("How to find a variance? Use a same list ")

v = np.var(W_khurshid)
print(v)



