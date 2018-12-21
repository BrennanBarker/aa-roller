from units import *
from battle_formations import attacking_force, defending_force


def roll_for_hits(force, side):
    total_hits = 0
    for unit_type in force:
        for roll in range(0, force[unit_type]):
            unit = unit_type()
            if (side == "attacking" and unit.attack() == "hit") or (side == "defending" and unit.defend() == "hit"):
                total_hits += 1
    return total_hits


def is_sneak_attack(force1, force2):
    """Check if a submarine sneak attack is possible."""
    return (force1[Submarine] > 0 and force2[Destroyer] == 0) or (force2[Submarine] > 0 and force1[Destroyer] == 0)


def account_for_supported_infantry(force):
    """Take account of Infantry or Mechanized Infantry supported by Artillery"""
    force[SupportedInfantry] = 0
    force[SupportedMechInfantry] = 0
    if force[Artillery] > 0:
        while (force[SupportedInfantry] + force[SupportedMechInfantry]) < force[Artillery] and \
              (force[Infantry] > 0 or force[MechanizedInfantry] > 0):
            if force[Infantry] > 0:
                force[Infantry] -= 1
                force[SupportedInfantry] += 1
            else:
                force[MechanizedInfantry] -= 1
                force[SupportedMechInfantry] += 1


def account_for_supported_tacbombers(force):
    """Take account of Tactical Bombers supported by Fighters or in combined arms with Tanks"""
    force[CombinedArmsTacticalBomber] = 0
    if force[TacticalBomber] > 0:
        while force[TacticalBomber] > 0 and force[CombinedArmsTacticalBomber] < (force[Fighter] + force[Tank]):
            force[TacticalBomber] -= 1
            force[CombinedArmsTacticalBomber] += 1


# Check for submarine sneak attacks and if so remind to roll these manually, first.
if is_sneak_attack(attacking_force, defending_force):
    print("Submarines can sneak attack! Resolve these manually and readjust battle formations.")
    quit()

# Account for combined arms
account_for_supported_infantry(attacking_force)
account_for_supported_tacbombers(attacking_force)

# Roll the battle!
print("---Attacker's rolls---")
total_attack_hits = roll_for_hits(attacking_force, "attacking")

print("\n---Defender's rolls---")
total_defense_hits = roll_for_hits(defending_force, "defending")

print("\n---Totals---")
print("Hits for the attack: {}".format(total_attack_hits))
print("Hits for the defense: {}".format(total_defense_hits))
