def main(n: str) -> list[tuple[str, str]]:
    r1 = str(int(n, 16) & (1 << 4) - 1)
    r2 = str(int(n, 16) >> 4 & (1 << 9) - 1)
    r3 = str(int(n, 16) >> 13 & (1 << 3) - 1)
    r4 = str(int(n, 16) >> 16 & (1 << 3) - 1)
    r5 = str(int(n, 16) >> 19 & (1 << 6) - 1)

    return [('R1', r1), ('R2', r2), ('R3', r3), ('R4', r4), ('R5', r5)]


if __name__ == "__main__":
    print(main('0x6a9f6'))

