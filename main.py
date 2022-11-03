# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'):
    joined_phrase = greeting[0:greeting.find('<')] + \
        name + greeting[greeting.find('>')+1:]
    return joined_phrase


def force(mass, body='earth'):
    gravity_of_body = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    if body.lower() in gravity_of_body:
        result = mass * gravity_of_body[body.lower()]
        return round(result, 1)
    else:
        return 'No available data for this body.'


def pull(mass1, mass2, distance):
    mass_part = (mass1 * mass2)/(distance * distance)
    gravitational_constant = 6.674*(10**-11)
    result = mass_part * gravitational_constant
    return result
