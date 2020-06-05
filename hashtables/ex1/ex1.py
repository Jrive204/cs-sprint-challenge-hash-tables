def get_indices_of_item_weights(weights, length, limit):
    weight = {}
    dupe_check = False
    duplicates = {}  # in order to pass test 2 we need to account for duplicate values
    # iterate through weights and store them in the dict
    for i in range(0, length):
        current = weights[i]
        print(weight, current, i)
        weight[current] = i  # set the value to the index
        # we subtract the current value from the limit to find which package
        # combines to equal weight limit
        target = limit - current
        print(target, "target")
        if target in weight:
            print(target, "target in weight")
            if current > target or current < target:
                return (i, weight[target])  # tuple of indexes
            elif target == current:  # if it finds a dupe
                if dupe_check is False:  # and it isnt already clasified as a duplicate
                    dupe_check = True  # change the bool
                    duplicates[current] = i  # set the value to the index
                    print("dupe True, goes back to loop")
                elif dupe_check is True:
                    print("End loop")
                    return (i, duplicates[current])
    return None


if __name__ == "__main__":
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    print(get_indices_of_item_weights(weights_4, 9, 7))
    weights_2 = [4, 4]
    print(get_indices_of_item_weights(weights_2, 2, 8))
