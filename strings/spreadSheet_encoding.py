import functools

def ss_decode_col_id(s):
    return functools.reduce(lambda result, c : result * 26 + ord(c) - ord('A') + 1, s, 0)



ss_decode_col_id("AA")