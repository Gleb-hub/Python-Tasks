def main(fields: dict) -> str:
    z1 = int(fields['z1'])
    z2 = int(fields['z2']) << 3
    z3 = int(fields['z3']) << 9
    z5 = int(fields['z5']) << 17
    z6 = int(fields['z6']) << 23 
    return str(hex(z1 | z2 | z3 | z5 | z6))




if __name__ == "__main__":
    print(main({'z1': '3', 'z2': '2', 'z3': '11', 'z5': '32', 'z6': '525'}))

