import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n_str = input_data[0]
    a = int(input_data[1])
    b = int(input_data[2])
    k = len(n_str)
    print(k)
    if a > k or b > k:
        print("NOT ACCEPT")
        return
    digits = list(n_str)
    idx_a = a - 1
    idx_b = b - 1
    digits[idx_a], digits[idx_b] = digits[idx_b], digits[idx_a]
    result_str = "".join(digits)
    print(result_str)

if __name__ == "__main__":
    solve()