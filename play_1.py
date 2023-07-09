#!/usr/bin/env python3
"""
Author:  
Purpose: play a game
"""

import argparse
from player import Player
from game import Game

# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Play a game')
    parser.add_argument('-g', '--games', default=1, help='Number of games',type=int)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    game = Game("Default", skill=0.8)

    p1 = Player("Bob")
    p2 = Player("Sandy", rating=90)
    p3 = Player("Ken", rating=98)
    p4 = Player("Dan", rating=94)
    p2.set_property("luck",35)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(game)
    print(f"\nlet's play a game {args.games} time(s)")
    for i in range(0,args.games):
        results = game.compete([p1,p2,p3,p4])
        print(','.join([player.name for player in results]))

# --------------------------------------------------
if __name__ == '__main__':
    main()

