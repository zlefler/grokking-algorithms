
# mainly good python tricks here. isalpha() is helpful,
# converting a string to an array just be prepending list,
# and swapcase() all help make this solution very clean.

# other than that, you just copy the string each time and add
# a version with the case swapped.

def find_permutations(string):
    '''Given a string, find all of its permutations preserving the character sequence but changing case.'''
    permutations = []
    permutations.append(string)
    for i in range(len(string)):
        if string[i].isalpha():
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations


print(find_permutations('ab7c'))
