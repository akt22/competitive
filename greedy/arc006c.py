def main():
    aggs = []
    for cargo in cargos:
        if not aggs:
            aggs.append(cargo)
            continue
        cand = [0, float('inf')]  # idx, value
        for idx, agg in enumerate(aggs):
            if cargo <= agg < cand[1]:
                cand = [idx, agg]
        if cand == [0, float('inf')]:
            aggs.append(cargo)
        else:
            aggs[cand[0]] = cargo

    print(len(aggs))

if __name__ == "__main__":
    N = int(input().strip())
    cargos = []
    for _ in range(N):
        cargos.append(int(input().strip()))
    main()
