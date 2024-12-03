import re 

def total():
    with open("day3.input") as file:
        content = file.read()

        numbers = re.findall("(mul)\(([0-9]+),([0-9]+)\)", content)
        
        add = 0

        for number in numbers:
            mult = int(number[1]) * int(number [2])
            add += mult

        print(add)

def main():
    total()

if __name__ == "__main__":
    main()