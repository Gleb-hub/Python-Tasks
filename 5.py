def main(n: str) -> str:
    s1 = int(int(n) & (1 << 3) - 1)
    s2 = int(int(n) >> 3 & (1 << 4) - 1)
    s4 = int(int(n) >> 17 & (1 << 10) - 1)
    s5 = int(int(n) >> 27 & (1 << 10) - 1)

    new_s1 = s4;
    new_s2 = s1 << 20;
    new_s4 = s5 << 23;
    new_s5 = s2 << 33;
    
    return  str(hex(new_s1 | new_s2 | new_s4 | new_s5))


if __name__ == "__main__":
    print(main('239948252'))
