# From a problem on HackerRank for Indeed.

import string

def convert_string(input_string):
    '''Returns a converted copy of input_string.

    A string is converted by the following method:
      For each letter in the string at index i, advance the letter by the number of times
      that letter has appeared in the string at indices 0-i (not including i).
      For example:
      "abc" -> "abc" (No letters repeat)
      "bbb" -> "bcd" (The first b is a new letter, the second b has been seen once before
        and is advanced by one letter, and the third b has been seen twice before, and
        advances by two letters)
      "zz" -> "za" (Letters wrap around the end of the alphabet)

    Note that only appearances in the input_string are counted, not appearances
      in the converted result string. 

    input_string only contains characters in the range lowercase a-z.

    Returns the converted string.
    '''
    result_string = []
    # With 'a' at index 0, how many times has each letter been seen so far?
    counts = [0] * 26
    # 'a' = 0, 'z' = 25, etc
    letter_map = {x:y for x, y in zip(string.ascii_lowercase, xrange(26))}
    for letter in input_string:
        letter_id = letter_map[letter]
        if counts[letter_id]:
            new_letter = string.ascii_lowercase[(letter_id + counts[letter_id]) % 26]
            result_string.append(new_letter)
        else:
            result_string.append(letter)
        counts[letter_id] += 1
        #if not counts[]
    return "".join(result_string)