import sys

lineas = sys.stdin.read().splitlines()

def resolver(n, k):
    actual = {n: 1}
    while True:
        for tam in sorted(actual, reverse=True):
            c = actual[tam]
            if k <= c:
                return (tam // 2, (tam - 1) // 2)
            k -= c

        siguiente = {}
        for tam, c in actual.items():
            if tam > 0:
                mayor = tam // 2
                menor = (tam - 1) // 2
                siguiente[mayor] = siguiente.get(mayor, 0) + c
                siguiente[menor] = siguiente.get(menor, 0) + c
        actual = siguiente

tiki = int(lineas[0])

for caso in range(1, tiki + 1):
    n_str, k_str = lineas[caso].split()
    mayor, menor = resolver(int(n_str), int(k_str))
    print(f"Case #{caso}: {mayor} {menor}")