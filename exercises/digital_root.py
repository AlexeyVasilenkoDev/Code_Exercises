def digital_root(n):
    while len(str(n)) > 1:
        n = sum([int(i) for i in list(str(n))])
    return n


digital_root(125)
digital_root(12532)
digital_root(9975)
digital_root(1)
