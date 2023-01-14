def string_perms(string):
    res = [string]
    for i in range(len(string)):
        if string[i].isalpha():
            length = len(res)
            for j in range(length):
                if string[i] == string[i].lower():
                    new = res[j][:i] + res[j][i].upper() + res[j][i+1:]
                else:
                    new = res[j][:i] + res[j][i].lower() + res[j][i+1:]
                res.append(new)
    return res


print(string_perms('ab7c'))
