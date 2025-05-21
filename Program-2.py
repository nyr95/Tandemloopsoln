def generate_series_count_based(x: int):
    result = []
    for i in range(x):
        result.append(2 * i + 1)
    print(", ".join(map(str, result)))


generate_series_count_based(4)  
