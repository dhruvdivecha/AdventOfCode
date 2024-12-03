def is_safe(numbers):
    prev_diff = numbers[0] - numbers[1]

    if not (1 <= abs(prev_diff) <= 3): 
        return False

    direction = "decreasing" if prev_diff > 0 else "increasing"

    for i in range(1, len(numbers) - 1):
        diff = numbers[i] - numbers[i + 1]

        if not (1 <= abs(diff) <= 3):  
            return False

        if direction == "decreasing" and diff > 0:
            continue
        elif direction == "increasing" and diff < 0:
            continue
        else:
            return False 

    return True


def dampener(filename):
    try:
        with open(filename) as file:
            data = file.readlines()
    except FileNotFoundError:
        print("Input file not found!")
        return

    safe_count = 0

    for line in data:
        numbers = list(map(int, line.strip().split()))
        if not numbers:
            continue

        if is_safe(numbers):
            safe_count += 1
            continue

        for i in range(len(numbers)):
            temp_numbers = numbers[:i] + numbers[i+1:]
            if is_safe(temp_numbers):
                safe_count += 1
                break

    print(safe_count)


def main():
    dampener("day2.input")


if __name__ == "__main__":
    main()
