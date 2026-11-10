import sys

lineas = sys.stdin.read().splitlines()

tokens = " ".join(lineas).split()
pos = 0

tiki = int(tokens[pos]); pos += 1

for caso in range(1, tiki + 1):
    n = int(tokens[pos])
    pos += 1
    actividades = []
    for i in range(n):
        s = int(tokens[pos])
        e = int(tokens[pos + 1])
        pos += 2
        actividades.append((s, e, i))

    actividades.sort()

    libre = {"C": 0, "J": 0}
    resultado = [""] * n
    posible = True
    k = 0

    while posible and k < len(actividades):
        s, e, i = actividades[k]
        if libre["C"] <= s:
            libre["C"] = e
            resultado[i] = "C"
        elif libre["J"] <= s:
            libre["J"] = e
            resultado[i] = "J"
        else:
            posible = False
        k += 1

    if posible:
        print(f"Case #{caso}: {''.join(resultado)}")
    else:
        print(f"Case #{caso}: IMPOSSIBLE")