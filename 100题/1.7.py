def back(n):
    if n == 1:
        return 1000/(1+12*0.0063)
    else:
        return (back(n-1)+1000)/(1+12*0.0063)


a = back(5)
print("%.2f" % a)
