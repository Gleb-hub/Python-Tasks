import re

def main(data : str) -> list:
    regex = re.compile(r"array\(\s*@'(\w*)'\s*;\s*@'(\w*)'\s*;\s*@'(\w*)'\s*\)\s*to\s*q\((\w+)\)")

    res = []
    for (first, second, third, name) in re.findall(regex, data):
        tup = (name, [first, second, third])
        res.append(tup)

    return res


if __name__ == "__main__":
    print(main("||<sect> data array( @'cebi_815'; @'geso'; @'usla_563' ) to q(dite_207);</sect>;<sect> data array( @'zaatus_229' ; @'ave'; @'enre' )to q(raat); </sect>;||"))
