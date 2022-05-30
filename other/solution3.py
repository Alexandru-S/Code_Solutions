def find(the_list):
    """
    Function that takes in a list of integers representing
    the floors of a building.

    The below code takes in a number of floors and calculates which
    is the most optimal floor that can have the most amount of integers from
    the input list that fit inside the lower bounds of the floors.

    The definition of 'most integers' is that as long as the
    items_in_lower_range tracker is higher than the theoretical limit
    calculated by (lower_ceiling- lower floor +1)

    Args:
        the_list (list): integers of different

    Returns:
        int: most optimal floor

    """
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        midpoint = floor + (
            (ceiling - floor) // 2
        )  # calculates midpoint, which is from 1 to
        lower_floor, lower_ceiling = (
            floor,
            midpoint,
        )  # lower floor bound, lower ceiling bound
        upper_floor, upper_ceiling = (
            midpoint + 1,
            ceiling,
        )  # upper floor bound, upper ceiling bound

        items_in_lower_range = 0
        for item in the_list:
            if (
                item >= lower_floor and item <= lower_ceiling
            ):  # check if item in list is below the lower floor and ceiling bounds
                items_in_lower_range += 1  # if yes, increment items_in_lower_range by 1
        distinct_possible_integers_in_lower_range = (
            lower_ceiling - lower_floor + 1
        )  # tracking the difference between the lower ceiling and floor for possible max
        if (
            items_in_lower_range > distinct_possible_integers_in_lower_range
        ):  # if there are more items in the counter than theoretically possible, go to the lower bound and repeat cycle
            floor, ceiling = (
                lower_floor,
                lower_ceiling,
            )  # thus new floor will be the lower floor and new ceiling will be lower ceiling
        else:
            floor, ceiling = (
                upper_floor,
                upper_ceiling,
            )  # if not, go up one section and increase the floor bounds
    return floor


print(find([6, 2, 3, 4, 1, 4, 4]))
