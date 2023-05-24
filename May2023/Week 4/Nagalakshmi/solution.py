from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

product_list = list(product(A, B))
sorted_product = sorted(product_list)

output = ' '.join([str(tuple_item) for tuple_item in sorted_product])
print(output)
