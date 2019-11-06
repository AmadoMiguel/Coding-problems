
def checkNonDecreasingArray(arr):
    # Iterate over the array by indexes
    noOfMOdifications = 0  # This should be 1 at the most
    for i in range(len(arr)):
        # If in first position
        if i == 0:
            if arr[i] >= arr[i + 1]:
                # Actually modify it in order to facilitate the process
                arr[i] = arr[i + 1] - 1
                # Add counter for number of modifications
                noOfMOdifications += 1
                # Verify with the next position if the array is non-decreasing
                if arr[i] > arr[i + 1]:
                    return False
        # Any other position
        else:
            if arr[i] < arr[i - 1]:
                # In this case, return false immediately in case both conditions are true
                if i < len(arr) - 1 and arr[i] > arr[i + 1]:
                    return False
                else:
                    if i != len(arr) - 1:
                        # Modify it according to the previous element
                        arr[i] = arr[i - 1] + 1
                        # Add # of modifications
                        noOfMOdifications += 1
                        # If by modifying it the rule breaks, return False
                        if arr[i] > arr[i + 1]:
                            return False
                    else:
                        if arr[i] < arr[i - 1]:
                            # Check if there is any previous modification
                            if noOfMOdifications:
                                return False
                            else:
                                arr[i] = arr[i - 1] + 1
                                # Should be the first (and only) modification
                                noOfMOdifications += 1
        # Reduce the computation time in case the only needed modification was already done
        # or in case there is one modification and another one is required
        if arr == list(sorted(arr)) and noOfMOdifications <= 1:
            print("Ordered", arr)
            return True
        elif arr != list(sorted(arr)) and noOfMOdifications == 1:
            return False
    # Make sure there was only one modification throughout all the traversal
    return noOfMOdifications == 1


print(checkNonDecreasingArray([13, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
