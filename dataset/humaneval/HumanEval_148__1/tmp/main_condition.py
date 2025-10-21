from typing import *


def bf(planet1, planet2):
    planet_names = (
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune")
    print(f'[ITE][LOC]13[/LOC][VAR]planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2[/VAR][VAL]{planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2}[/VAL][/ITE]')
    print(f'[ITE][LOC]13[/LOC][VAR]planet1 == planet2[/VAR][VAL]{planet1 == planet2}[/VAL][/ITE]')
    print(f'[ITE][LOC]13[/LOC][VAR]planet1 not in planet_names[/VAR][VAL]{planet1 not in planet_names}[/VAL][/ITE]')
    print(f'[ITE][LOC]13[/LOC][VAR]planet2 not in planet_names[/VAR][VAL]{planet2 not in planet_names}[/VAL][/ITE]')
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    print(f'[ITE][LOC]17[/LOC][VAR]planet1_index < planet2_index[/VAR][VAL]{planet1_index < planet2_index}[/VAL][/ITE]')
    if planet1_index < planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1: planet1_index])

bf("Mercury", "Uranus")