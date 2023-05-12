
a, b = map(float, input().split())
c, d = map(float, input().split())


x = complex(a, b)
y = complex(c, d)
sum = x + y
diff = x - y
prod = x * y
div = x / y
mod_x = abs(x)
mod_y = abs(y)

print('{:.2f}{:+.2f}i'.format(sum.real, sum.imag))
print('{:.2f}{:+.2f}i'.format(diff.real, diff.imag))
print('{:.2f}{:+.2f}i'.format(prod.real, prod.imag))
print('{:.2f}{:+.2f}i'.format(div.real, div.imag))
print('{:.2f}{:+.2f}i'.format(mod_x.real, mod_x.imag))
print('{:.2f}{:+.2f}i'.format(mod_y.real, mod_y.imag))

