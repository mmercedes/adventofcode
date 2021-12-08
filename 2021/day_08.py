
def p1():
    vals = []
    with open("./inputs/input_08.txt") as f:
        for line in f:
            vals += line.split("|")[1].split(" ")

    ans = 0

    for val in vals:
        if 2 <= len(val.strip()) <= 4 or len(val.strip()) == 7:
            ans += 1
    print("p1: %i" % ans)


"""
     000      aaa
    5   1    b   c
    5   1    b   c
    5   1    b   c
     666      ddd
    4   2    e   f
    4   2    e   f
    4   2    e   f
     333      ggg

you start knowing 1, 4, 7, 8 for sure
assume for example you dont know bacfged maps to 0123456
- terms:
  str(7) = string that represents 7 on the display like "acf"
  display(7) = referring to the physical representation of the number via segments
  len(7) = number of segments needed enabled to show the character

a) take the three len(6) strings since those map to a display of 0, 6, or 9
   display(6) has 1 matching characters with display(1) and you know string for 1 already
   now you know str(6)
   there are 5 left to figure out (0, 9, 2, 3, 5)
b) take the two len(6) strings since those map to a display of 0 or 9
   display(9) has 4 matching characters with display(4)
   now you know str(9) and str(0)
   there are 3 left to figure out (2, 3, 5)
c) take the three len(5) strings and check that
   display(3) and display(7) only have 3 in common 
   now you know str(3)
d) take last two len(5) strings and check that
   display(2) and display(6) only have 4 in common
   now you know str(2) and str(5)

in the above example:
  s1='cf', s4='bcdf', s7='acf', s8='abcdefg'
  s2='acdeg', s3='acdfg', s5='abdfg',
  s0='abcefg', s6='abdefg', s9='abcdfg'
"""
# given the ten input strings
# returns [str(0), ..., str(9)]
def decode_strings(strings):
    s0, s1, s2, s3, s4, s5, s6, s7, s8, s9 = ("", "", "", "", "", "", "", "", "", "")
    # strings with length 5 and 6 repectively
    fivestrs, sixstrs = ([], [])

    # determine str(1), str(4), str(7), and str(8)
    for s in strings:
        if len(s) == 2:
            s1 = s
        elif len(s) == 3:
            s7 = s
        elif len(s) == 4:
            s4 = s
        elif len(s) == 5:
            fivestrs.append(s)
        elif len(s) == 6:
            sixstrs.append(s)
        elif len(s) == 7:
            s8 = s
        else:
            raise Exception("logic error?")

    def matching_chars_count(a, b):
        return len(set(a) & set(b))
    
    # step a)
    sixstrs_left = []
    for s in sixstrs:
        if matching_chars_count(s, s1) == 1:
            s6 = s
        else:
            sixstrs_left.append(s)
    # step b)
    for s in sixstrs_left:
        if matching_chars_count(s, s4) == 4:
            s9 = s
        else:
            s0 = s
    # step c)
    fivestrs_left = []
    for s in fivestrs:
        if matching_chars_count(s, s7) == 3:
            s3 = s
        else:
            fivestrs_left.append(s)
    # step d)
    for s in fivestrs_left:
        if matching_chars_count(s, s6) == 4:
            s2 = s
        else:
            s5 = s
            
    return {s0:0, s1:1, s2:2, s3:3, s4:4, s5:5, s6:6, s7:7, s8:8, s9:9}
# to test above
#strs=['cf', 'bcdf', 'acf', 'abcdefg', 'acdeg', 'acdfg', 'abdfg', 'abcefg', 'abdefg', 'abcdfg']
#print("%s" % decode_strings(strs))

def parse_line(line):
    s = line.split("|")
    usp = ["".join(sorted(x.strip())) for x in s[0].split(" ") if len(x) > 0]
    fdov = ["".join(sorted(x.strip())) for x in s[1].split(" ") if len(x) > 0]
    
    # unique signal pattern, four digit output value
    return (usp, fdov)
# to test above
# print("usp: %s\nfdov: %s" % parse_line("cgdf eagcbf fc adefg eacdb fbedga geafcd efc dacfe fdgaecb | dcefbag dgcf fc daefc"))

# given ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'] return 5353
def fdov_val_from_map(code_lookup, fdov):
    ans = ""
    for x in fdov:
        ans += str(code_lookup[x])
    return int(ans)
# to test above
# given ['cdfeb', 'cdbaf', 'cdfeb', 'cdbaf'] return 5353
#print("%s" % str(fdov_val_from_map({'cdfeb':5,'cdbaf':3}, ['cdfeb', 'cdbaf', 'cdfeb', 'cdbaf'])))

def p2():
    ans=0
    with open("./inputs/input_08.txt") as f:
        for line in f:
            usp, fdov = parse_line(line)
            code_lookup = decode_strings(usp)
            ans += fdov_val_from_map(code_lookup, fdov)
    print("p2: %i" % ans)

p1()
p2()
