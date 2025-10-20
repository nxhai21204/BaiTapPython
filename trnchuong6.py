def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    if num == 1:
        return triangle(1) ** 2
    return triangle(num) ** 2 + square(num-1)
print(square(1))
# công thức square(n)=triangle(1)**2+triangle(2)**2+...+triangle(n)**2