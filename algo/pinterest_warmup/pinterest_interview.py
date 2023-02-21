k = [
    [0, 1, 1, 0],  # 0
    [0, 0, 1, 0],  # 1 a
    [0, 0, 0, 0],  # 2
    [0, 0, 1, 0]  # 3 a nobody.
]


def knows(i: int, j: int):
    return k[i][j] == 1


def get_celebrity(n: int):
    celebs = set()
    not_celeb = set()
    for me in range(n):
        for person in range(n):
            if me != person:
                if knows(me, person) and not knows(person, me) and person not in not_celeb:
                    celebs.add(person)
                    not_celeb.add(me)
                elif knows(person, me):
                    not_celeb.add(me)
                    if person in celebs:
                        celebs.remove(person)
                elif not knows(me, person):
                    not_celeb.add(person)
                    if person in celebs:
                        celebs.remove(person)

    return -1 if len(celebs) == 0 else list(celebs)[0]


def main():
    res = get_celebrity(len(k))
    assert res == 2


if __name__ == '__main__':
    main()