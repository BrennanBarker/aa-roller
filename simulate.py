from units import *
from battle_formations import attacking_force, defending_force

# TODO remind people to look for AAA fires
# TODO remind that aircraft can't hit subs without a destroyer present

# If a submarine sneak attack is possible, raise an error to ask to resolve manually
if attacking_force[Submarine] > 0 and defending_force[Destroyer] == 0:
    raise Exception("Attacking submarines can sneak attack! Resolve these manually and readjust battle formations.")
if defending_force[Submarine] > 0 and attacking_force[Destroyer] == 0:
    raise Exception("Defending submarines can sneak attack! Resolve these manually and readjust battle formations.")


# Take account of Infantry or Mechanized Infantry supported by Artillery
attacking_force[SupportedInfantry] = 0
attacking_force[SupportedMechInfantry] = 0
if attacking_force[Artillery] > 0:
    while attacking_force[SupportedInfantry] < attacking_force[Artillery] and \
         (attacking_force[Infantry] > 0 or attacking_force[MechanizedInfantry] > 0):
        if attacking_force[Infantry] > 0:
            attacking_force[Infantry] -= 1
            attacking_force[SupportedInfantry] += 1
        else:
            attacking_force[MechanizedInfantry] -= 1
            attacking_force[SupportedMechInfantry] += 1

# Take account of Tactical Bombers supported by Fighters or in combined arms with Tanks
attacking_force[CombinedArmsTacticalBomber] = 0
if attacking_force[TacticalBomber] > 0:
    while attacking_force[TacticalBomber] > 0 and \
          attacking_force[CombinedArmsTacticalBomber] < (attacking_force[Fighter] + attacking_force[Tank]):
        attacking_force[TacticalBomber] -= 1
        attacking_force[CombinedArmsTacticalBomber] += 1


# Roll the battle!
print("---Attacker's rolls---")
total_attack_hits = 0
for unit_type in attacking_force:
    for roll in range(0, attacking_force[unit_type]):
        unit = unit_type()
        if unit.attack() == "hit":
            total_attack_hits += 1

print("\n---Defender's rolls---")
total_defense_hits = 0
for unit_type in defending_force:
    for roll in range(0, defending_force[unit_type]):
        unit = unit_type()
        if unit.defend() == "hit":
            total_defense_hits += 1

print("\n---Totals---")
print("Hits for the attack: {}".format(total_attack_hits))
print("Hits for the defense: {}".format(total_defense_hits))
