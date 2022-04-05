# very impromptu solution to count case switches of a string, not optimized for performance

def count_case_switches(letters):
    count = 0
    if len(letters) > 1:

        for i in range(0, len(letters)):
            # index position 0 check
            if i == 0:
                if letters[0].isupper():
                    lastchar = "upper"
                elif letters[0].islower():
                    lastchar = "lower"

            elif letters[i].isupper() and lastchar == "lower":
                lastchar = "upper"
                count+=1
            elif letters[i].islower() and lastchar == "upper":
                lastchar = "lower"
                count+=1
            else:
                continue

    return count
    # loop over string with range(len)

if __name__ == "__main__":
    print(count_case_switches(""))  # Prints 0
    print(count_case_switches("aaaBa"))  # Prints 2
    print(count_case_switches("bAbA"))  # Prints 3
