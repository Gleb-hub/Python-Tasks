def main(data: tuple[int, ...]) -> int:
    v1 = data[0]
    v2 = data[1] << 9
    v3 = data[2] << 18
    v4 = data[3] << 19
    v5 = data[4] << 23
    v6 = data[5] << 24

    return v1 | v2  | v3 | v4 | v5 | v6


if __name__ == "__main__":
    print(main((376, 159, 1, 0, 1, 21)))
