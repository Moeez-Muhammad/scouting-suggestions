from core import *
from summary import *
import pprint

def suggestions(colour: str) -> dict:
    alliance = {
        'colour' : "",
        'teams' : {
            'team1' : {},
            'team2' : {},
            'team3' : {}
        },
        'suggestions' : [
            
        ]
    }

    if not isinstance(colour, str):
        raise TypeError("Alliance colour must be a string")
    colour = colour.lower()
    if colour != "blue" and colour != "red":
        raise ValueError("Alliance colour must be 'blue' or 'red'")
    alliance['colour'] = colour
    if colour == "blue":
        alliance['teams']['team1'] = summary(red_team1)
        alliance['teams']['team2'] = summary(red_team2)
        alliance['teams']['team3'] = summary(red_team3)
    else:
        alliance['teams']['team1'] = summary(blue_team1)
        alliance['teams']['team2'] = summary(blue_team2)
        alliance['teams']['team3'] = summary(blue_team3)





    return alliance
