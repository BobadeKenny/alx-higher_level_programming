#!/usr/bin/python3
for i in range(99):
    print("{:0>2}".format(i), end=", ")
print("{:d}".format(i+1))
