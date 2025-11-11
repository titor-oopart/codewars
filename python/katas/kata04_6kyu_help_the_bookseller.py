def stock_list(stocklist, categories):
    if len(stocklist) == 0:
        return ""
    arr = [item[0] for item in stocklist]
    solution = []
    for categorie in categories:
        if categorie in arr:
            ind = [i for i, val in enumerate(arr) if val == categorie]
            amount = [int(stocklist[index].split()[1]) for index in ind]
            solution.append(f"({categorie} : {sum(amount)})")
        else:
            solution.append(f"({categorie} : 0)")

    return " - ".join(solution)
