import operator


def person_lister(f):
    def inner(people):
        # people.sort(key=lambda x: int(x[2]))
        # return list(map(f, people))

        people.sort(key=operator.itemgetter(2))
        # people = list(map(lambda person: int(person[2]), people))
        # print(people)
        people = map(f, people)

        # print(people)
        return list(people)

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [['Jake', 'Jake', '42', 'M'],
              ['Jake', 'Kevin', '57', 'M'],
              ['Jake', 'Michael', '91', 'M'],
              ['Kevin', 'Jake', '2', 'M'],
              ['Kevin', 'Kevin', '44', 'M'],
              ['Kevin', 'Michael', '100', 'M'],
              ['Michael', 'Jake', '4', 'M'],
              ['Michael', 'Kevin', '36', 'M'],
              ['Michael', 'Michael', '15', 'M'],
              ['Micheal', 'Micheal', '6', 'M']]
    print(*name_format(people), sep='\n')


"""
Mr. Kevin Jake
Mr. Michael Jake
Mr. Micheal Micheal
Mr. Michael Michael
Mr. Michael Kevin
Mr. Jake Jake
Mr. Kevin Kevin
Mr. Jake Kevin
Mr. Jake Michael
Mr. Kevin Michael
"""

"""
Mr. Kevin Michael
Mr. Michael Michael
Mr. Kevin Jake
Mr. Michael Kevin
Mr. Michael Jake
Mr. Jake Jake
Mr. Kevin Kevin
Mr. Jake Kevin
Mr. Micheal Micheal
Mr. Jake Michael
"""