import random

class Dice:
    def __init__(self):
        self.side_now = 0

    def throw_dice(self):
        self.side_now = random.randint(1,20)

    def get_dice_side(self):
        return self.side_now

def main():
    my_dice = Dice()
    my_dice.throw_dice()
    print(my_dice.get_dice_side())
    my_dice.throw_dice()
    print(my_dice.get_dice_side())

main()
