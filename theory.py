# p = k-1
# s = mod/k
# for p = s
# mod = k * (k-1) 
# for p = 2s
# k-1= 2mod/k
# mod = k*(k-1)/2
for k in range(1, 100):
    input(str(k) + ": " + str(k*(k-1)/2))

