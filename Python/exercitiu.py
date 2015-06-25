#!/usr/bin/env python

import sys


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)


try:
    fp = open(sys.argv[1], "r")
except IOError as e:
    print >> sys.stderr, "Argument is not a valid filename"
    sys.exit(2)

max = -1
min = 9999
nameMin = ""
nameMax = ""
prenumeMax = ""
prenumeMin = ""

for idx, line in enumerate(list(fp)):
    print "Line no: %d -> %s" % (idx, line)
    tokens = line.split('\t')
    grade = int(tokens[3])
    if max < grade:
        max = grade
        nameMax = tokens[1]
        prenumeMax = tokens[0]
    if min > grade:
        min = grade
        nameMin = tokens[1]
        prenumeMin = tokens[0]

print "Elevul cu nota maxima(%d) este %s" % (max, nameMax)
print "Elevul cu nota minima(%d) este %s" % (min, nameMin)

if __name__ == '__main__':
    sys.exit(main())
