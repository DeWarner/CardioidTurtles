# p = k-1
# s = mod/k
# for p = s
# mod = k * (k-1) 
# for p = 2s
# k-1= 2mod/k
# mod = k*(k-1)/2

def map(num):
    return num*(num-1)


def mess(num):
    return str(num) + ": "  + str(map(num))


ks = range(1, 1000)

messages = (mess(k) for k in ks)

for message in messages:
    input(message)


