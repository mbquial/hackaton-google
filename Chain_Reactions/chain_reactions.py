import sys

lineas = sys.stdin.read().splitlines()

tokens = " ".join(lineas).split()
pos = 0

tiki = int(tokens[pos]); pos += 1

for caso in range(1, tiki + 1):
    n = int(tokens[pos]); pos += 1
    F = [0] + [int(x) for x in tokens[pos:pos + n]]
    pos += n
    P = [0] + [int(x) for x in tokens[pos:pos + n]]
    pos += n

    hijos = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        hijos[P[i]].append(i)

    total = [0] * (n + 1)
    maximo = [0] * (n + 1)

    for v in range(n, 0, -1):
        if not hijos[v]:
            total[v] = F[v]
            maximo[v] = F[v]
        else:
            suma = sum(total[c] for c in hijos[v])
            m_min = min(maximo[c] for c in hijos[v])
            maximo[v] = max(m_min, F[v])
            total[v] = suma - m_min + maximo[v]

    respuesta = sum(total[r] for r in hijos[0])
    print(f"Case #{caso}: {respuesta}")