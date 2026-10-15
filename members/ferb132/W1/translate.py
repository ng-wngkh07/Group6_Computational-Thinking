def binary_to_demical(binary_str: str) -> int:
    demical_value = 0
    for i, digit in enumerate(reversed(binary_str)):
        if digit == '1':
            demical_value += 2 ** i
    return demical_value
def main():
    print(binary_to_demical("1100"))
    print(binary_to_demical("1010"))
if __name__ == "__main__":
    main()