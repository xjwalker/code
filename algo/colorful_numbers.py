"""
   Objective: Given a number, find out whether its colorful or not.
   Colorful Number: When in a given number, product of every digit of a sub-sequence are different.
    That number is called Colorful Number.
   Example:

   Given Number : 3245

   Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
   this number is a colorful number, since product of every digit of a sub-sequence are different.
   That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

   Output : Colorful

   Given Number : 326
   326 is not a colorful number as it generates 3 2 6 (3*2)=6 and 6 is part of the original number.

   Output : Not Colorful

   """


def colorful_number(num: int):
    colorful = True
    s_nums = str(num)
    viewed_nums = set()
    for i in range(len(s_nums)):
        for j in range(i, len(s_nums)):
            aux_num = s_nums[i:j + 1]
            res = 1
            for n in aux_num:
                res *= int(n)
            if res in viewed_nums:
                colorful = False
                break
            viewed_nums.add(res)

    return colorful


def is_colorful_number(number):
    num_str = str(number)  # Convert number to string
    products = set()  # Create a set to store products
    for i in range(len(num_str)):
        for j in range(i, len(num_str)):
            sub_sequence = num_str[i:j + 1]
            product = 1
            for char in sub_sequence:
                product *= int(char)
            if product in products:
                return False
            products.add(product)
    return True


def main():
    print(colorful_number(326))
    print(colorful_number(3245))
    print(colorful_number(263))
    print(colorful_number(2232163))
    print(colorful_number(1))
    print(colorful_number(10))
    print('second func')
    print(is_colorful_number(326))
    print(is_colorful_number(3245))
    print(is_colorful_number(263))
    print(is_colorful_number(2232163))
    print(is_colorful_number(1))
    print(is_colorful_number(10))


if __name__ == '__main__':
    main()
