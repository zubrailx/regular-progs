import parse

def main():
    exp = parse.parse_expression("1 + \\cot 2")
    print(exp[0].calculate({}))


if __name__ == "__main__":
    main()
