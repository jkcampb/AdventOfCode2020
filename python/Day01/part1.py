
def main():
    with open("Day01/input.txt") as input:
        report = [int(x) for x in input.readlines()]
        
    for i, val1 in enumerate(report):
        for j, val2 in enumerate(report[i+1:]):
            if val1+val2 == 2020:
                return val1*val2
    


if __name__ == "__main__":
    result = main()
    print(result)
