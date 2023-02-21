"""
Colorful Numbers
Objective: Given a number, find out whether its colorful or not.

Colorful Number: When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number. See Example

Example:

Given Number : 3245
Output : Colorful

Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
this number is a colorful number, since product of every digit of a sub-sequence are different.
That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

Given Number : 326
Output : Not Colorful.

326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.

"""


def is_colorful(num):
    num = str(num)
    products = {int(n): True for n in num}
    for i in range(len(num)):
        aux = ''
        for j in range(i + 1, len(num)):
            aux += num[j]
            if int(num[i]) * int(aux) in products:
                return False
            products[num[i] * int(aux)] = True
    return True


# chat gpt solution:
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
    res = is_colorful(326)
    assert res is False
    res = is_colorful(3245)
    assert res is True
    assert is_colorful(326) is False
    assert is_colorful(3245) is True
    assert is_colorful(263) is True
    assert is_colorful(2232163) is False
    assert is_colorful(1) is True
    assert is_colorful(10) is False
    assert is_colorful(1123) is False


if __name__ == '__main__':
    main()
