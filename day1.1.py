

def distance():
    with open("input1.1.txt") as file:
        data = file.readlines()
    
    digitOne = []
    digitTwo = []

    for datas in data:
        nums = datas.strip().split()
        digitOne.append(nums[0])
        digitTwo.append(nums[1])

    sortedOne = []
    sortedTwo = []
    diff = []
    dist = 0
    
    sortedOne = sorted(digitOne)
    sortedTwo = sorted(digitTwo)

    for i,j in zip(sortedOne, sortedTwo):
        diff.append(abs(int(i) - int(j)))
        dist = sum(diff)
        
    print(dist)
        


def main():
    distance()

if __name__ == "__main__":
    main()