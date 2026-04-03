import csv
import config_exp

def load_numbers():
    nums = []
    with open(config_exp.INPUT_FILE) as f:
        for line in f:
            nums.append(int(line.strip()))
    return nums

def filter_numbers(nums):
    return [n for n in nums if n > config_exp.THRESHOLD]

def save_numbers(nums):
    with open(config_exp.OUTPUT_FILE,"w") as f:
        for n in nums:
            f.write(str(n) + "\n")
        
def main():
    nums = load_numbers()
    filtered = filter_numbers(nums)
    save_numbers(filtered)

if __name__ == "__main__":
    main()