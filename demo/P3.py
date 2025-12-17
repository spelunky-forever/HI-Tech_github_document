import sys

def solve():
    input_data = input()
    if not input_data:
        return
    n_str = input_data[0]
    a = int(input_data[1])
    b = int(input_data[2])
    k = len(n_str)
    print(k)
    digits = list(n_str)
    digits[a-1], digits[b-1] = digits[b-1], digits[a-1]
    if a > k or b > k:
        print("NOT ACCEPT")
        return
    result_str = "".join(digits)
    print(int(result_str))

solve()