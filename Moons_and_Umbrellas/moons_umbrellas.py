import sys

lineas = sys.stdin.read().splitlines()

inf = float("inf")
tiki = int(lineas[0])

for caso in range(1, tiki + 1):
    x_str, y_str, s = lineas[caso].split()
    X = int(x_str)
    Y = int(y_str)
    dp = {"C": inf, "J": inf}
    primero = True
    for ch in s:
        opciones = "CJ" if ch == "?" else ch
        nuevo = {"C": inf, "J": inf}
        for c in opciones:
            if primero:
                nuevo[c] = 0
            else:
                for p in "CJ":
                    if dp[p] == inf:
                        continue
                    costo = dp[p]
                    if p == "C" and c == "J":
                        costo += X
                    elif p == "J" and c == "C":
                        costo += Y
                    if costo < nuevo[c]:
                        nuevo[c] = costo
        dp = nuevo
        primero = False

    print(f"Case #{caso}: {min(dp.values())}")