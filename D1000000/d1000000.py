import sys

lineas = sys.stdin.read().splitlines()

tokens = " ".join(lineas).split()
pos = 0

tiki = int(tokens[pos])
pos += 1

for caso in range(1, tiki + 1):
    n = int(tokens[pos])
    pos += 1
    temp = tokens[pos:pos + n]
    dados = sorted(map(int, temp))
    pos += n

    siguiente = 1
    for s in dados:
        if s >= siguiente:
            siguiente += 1

    print(f"Case #{caso}: {siguiente - 1}")