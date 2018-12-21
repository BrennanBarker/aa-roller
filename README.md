# aa-roller
A battle simulator for a popular boardgame.  This is meant to reduce the headache and mess of manually rolling many dice per round of combat.

This is callibrated to 1940, Second Edition; you may need to adjust unit stats and battle proceedings if playing a different version.

#### "Installation":
Simply drop the three .py files into a single directory on your computer.  The only external python package dependancy is `random.py`, which is part of the Python Standard Library.  This was written for Python 3.5, YMMV with other versions.

#### Usage:

1) Roll manually for any submarine surprise attacks.  Roll manually for AAA fires, provided this is the first round of an engagement (AAA's fire only once for an entire engagement, sneak attacking submarines get to fire every round).

2) Update `battle_formations.py` with the numbers of units of each type, on each side (after removing any units hit by sneaky subs or AAA).
  a) Only include submarines if the opposing side has a destroyer.  Sneak attacking subs should be rolled first, seperately, manually, becuase their kills are removed from the board prior to general combat roll and these submarines do not participate in general combat.
  b) Only include battleships and cruisers in the first round of an amphibius invasion if rolling a naval bombardment.
  c) Infantry and mechanized infantry supported by artillery, and tactical bombers working with tanks or fighters will be accounted for and their attacking stat boosted appropriately.

3) Run `python3 simulation.py` from the directory where you saved the .py files. Take note of hits for the attack and defense. A breakdown of each unit's roll is provided for a more detailed view of what happened.

4) Remove units (or take damage on aircraft carriers and/or battleships) from the board on each side as appropriate.

5) Repeat from Step 1.

#### I hope this makes your gaming more fun.  If it has, would you consider [donating me a cup of coffee](https://www.paypal.me/brennanbarker)?
