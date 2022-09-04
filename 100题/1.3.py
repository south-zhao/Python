def so(a, b, c, d):
    x = 1.5
    x0 = x
    f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
    fd = 3 * a * x0 * x0 + 2 * b * x0 + c
    h = f / fd
    x = x0 - h
    while abs(x - x0) >= 1e-5:
        x0 = x
        f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
        fd = 3 * a * x0 * x0 + 2 * b * x0 + c
        h = f / fd
        x = x0 - h

    return x


print("请输入方程的系数:")
a, b, c, d = map(float, input().split())  # map类型转换和其他功能 , split()默认以空格分开
print("方程的系数:", a, b, c, d)
x = so(a, b, c, d)
print("方程的根为:x = %.6f" % x)
