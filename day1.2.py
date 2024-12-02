def similarity():
    with open("input1.1.txt") as file:
        data = file.readlines()
    
    digitOne = []
    digitTwo = []
    mult = 0
   

    for datas in data:
        nums = datas.strip().split()
        digitOne.append(nums[0])
        digitTwo.append(nums[1])

    for i in range(len(digitOne)):
        reps = digitTwo.count(digitOne[i])
        mult += int(digitOne[i]) * reps
    
        
        

    print(mult)

def main():
    similarity()

if __name__ == "__main__":
    main()