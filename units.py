"""units.py defines classes for units with various characteristics."""

import random

DICE_SIDES = [1, 2, 3, 4, 5, 6]


class Unit:

    def __str__(self):
        return self.name

    def attack(self):
        """Roll for a hit, using self.attack_value"""
        roll = random.choice(DICE_SIDES)
        if roll <= self.attack_value:
            result = "hit"
        else:
            result = "miss"
        print("{} rolls a {}, {}!".format(self.name, roll, result))
        return result

    def defend(self):
        roll = random.choice(DICE_SIDES)
        if roll <= self.defend_value:
            result = "hit"
        else:
            result = "miss"
        print("{} rolls a {}, {}!".format(self.name, roll, result))
        return result


# --- GROUND UNITS --- #
class Infantry(Unit):
    def __init__(self):
        self.name = "Infantry"
        self.attack_value = 1
        self.defend_value = 2


class Artillery(Unit):
    def __init__(self):
        self.name = "Artillery"
        self.attack_value = 2
        self.defend_value = 2


class MechanizedInfantry(Unit):
    def __init__(self):
        self.name = "Mechanized Infantry"
        self.attack_value = 1
        self.defend_value = 2


class SupportedInfantry(Infantry):  # Deals with enhanced attack for Infantry supported by Artillery
    def __init__(self):
        super().__init__()
        self.name = "Supported Infantry"
        self.attack_value = 2


class SupportedMechInfantry(MechanizedInfantry):  # Deals with enhanced attack for MechInfantry supported by Artillery
    def __init__(self):
        super().__init__()
        self.name = "Supported Mechanized Infantry"
        self.attack_value = 2


class Tank(Unit):
    def __init__(self):
        self.name = "Tank"
        self.attack_value = 3
        self.defend_value = 3


# --- AIR UNITS --- #
class Fighter(Unit):
    def __init__(self):
        self.name = "Fighter"
        self.attack_value = 3
        self.defend_value = 4


class TacticalBomber(Unit):
    def __init__(self):
        self.name = "Tactical Bomber"
        self.attack_value = 3
        self.defend_value = 3


class CombinedArmsTacticalBomber(TacticalBomber):
    def __init__(self):
        super().__init__()
        self.name = "Tactical Bomber in Combined Arms"
        self.attack_value = 4


class StrategicBomber(Unit):
    def __init__(self):
        self.name = "Strategic Bomber"
        self.attack_value = 4
        self.defend_value = 1


# --- NAVAL UNITS --- #
class Submarine(Unit):
    """This is just for submarines in battles where the defender has a destroyer.  Roll sneak attacks manually."""
    def __init__(self):
        self.name = "Submarine"
        self.attack_value = 2
        self.defend_value = 1


class Destroyer(Unit):
    def __init__(self):
        self.name = "Destroyer"
        self.attack_value = 2
        self.defend_value = 2


class Cruiser(Unit):
    def __init__(self):
        self.name = "Cruiser"
        self.attack_value = 3
        self.defend_value = 3


class Battleship(Unit):
    """This class includes damaged battleships - relying on players to count damage and remove as necessary"""
    def __init__(self):
        self.name = "Battleship"
        self.attack_value = 4
        self.defend_value = 4


class AircraftCarrier(Unit):
    def __init__(self):
        self.name = "Aircraft Carrier"
        self.attack_value = 0
        self.defend_value = 2
