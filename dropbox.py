# Based on a problem from Dropbox:
# http://hr.gs/redbluebluered

def wordpattern(pattern, input, word_map=None):
    """Determines if pattern matches input.
    
    Given a pattern string and an input string, determine if the pattern matches the input,
    such that each character in pattern maps to a substring of input.

    Examples:
    abba, redbluebluered: matches
    abc, redbluebluered: matches
    abcdab, tobeornottobe: matches
    aba, nonrepeating: doesn't match

    Args:
        pattern: string, the input to match.

        input: string, the full string to check substrings.

    Returns:
        1 if there exist any mappings such that pattern matches input, 0 otherwise.
    """

    if not word_map:
        word_map = {}
    if pattern == "":
        # Out of characters to check; has the full input been matched?
        return 1 if input == "" else 0
    current_letter = pattern[0]
    if current_letter in word_map:
        # Letter exists earlier in the pattern
        word = word_map[current_letter]
        if input.startswith(word):
            return wordpattern(pattern[1:], input[len(word):], word_map)
        # Don't recurse if this appearance doesn't match the previous one
        return 0
    # TODO: Range can be smaller than this
    for length in xrange(1, len(input)):
        # Make a copy so that this mapping is only used for this recursive path
        temp_map = word_map.copy()
        temp_map[current_letter] = input[:length]
        if wordpattern(pattern[1:], input[length:], temp_map):
            return 1
    return 0

# Passing cases
print wordpattern("abba", "redbluebluered")
print wordpattern("abcdab", "tobeornottobe")
print wordpattern("xx", "xyzxyz")
print wordpattern("aba", "same word same")
# Failing cases
print wordpattern("aba", "nopatternhere")
print wordpattern("a", "abc")


