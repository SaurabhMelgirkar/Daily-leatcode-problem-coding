def binary_vault(s):

    if s == "NULL":
        return -1

    if len(s) == 1:
        return int(s)

    result = int(s[0])   # take first number

    for i in range(1, len(s), 2):
        operator = s[i]
        next_number = int(s[i+1])

        if operator == 'A':      # AND
            result = result & next_number
        elif operator == 'B':    # OR
            result = result | next_number
        elif operator == 'C':    # XOR
            result = result ^ next_number

    return result


print(binary_vault("1C0C1C1A0B1"))
