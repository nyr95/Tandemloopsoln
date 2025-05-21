def generate_series_value_based(x: int):
    result = []
    i = 1
    while i <= x:
        result.append(i)
        i += 2
    print(", ".join(map(str, result)))

# Example
generate_series_value_based(6) 
