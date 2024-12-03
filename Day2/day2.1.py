def safety():
    with open("day2.input") as file:
        data = file.readlines()
    
    counter = 0

    for line in data:
        numbers = list(map(int, line.strip().split()))
        if check_safety(numbers):
            counter += 1
    
    print(counter)


def check_safety(number):
        for i in range(len(number) - 1):
            diff = number[i] - number[i + 1]

            prev_diff = 0

            if number[i] == number[i + 1]:
                return False
                

            if (prev_diff >= 0 and diff >= 0) or (prev_diff <= 0 and diff <= 0):
                if 1 <= abs(diff) <= 3:
                    prev_diff = diff
                else:
                    return False
                    
            else:
                return False
                
        return True
        
        
def main():
    safety()

if __name__ == "__main__":
    main()