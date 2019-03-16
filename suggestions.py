from core import *

def suggestions(colour: str) -> dict:
    alliance = {
        colour : "",
        teams : [

        ],
        suggestions : [
            
        ]
    }

    if not isinstance(colour, str):
        raise TypeError("Alliance colour must be a string")
    colour = colour.lower()
    if colour != "blue" and colour != "red":
        raise ValueError("Alliance colour must be 'blue' or 'red'")

    if colour == "blue":
        teams = [red_team1, red_team2, red_team3]
    else:
        teams = [blue_team1, blue_team2, blue_team3]

    
