def bf(planet1, planet2):
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupyter", "Saturn", "Uranus", "Neptune")
    print('[LINE]2[/LINE] may be hit')
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        print('[LINE]2[/LINE] is hit')
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    print('[LINE]6[/LINE] may be hit')
    print('[LINE]8[/LINE] may be hit')
    if planet1_index < planet2_index:
        print('[LINE]6[/LINE] is hit')
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        print('[LINE]8[/LINE] is hit')
        return (planet_names[planet2_index + 1 : planet1_index])

bf('Mercury', 'Uranus')