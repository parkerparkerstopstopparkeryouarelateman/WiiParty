#!/usr/bin/env python3
"""
Author:  
Purpose: roll the dice
"""

import argparse
from dice import *

# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Roll dice')
    parser.add_argument('-d', '--dice', default=6, help='Number of sides',type=int)
    parser.add_argument('-r', '--rolls', default=1, help='Number of rolls',type=int)
    parser.add_argument('-f', '--freq', default=False, help='Output frequency', type=bool)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.freq:
        freq = countRolls(args.rolls, args.dice)
        print("roll","tally")
        for i in range(1,args.dice + 1):
            print(i,freq[i])
    
    else:
        my_roll = roll(args.rolls, args.dice)
        print(f"You rolled {my_roll}")


# --------------------------------------------------
if __name__ == '__main__':
    main()

