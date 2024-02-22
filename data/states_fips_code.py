"""
Helper to get the FIPS code for states
"""

def parse_fips_file():
    with open("data/fips.txt") as f:
        for line in f:
            print(line)

parse_fips_file()