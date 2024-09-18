# import lottory as random

# lottery=[]
# for x in range(100):
#     lottery.append(random.randint(100,200))

# print(lottery)

# import random

# lottery_nos=[]
# for x in range(100):
#     lottery_nos.append(random.randint(100,200))

# #print(lottery_nos)

# luckydip=random.sample(lottery_nos,2)
# print(luckydip)

import random

def generate_lottery_numbers(num_count, min_num, max_num):
    """Generate a set of unique lottery numbers."""
    if num_count > (max_num - min_num + 1):
        raise ValueError("Number of lottery numbers requested exceeds the range of possible numbers.")
    
    return random.sample(range(min_num, max_num + 1), num_count)

def main():
    num_count = 6  # Number of lottery numbers to generate
    min_num = 1    # Minimum possible number
    max_num = 49   # Maximum possible number

    lottery_numbers = generate_lottery_numbers(num_count, min_num, max_num)
    print(f"Your lottery numbers are: {sorted(lottery_numbers)}")

if __name__ == "__main__":
    main()
