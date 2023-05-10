def persistence(n):
    persistence_counter = 0
    while len(str(n)) > 1:
        persistence_counter += 1
        num = [i for i in str(n)]
        n = eval(" * ".join(num))
    return persistence_counter


print(persistence(999))
