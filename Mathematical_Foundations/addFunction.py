def add(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return (x1 + x2, y1 +y2)

p = (3, -2)
q = (-6 ,4)

points = add(p, q)
print(points)
