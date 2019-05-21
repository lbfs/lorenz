def attractor(a=10, b=28, c=8.0/3.0, x=0.01, y=0, z=0):
    while True:
        dt = 0.01
        dx = (a * (y - x)) * dt
        dy = (x * (b - z) - y) * dt
        dz = (x * y - c * z) * dt
        x = x + dx
        y = y + dy
        z = z + dz
        yield [x, y, z]
