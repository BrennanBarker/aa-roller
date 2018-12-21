from units import *

attacking_force = {
    Infantry: 0,
    Artillery: 0,
    MechanizedInfantry: 0,
    Tank: 0,
    Fighter: 0,
    TacticalBomber: 0,
    StrategicBomber: 0,
    Submarine: 0,  # Only if involved in the battle; roll sneak attacks first!
    Destroyer: 0,
    Cruiser: 0,
    Battleship: 0,  # Include damaged battleships
    # Aircraft carriers have no attack value
}

defending_force = {
    Infantry: 0,
    Artillery: 0,
    MechanizedInfantry: 0,
    Tank: 0,
    Fighter: 0,
    TacticalBomber: 0,
    StrategicBomber: 0,
    Submarine: 0,  # Only if involved in the battle; roll sneak attacks first!
    Destroyer: 0,
    Cruiser: 0,
    Battleship: 0,
    AircraftCarrier: 0,
}
