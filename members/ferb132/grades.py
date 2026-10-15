def summary(score: list[float]) -> dict:
    if len(score) == 0:
            raise ValueError("Danh sách điểm số để trống")
    kq = {}
    kq["max"] = max(score)
    kq["min"] = min(score)
    kq["mean"] = round(sum(score) / len(score), 2)
    sorted_score = sorted(score)
    n = len(score)
    if n % 2 == 1:
        kq["median"] = sorted_score[n // 2]
    else:
        kq["median"] = round((sorted_score[n // 2] + sorted_score[n // 2 - 1]) / 2, 2)
    return kq

def main():
    a = {}
    a = summary([7.5, 9, 6, 8])
    print(a)

if __name__ == "__main__": 
    main()
