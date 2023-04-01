def main(n: str) -> list[tuple[str, str]]:
    r1 = str(int(n, 16) & (1 << 6) - 1)
    r2 = str(int(n, 16) >> 6 & (1 << 6) - 1)
    r3 = str(int(n, 16) >> 12 & (1 << 7) - 1)
    r4 = str(int(n, 16) >> 19 & (1 << 2) - 1)
    r5 = str(int(n, 16) >> 21 & (1 << 3) - 1)

    return [('N1', r1), ('N2', r2), ('N3', r3), ('N4', r4), ('N5', r5)]


if __name__ == "__main__":
    print(main('0xb9a562'))

