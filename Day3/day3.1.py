import re 

def open_file():
    with open("day3.input") as file:
        content = file.read()
    return content

def part_one(content):
    numbers = re.findall("(mul)\(([0-9]+),([0-9]+)\)", content)
    add = 0

    for number in numbers:
        mult = int(number[1]) * int(number [2])
        add += mult

    print("part one:", add )

def part_two(content):
    numbers = re.finditer(r"(do\(\))|(don't\(\))|(mul\(([0-9]+),([0-9]+)\))|", content)

    do = True    
    total = 0

    for number in numbers:
        if number.group(1):
            do = True
        elif number.group(2):
            do = False
        if number.group(3) and do:
            mult = int(number.group(4)) * int(number.group(5))
            total += mult

    print("part Two:", total )
        

def main():
    content = open_file()
    part_one(content)
    part_two(content)

if __name__ == "__main__":
    main()