def sieve_of_eratosthenes(n: int) -> list[int]:
    """Trả về danh sách tất cả các số nguyên tố <= n."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]


def main():
    while True:
        try:
            n = int(input("Nhập số nguyên N (N >= 2): "))
            if n < 2:
                print("Vui lòng nhập số lớn hơn hoặc bằng 2 để tìm số nguyên tố!\n")
                continue
            break
        except ValueError:
            print("Giá trị không hợp lệ! Vui lòng nhập một số nguyên.\n")
    primes = sieve_of_eratosthenes(n)
    print(f"\nCó tất cả {len(primes)} số nguyên tố <= {n}:")
    print(primes)


if __name__ == "__main__":
    main()