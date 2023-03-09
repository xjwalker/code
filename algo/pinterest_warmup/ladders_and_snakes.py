def find_dice_value(missing_steps):
    dice_rolls = 0
    while missing_steps > 0:
        if missing_steps - 6 >= 0:
            dice_rolls += 1
            missing_steps -= 6
        elif missing_steps - 5 >= 0:
            dice_rolls += 1
            missing_steps -= 5

        elif missing_steps - 4 >= 0:
            dice_rolls += 1
            missing_steps -= 4

        elif missing_steps - 3 >= 0:
            dice_rolls += 1
            missing_steps -= 3

        elif missing_steps - 2 >= 0:
            dice_rolls += 1
            missing_steps -= 2

        elif missing_steps - 1 >= 0:
            dice_rolls += 1
            missing_steps -= 1
    return dice_rolls

def get_dice(position, snakes_d, dice=6, count=0):
    if position + dice == 100:
        return count

    if position + dice  in snakes_d:
        return get_dice(position, snakes_d, dice - 1, count)


    return get_dice(position, snakes_d, count=count)


def ladders_and_snakes(ladders, snakes):
    min_amount_moves = -1

    # go through the ladders and find a the tallest
    # see how many moves are left
    # loop to find the dice combination to get me there
    # if positions touch a snake we re-roll with constains.
    snakes_d = {key: value for key, value in snakes}
    ladder_d = {key: value for key, value in ladders}
    print(snakes_d)
    tallest_ladder = []
    curr_position = 1
    i = 0
    for ladder_start, ladder_end in ladders:
        dice_rolls = find_dice_value(ladder_start - 1)
        curr_position = ladder_end
        # todo; should ask for another ladder?
        i += 1
        missing_steps = 100 - curr_position
        for position in range(missing_steps, 100):


    return min_amount_moves


def main():
    ladders = [[32, 62], [42, 68], [12, 98]]
    snakes = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
    res = ladders_and_snakes(ladders, snakes)
    print(res)

    # ladders = [[8, 52], [6, 80], [26, 42], [2, 72]]
    # snakes = [[51, 19], [39, 11], [37, 29], [81, 3], [59, 5], [79, 23], [53, 7], [43, 33], [77, 21]]
    # res = ladders_and_snakes(ladders, snakes)
    # print(res)


if __name__ == '__main__':
    main()
