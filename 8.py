import re

def main(data : str) -> dict:
    regex = re.compile(r"set\s*@\"(\w+)\"\s*=\s*([\d-]+)")

    res = {}
    for (name, value) in re.findall(regex, data): 
        res[name] = int(value)

    return res


if __name__ == "__main__":
    print(main("""
[<data>set @"este_583" = 5840 </data> <data> set @"usbear" = -2370
</data> <data>set @"arso_10" = -1480 </data><data>set @"vesobi"= 2526
</data> ]

               """))
