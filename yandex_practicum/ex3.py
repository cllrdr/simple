def gen_seq():
    return range(10)
print(gen_seq())

def gen_seq1():
    return [num for num in range(10)]
print(gen_seq1())

def gen_seq2():
    return (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(gen_seq2())

def gen_seq3():
    num = 0
    while num < 3:
        yield num
        num += 1
print(gen_seq3())

for i in gen_seq3(): print(i)