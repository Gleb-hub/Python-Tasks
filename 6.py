def main(n: str) -> str:
    c1 = int(int(n) & (1 << 7) - 1)
    c2 = int(int(n) >> 7 & (1 << 3) - 1)
    c3 = int(int(n) >> 10 & (1 << 6) - 1)
    c4 = int(int(n) >> 16 & (1 << 4) - 1)

    new_c1 = c1;
    new_c2 = c3 << 7;
    new_c3 = c4 << 13;
    new_c4 = c2 << 17;
    
    return  str(new_c1 | new_c2 | new_c3 | new_c4)


if __name__ == "__main__":
    print(main('743096'))

