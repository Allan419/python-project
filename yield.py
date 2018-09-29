# encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield i * 2
        print("i=", i)


print(yield_test(5))
for i in yield_test(5):
    print(i, ",")


print('Anything possible')
