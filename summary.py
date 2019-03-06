from openpyxl import load_workbook
import pdb

wb = load_workbook(filename="scouting.xlsx", data_only=True)
ws = wb["Abbreviated NMA"]

red_team1 = ws["A4"]
red_team1_data = {"max_sandstorm_hatch": ws["B4"], 
    "average_sandstorm_hatch": ws["C4"], 
    "max_sandstorm_cargo": ws["D4"], 
    "average_sandstorm_cargo": ws["E4"],
    "max_piece": ws["F4"],
    "max_hatch": ws["G4"],
    "cargo_ship_rocket1_hatch": ws["H4"],
    "higher_level_rocket_hatch": ws["I4"],
    "max_cargo": ws["J4"],
    "cargo_ship_rocket1_cargo": ws["K4"],
    "higher_level_rocket_cargo": ws["L4"],
    "higher_level_rocket_average": (ws["L4"].value + ws["I4"].value)/2,
    "climb": ws["M4"],
    "penalty": ws["N4"]}
red_team1_info = []

if red_team1_data["average_sandstorm_hatch"].value - red_team1_data["average_sandstorm_cargo"].value >= 0.25:
    if red_team1_data["average_sandstorm_hatch"].value == 0:
        pass
    elif red_team1_data["average_sandstorm_hatch"].value <= 0.5:
        red_team1_info.append("Can sometimes do one sandstorm hatch")
    elif red_team1_data["average_sandstorm_hatch"].value <= 0.9:
        red_team1_info.append("Can mostly do one sandstorm hatch")
    elif red_team1_data["average_sandstorm_hatch"].value <= 1.0:
        red_team1_info.append("Can always do one sandstorm hatch")
elif red_team1_data["average_sandstorm_hatch"].value - red_team1_data["average_sandstorm_cargo"].value <= -0.25:
    if red_team1_data["average_sandstorm_cargo"].value == 0:
        pass
    elif red_team1_data["average_sandstorm_cargo"].value <= 0.5:
        red_team1_info.append("Can sometimes do one sandstorm cargo")
    elif red_team1_data["average_sandstorm_cargo"].value <= 0.9:
        red_team1_info.append("Can mostly do one sandstorm cargo")
    elif red_team1_data["average_sandstorm_cargo"].value <= 1.0:
        red_team1_info.append("Can always do one sandstorm cargo")
else:
    if red_team1_data["average_sandstorm_cargo"].value == 0:
        pass
    elif red_team1_data["average_sandstorm_cargo"].value <= 0.5:
        red_team1_info.append("Can sometimes do one sandstorm cargo")
    elif red_team1_data["average_sandstorm_cargo"].value <= 0.9:
        red_team1_info.append("Can mostly do one sandstorm cargo")
    elif red_team1_data["average_sandstorm_cargo"].value <= 1.0:
        red_team1_info.append("Can always do one sandstorm cargo")
    if red_team1_data["average_sandstorm_hatch"].value == 0:
        pass
    elif red_team1_data["average_sandstorm_hatch"].value <= 0.5:
        red_team1_info.append("Can sometimes do one sandstorm hatch")
    elif red_team1_data["average_sandstorm_hatch"].value <= 0.9:
        red_team1_info.append("Can mostly do one sandstorm hatch")
    elif red_team1_data["average_sandstorm_hatch"].value <= 1.0:
        red_team1_info.append("Can always do one sandstorm hatch")
if red_team1_data["average_sandstorm_cargo"].value == 0 and red_team1_data["average_sandstorm_hatch"].value == 0:
        red_team1_info.append("Cannot do sandstorm")
        
if red_team1_data["max_piece"].value >= 4:
    red_team1_info.append("Good gamepiece bot")
    if red_team1_data["max_hatch"].value - red_team1_data["max_cargo"].value > 1:
        red_team1_info.append("Hatch bot")
    elif red_team1_data["max_hatch"].value - red_team1_data["max_cargo"].value < -1:
        red_team1_info.append("Cargo bot")
    else:
        red_team1_info.append("Can do both")
    if red_team1_data["higher_level_rocket_average"] == 0:
        red_team1_info.append("Cannot do higher level rocket")
    elif red_team1_data["higher_level_rocket_average"] <= 1:
        red_team1_info.append("Can somewhat do higher level rocket")
    else:
        red_team1_info.append("Can do higher level rocket")
else:
    red_team1_info.append("Not very good gamepiece bot")

if red_team1_data["climb"].value < 0.85:
    red_team1_info.append("Can't climb to level 1 consistently")
elif red_team1_data["climb"].value <= 1:
    red_team1_info.append("Consistent level 1 climb")
elif red_team1_data["climb"].value <= 1.65:
    red_team1_info.append("Sketchy level 2 climb")
elif red_team1_data["climb"].value <= 2:
    red_team1_info.append("Consistent level 2 climb")
elif red_team1_data["climb"].value <= 2.65:
    red_team1_info.append("Sketchy level 3 climb")
else:
    red_team1_info.append("Consistent level 3 climb")

if red_team1_data["penalty"].value < 1:
    red_team1_info.append("Not very penalty prone")
elif red_team1_data["penalty"].value < 2:
    red_team1_info.append("Be wary of penalties")
else:
    red_team1_info.append("VERY prone to penalties (maybe give copy of manual?)")



red_team2 = ws["A5"]
red_team2_data = {"max_sandstorm_hatch": ws["B5"], 
    "average_sandstorm_hatch": ws["C5"], 
    "max_sandstorm_cargo": ws["D5"], 
    "average_sandstorm_cargo": ws["E5"],
    "max_piece": ws["F5"],
    "max_hatch": ws["G5"],
    "cargo_ship_rocket1_hatch": ws["H5"],
    "higher_level_rocket_hatch": ws["I5"],
    "max_cargo": ws["J5"],
    "cargo_ship_rocket1_cargo": ws["K5"],
    "higher_level_rocket_cargo": ws["L5"],
    "higher_level_rocket_average": (ws["L5"].value + ws["I5"].value)/2,
    "climb": ws["M5"],
    "penalty": ws["N5"]}
red_team2_info = []

if red_team2_data["average_sandstorm_hatch"].value - red_team2_data["average_sandstorm_cargo"].value >= 0.25:
    if red_team2_data["average_sandstorm_hatch"].value == 0:
        pass
    elif red_team2_data["average_sandstorm_hatch"].value <= 0.5:
        red_team2_info.append("Can sometimes do one sandstorm hatch")
    elif red_team2_data["average_sandstorm_hatch"].value <= 0.9:
        red_team2_info.append("Can mostly do one sandstorm hatch")
    elif red_team2_data["average_sandstorm_hatch"].value <= 1.0:
        red_team2_info.append("Can always do one sandstorm hatch")
elif red_team2_data["average_sandstorm_hatch"].value - red_team2_data["average_sandstorm_cargo"].value <= -0.25:
    if red_team2_data["average_sandstorm_cargo"].value == 0:
        pass
    elif red_team2_data["average_sandstorm_cargo"].value <= 0.5:
        red_team2_info.append("Can sometimes do one sandstorm cargo")
    elif red_team2_data["average_sandstorm_cargo"].value <= 0.9:
        red_team2_info.append("Can mostly do one sandstorm cargo")
    elif red_team2_data["average_sandstorm_cargo"].value <= 1.0:
        red_team2_info.append("Can always do one sandstorm cargo")
else:
    if red_team2_data["average_sandstorm_cargo"].value == 0:
        pass
    elif red_team2_data["average_sandstorm_cargo"].value <= 0.5:
        red_team2_info.append("Can sometimes do one sandstorm cargo")
    elif red_team2_data["average_sandstorm_cargo"].value <= 0.9:
        red_team2_info.append("Can mostly do one sandstorm cargo")
    elif red_team2_data["average_sandstorm_cargo"].value <= 1.0:
        red_team2_info.append("Can always do one sandstorm cargo")
    if red_team2_data["average_sandstorm_hatch"].value == 0:
        pass
    elif red_team2_data["average_sandstorm_hatch"].value <= 0.5:
        red_team2_info.append("Can sometimes do one sandstorm hatch")
    elif red_team2_data["average_sandstorm_hatch"].value <= 0.9:
        red_team2_info.append("Can mostly do one sandstorm hatch")
    elif red_team2_data["average_sandstorm_hatch"].value <= 1.0:
        red_team2_info.append("Can always do one sandstorm hatch")
if red_team2_data["average_sandstorm_cargo"].value == 0 and red_team2_data["average_sandstorm_hatch"].value == 0:
        red_team2_info.append("Cannot do sandstorm")

if red_team2_data["max_piece"].value >= 4:
    red_team2_info.append("Good gamepiece bot")
    if red_team2_data["max_hatch"].value - red_team2_data["max_cargo"].value > 1:
        red_team2_info.append("Hatch bot")
    elif red_team2_data["max_hatch"].value - red_team2_data["max_cargo"].value < -1:
        red_team2_info.append("Cargo bot")
    else:
        red_team2_info.append("Can do both")
    if red_team2_data["higher_level_rocket_average"] == 0:
        red_team2_info.append("Cannot do higher level rocket")
    elif red_team2_data["higher_level_rocket_average"] <= 1:
        red_team2_info.append("Can somewhat do higher level rocket")
    else:
        red_team2_info.append("Can do higher level rocket")
else:
    red_team2_info.append("Not very good gamepiece bot")

if red_team2_data["climb"].value < 0.85:
    red_team2_info.append("Can't climb to level 1 consistently")
elif red_team2_data["climb"].value <= 1:
    red_team2_info.append("Consistent level 1 climb")
elif red_team2_data["climb"].value <= 1.65:
    red_team2_info.append("Sketchy level 2 climb")
elif red_team2_data["climb"].value <= 2:
    red_team2_info.append("Consistent level 2 climb")
elif red_team2_data["climb"].value <= 2.65:
    red_team2_info.append("Sketchy level 3 climb")
else:
    red_team2_info.append("Consistent level 3 climb")

if red_team2_data["penalty"].value < 1:
    red_team2_info.append("Not very penalty prone")
elif red_team2_data["penalty"].value < 2:
    red_team2_info.append("Be wary of penalties")
else:
    red_team2_info.append("VERY prone to penalties (maybe give copy of manual?)")



red_team3 = ws["A6"]
red_team3_data = {"max_sandstorm_hatch": ws["B6"], 
    "average_sandstorm_hatch": ws["C6"], 
    "max_sandstorm_cargo": ws["D6"], 
    "average_sandstorm_cargo": ws["E6"],
    "max_piece": ws["F6"],
    "max_hatch": ws["G6"],
    "cargo_ship_rocket1_hatch": ws["H6"],
    "higher_level_rocket_hatch": ws["I6"],
    "max_cargo": ws["J6"],
    "cargo_ship_rocket1_cargo": ws["K6"],
    "higher_level_rocket_cargo": ws["L6"],
    "higher_level_rocket_average": (ws["L6"].value + ws["I6"].value)/2,
    "climb": ws["M6"],
    "penalty": ws["N6"]}
red_team3_info = []

if red_team3_data["average_sandstorm_hatch"].value - red_team3_data["average_sandstorm_cargo"].value >= 0.25:
    if red_team3_data["average_sandstorm_hatch"].value == 0:
        pass
    elif red_team3_data["average_sandstorm_hatch"].value <= 0.5:
        red_team3_info.append("Can sometimes do one sandstorm hatch")
    elif red_team3_data["average_sandstorm_hatch"].value <= 0.9:
        red_team3_info.append("Can mostly do one sandstorm hatch")
    elif red_team3_data["average_sandstorm_hatch"].value <= 1.0:
        red_team3_info.append("Can always do one sandstorm hatch")
elif red_team3_data["average_sandstorm_hatch"].value - red_team3_data["average_sandstorm_cargo"].value <= -0.25:
    if red_team3_data["average_sandstorm_cargo"].value == 0:
        pass
    elif red_team3_data["average_sandstorm_cargo"].value <= 0.5:
        red_team3_info.append("Can sometimes do one sandstorm cargo")
    elif red_team3_data["average_sandstorm_cargo"].value <= 0.9:
        red_team3_info.append("Can mostly do one sandstorm cargo")
    elif red_team3_data["average_sandstorm_cargo"].value <= 1.0:
        red_team3_info.append("Can always do one sandstorm cargo")
else:
    if red_team3_data["average_sandstorm_cargo"].value == 0:
        pass
    elif red_team3_data["average_sandstorm_cargo"].value <= 0.5:
        red_team3_info.append("Can sometimes do one sandstorm cargo")
    elif red_team3_data["average_sandstorm_cargo"].value <= 0.9:
        red_team3_info.append("Can mostly do one sandstorm cargo")
    elif red_team3_data["average_sandstorm_cargo"].value <= 1.0:
        red_team3_info.append("Can always do one sandstorm cargo")
    if red_team3_data["average_sandstorm_hatch"].value == 0:
        pass
    elif red_team3_data["average_sandstorm_hatch"].value <= 0.5:
        red_team3_info.append("Can sometimes do one sandstorm hatch")
    elif red_team3_data["average_sandstorm_hatch"].value <= 0.9:
        red_team3_info.append("Can mostly do one sandstorm hatch")
    elif red_team3_data["average_sandstorm_hatch"].value <= 1.0:
        red_team3_info.append("Can always do one sandstorm hatch")
if red_team3_data["average_sandstorm_cargo"].value == 0 and red_team3_data["average_sandstorm_hatch"].value == 0:
        red_team3_info.append("Cannot do sandstorm")

if red_team3_data["max_piece"].value >= 4:
    red_team3_info.append("Good gamepiece bot")
    if red_team3_data["max_hatch"].value - red_team3_data["max_cargo"].value > 1:
        red_team3_info.append("Hatch bot")
    elif red_team3_data["max_hatch"].value - red_team3_data["max_cargo"].value < -1:
        red_team3_info.append("Cargo bot")
    else:
        red_team3_info.append("Can do both")
    if red_team3_data["higher_level_rocket_average"] == 0:
        red_team3_info.append("Cannot do higher level rocket")
    elif red_team3_data["higher_level_rocket_average"] <= 1:
        red_team3_info.append("Can somewhat do higher level rocket")
    else:
        red_team3_info.append("Can do higher level rocket")
else:
    red_team3_info.append("Not very good gamepiece bot")

if red_team3_data["climb"].value < 0.85:
    red_team3_info.append("Can't climb to level 1 consistently")
elif red_team3_data["climb"].value <= 1:
    red_team3_info.append("Consistent level 1 climb")
elif red_team3_data["climb"].value <= 1.65:
    red_team3_info.append("Sketchy level 2 climb")
elif red_team3_data["climb"].value <= 2:
    red_team3_info.append("Consistent level 2 climb")
elif red_team3_data["climb"].value <= 2.65:
    red_team3_info.append("Sketchy level 3 climb")
else:
    red_team3_info.append("Consistent level 3 climb")

if red_team3_data["penalty"].value < 1:
    red_team3_info.append("Not very penalty prone")
elif red_team3_data["penalty"].value < 2:
    red_team3_info.append("Be wary of penalties")
else:
    red_team3_info.append("VERY prone to penalties (maybe give copy of manual?)")



blue_team1 = ws["A8"]
blue_team1_data = {"max_sandstorm_hatch": ws["B8"], 
    "average_sandstorm_hatch": ws["C8"], 
    "max_sandstorm_cargo": ws["D8"], 
    "average_sandstorm_cargo": ws["E8"],
    "max_piece": ws["F8"],
    "max_hatch": ws["G8"],
    "cargo_ship_rocket1_hatch": ws["H8"],
    "higher_level_rocket_hatch": ws["I8"],
    "max_cargo": ws["J8"],
    "cargo_ship_rocket1_cargo": ws["K8"],
    "higher_level_rocket_cargo": ws["L8"],
    "higher_level_rocket_average": (ws["L8"].value + ws["I8"].value)/2,
    "climb": ws["M8"],
    "penalty": ws["N8"]}
blue_team1_info = []

if blue_team1_data["average_sandstorm_hatch"].value - blue_team1_data["average_sandstorm_cargo"].value >= 0.25:
    if blue_team1_data["average_sandstorm_hatch"].value == 0:
        pass
    elif blue_team1_data["average_sandstorm_hatch"].value <= 0.5:
        blue_team1_info.append("Can sometimes do one sandstorm hatch")
    elif blue_team1_data["average_sandstorm_hatch"].value <= 0.9:
        blue_team1_info.append("Can mostly do one sandstorm hatch")
    elif blue_team1_data["average_sandstorm_hatch"].value <= 1.0:
        blue_team1_info.append("Can always do one sandstorm hatch")
elif blue_team1_data["average_sandstorm_hatch"].value - blue_team1_data["average_sandstorm_cargo"].value <= -0.25:
    if blue_team1_data["average_sandstorm_cargo"].value == 0:
        pass
    elif blue_team1_data["average_sandstorm_cargo"].value <= 0.5:
        blue_team1_info.append("Can sometimes do one sandstorm cargo")
    elif blue_team1_data["average_sandstorm_cargo"].value <= 0.9:
        blue_team1_info.append("Can mostly do one sandstorm cargo")
    elif blue_team1_data["average_sandstorm_cargo"].value <= 1.0:
        blue_team1_info.append("Can always do one sandstorm cargo")
else:
    if blue_team1_data["average_sandstorm_cargo"].value == 0:
        pass
    elif blue_team1_data["average_sandstorm_cargo"].value <= 0.5:
        blue_team1_info.append("Can sometimes do one sandstorm cargo")
    elif blue_team1_data["average_sandstorm_cargo"].value <= 0.9:
        blue_team1_info.append("Can mostly do one sandstorm cargo")
    elif blue_team1_data["average_sandstorm_cargo"].value <= 1.0:
        blue_team1_info.append("Can always do one sandstorm cargo")
    if blue_team1_data["average_sandstorm_hatch"].value == 0:
        pass
    elif blue_team1_data["average_sandstorm_hatch"].value <= 0.5:
        blue_team1_info.append("Can sometimes do one sandstorm hatch")
    elif blue_team1_data["average_sandstorm_hatch"].value <= 0.9:
        blue_team1_info.append("Can mostly do one sandstorm hatch")
    elif blue_team1_data["average_sandstorm_hatch"].value <= 1.0:
        blue_team1_info.append("Can always do one sandstorm hatch")
if blue_team1_data["average_sandstorm_cargo"].value == 0 and blue_team1_data["average_sandstorm_hatch"].value == 0:
        blue_team1_info.append("Cannot do sandstorm")

if blue_team1_data["max_piece"].value >= 4:
    blue_team1_info.append("Good gamepiece bot")
    if blue_team1_data["max_hatch"].value - blue_team1_data["max_cargo"].value > 1:
        blue_team1_info.append("Hatch bot")
    elif blue_team1_data["max_hatch"].value - blue_team1_data["max_cargo"].value < -1:
        blue_team1_info.append("Cargo bot")
    else:
        blue_team1_info.append("Can do both")
    if blue_team1_data["higher_level_rocket_average"] == 0:
        blue_team1_info.append("Cannot do higher level rocket")
    elif blue_team1_data["higher_level_rocket_average"] <= 1:
        blue_team1_info.append("Can somewhat do higher level rocket")
    else:
        blue_team1_info.append("Can do higher level rocket")
else:
    blue_team1_info.append("Not very good gamepiece bot")

if blue_team1_data["climb"].value < 0.85:
    blue_team1_info.append("Can't climb to level 1 consistently")
elif blue_team1_data["climb"].value <= 1:
    blue_team1_info.append("Consistent level 1 climb")
elif blue_team1_data["climb"].value <= 1.65:
    blue_team1_info.append("Sketchy level 2 climb")
elif blue_team1_data["climb"].value <= 2:
    blue_team1_info.append("Consistent level 2 climb")
elif blue_team1_data["climb"].value <= 2.65:
    blue_team1_info.append("Sketchy level 3 climb")
else:
    blue_team1_info.append("Consistent level 3 climb")

if blue_team1_data["penalty"].value < 1:
    blue_team1_info.append("Not very penalty prone")
elif blue_team1_data["penalty"].value < 2:
    blue_team1_info.append("Be wary of penalties")
else:
    blue_team1_info.append("VERY prone to penalties (maybe give copy of manual?)")



blue_team2 = ws["A9"]
blue_team2_data = {"max_sandstorm_hatch": ws["B9"], 
    "average_sandstorm_hatch": ws["C9"], 
    "max_sandstorm_cargo": ws["D9"], 
    "average_sandstorm_cargo": ws["E9"],
    "max_piece": ws["F9"],
    "max_hatch": ws["G9"],
    "cargo_ship_rocket1_hatch": ws["H9"],
    "higher_level_rocket_hatch": ws["I9"],
    "max_cargo": ws["J9"],
    "cargo_ship_rocket1_cargo": ws["K9"],
    "higher_level_rocket_cargo": ws["L9"],
    "higher_level_rocket_average": (ws["L9"].value + ws["I9"].value)/2,
    "climb": ws["M9"],
    "penalty": ws["N9"]}
blue_team2_info = []

if blue_team2_data["average_sandstorm_hatch"].value - blue_team2_data["average_sandstorm_cargo"].value >= 0.25:
    if blue_team2_data["average_sandstorm_hatch"].value == 0:
        pass
    elif blue_team2_data["average_sandstorm_hatch"].value <= 0.5:
        blue_team2_info.append("Can sometimes do one sandstorm hatch")
    elif blue_team2_data["average_sandstorm_hatch"].value <= 0.9:
        blue_team2_info.append("Can mostly do one sandstorm hatch")
    elif blue_team2_data["average_sandstorm_hatch"].value <= 1.0:
        blue_team2_info.append("Can always do one sandstorm hatch")
elif blue_team2_data["average_sandstorm_hatch"].value - blue_team2_data["average_sandstorm_cargo"].value <= -0.25:
    if blue_team2_data["average_sandstorm_cargo"].value == 0:
        pass
    elif blue_team2_data["average_sandstorm_cargo"].value <= 0.5:
        blue_team2_info.append("Can sometimes do one sandstorm cargo")
    elif blue_team2_data["average_sandstorm_cargo"].value <= 0.9:
        blue_team2_info.append("Can mostly do one sandstorm cargo")
    elif blue_team2_data["average_sandstorm_cargo"].value <= 1.0:
        blue_team2_info.append("Can always do one sandstorm cargo")
else:
    if blue_team2_data["average_sandstorm_cargo"].value == 0:
        pass
    elif blue_team2_data["average_sandstorm_cargo"].value <= 0.5:
        blue_team2_info.append("Can sometimes do one sandstorm cargo")
    elif blue_team2_data["average_sandstorm_cargo"].value <= 0.9:
        blue_team2_info.append("Can mostly do one sandstorm cargo")
    elif blue_team2_data["average_sandstorm_cargo"].value <= 1.0:
        blue_team2_info.append("Can always do one sandstorm cargo")
    if blue_team2_data["average_sandstorm_hatch"].value == 0:
        pass
    elif blue_team2_data["average_sandstorm_hatch"].value <= 0.5:
        blue_team2_info.append("Can sometimes do one sandstorm hatch")
    elif blue_team2_data["average_sandstorm_hatch"].value <= 0.9:
        blue_team2_info.append("Can mostly do one sandstorm hatch")
    elif blue_team2_data["average_sandstorm_hatch"].value <= 1.0:
        blue_team2_info.append("Can always do one sandstorm hatch")
if blue_team2_data["average_sandstorm_cargo"].value == 0 and blue_team2_data["average_sandstorm_hatch"].value == 0:
        blue_team2_info.append("Cannot do sandstorm")

if blue_team2_data["max_piece"].value >= 4:
    blue_team2_info.append("Good gamepiece bot")
    if blue_team2_data["max_hatch"].value - blue_team2_data["max_cargo"].value > 1:
        blue_team2_info.append("Hatch bot")
    elif blue_team2_data["max_hatch"].value - blue_team2_data["max_cargo"].value < -1:
        blue_team2_info.append("Cargo bot")
    else:
        blue_team2_info.append("Can do both")
    if blue_team2_data["higher_level_rocket_average"] == 0:
        blue_team2_info.append("Cannot do higher level rocket")
    elif blue_team2_data["higher_level_rocket_average"] <= 1:
        blue_team2_info.append("Can somewhat do higher level rocket")
    else:
        blue_team2_info.append("Can do higher level rocket")
else:
    blue_team2_info.append("Not very good gamepiece bot")

if blue_team2_data["climb"].value < 0.85:
    blue_team2_info.append("Can't climb to level 1 consistently")
elif blue_team2_data["climb"].value <= 1:
    blue_team2_info.append("Consistent level 1 climb")
elif blue_team2_data["climb"].value <= 1.65:
    blue_team2_info.append("Sketchy level 2 climb")
elif blue_team2_data["climb"].value <= 2:
    blue_team2_info.append("Consistent level 2 climb")
elif blue_team2_data["climb"].value <= 2.65:
    blue_team2_info.append("Sketchy level 3 climb")
else:
    blue_team2_info.append("Consistent level 3 climb")

if blue_team2_data["penalty"].value < 1:
    blue_team2_info.append("Not very penalty prone")
elif blue_team2_data["penalty"].value < 2:
    blue_team2_info.append("Be wary of penalties")
else:
    blue_team2_info.append("VERY prone to penalties (maybe give copy of manual?)")



blue_team3 = ws["A10"]
blue_team3_data = {"max_sandstorm_hatch": ws["B10"], 
    "average_sandstorm_hatch": ws["C10"], 
    "max_sandstorm_cargo": ws["D10"], 
    "average_sandstorm_cargo": ws["E10"],
    "max_piece": ws["F10"],
    "max_hatch": ws["G10"],
    "cargo_ship_rocket1_hatch": ws["H10"],
    "higher_level_rocket_hatch": ws["I10"],
    "max_cargo": ws["J10"],
    "cargo_ship_rocket1_cargo": ws["K10"],
    "higher_level_rocket_cargo": ws["L10"],
    "higher_level_rocket_average": (ws["L10"].value + ws["I10"].value)/2,
    "climb": ws["M10"],
    "penalty": ws["N10"]}
blue_team3_info = []

if blue_team3_data["average_sandstorm_hatch"].value - blue_team3_data["average_sandstorm_cargo"].value >= 0.25:
    if blue_team3_data["average_sandstorm_hatch"].value == 0:
        pass
    elif blue_team3_data["average_sandstorm_hatch"].value <= 0.5:
        blue_team3_info.append("Can sometimes do one sandstorm hatch")
    elif blue_team3_data["average_sandstorm_hatch"].value <= 0.9:
        blue_team3_info.append("Can mostly do one sandstorm hatch")
    elif blue_team3_data["average_sandstorm_hatch"].value <= 1.0:
        blue_team3_info.append("Can always do one sandstorm hatch")
elif blue_team3_data["average_sandstorm_hatch"].value - blue_team3_data["average_sandstorm_cargo"].value <= -0.25:
    if blue_team3_data["average_sandstorm_cargo"].value == 0:
        pass
    elif blue_team3_data["average_sandstorm_cargo"].value <= 0.5:
        blue_team3_info.append("Can sometimes do one sandstorm cargo")
    elif blue_team3_data["average_sandstorm_cargo"].value <= 0.9:
        blue_team3_info.append("Can mostly do one sandstorm cargo")
    elif blue_team3_data["average_sandstorm_cargo"].value <= 1.0:
        blue_team3_info.append("Can always do one sandstorm cargo")
else:
    if blue_team3_data["average_sandstorm_cargo"].value == 0:
        pass
    elif blue_team3_data["average_sandstorm_cargo"].value <= 0.5:
        blue_team3_info.append("Can sometimes do one sandstorm cargo")
    elif blue_team3_data["average_sandstorm_cargo"].value <= 0.9:
        blue_team3_info.append("Can mostly do one sandstorm cargo")
    elif blue_team3_data["average_sandstorm_cargo"].value <= 1.0:
        blue_team3_info.append("Can always do one sandstorm cargo")
    if blue_team3_data["average_sandstorm_hatch"].value == 0:
        pass
    elif blue_team3_data["average_sandstorm_hatch"].value <= 0.5:
        blue_team3_info.append("Can sometimes do one sandstorm hatch")
    elif blue_team3_data["average_sandstorm_hatch"].value <= 0.9:
        blue_team3_info.append("Can mostly do one sandstorm hatch")
    elif blue_team3_data["average_sandstorm_hatch"].value <= 1.0:
        blue_team3_info.append("Can always do one sandstorm hatch")
if blue_team3_data["average_sandstorm_cargo"].value == 0 and blue_team3_data["average_sandstorm_hatch"].value == 0:
        blue_team3_info.append("Cannot do sandstorm")

if blue_team3_data["max_piece"].value >= 4:
    blue_team3_info.append("Good gamepiece bot")
    if blue_team3_data["max_hatch"].value - blue_team3_data["max_cargo"].value > 1:
        blue_team3_info.append("Hatch bot")
    elif blue_team3_data["max_hatch"].value - blue_team3_data["max_cargo"].value < -1:
        blue_team3_info.append("Cargo bot")
    else:
        blue_team3_info.append("Can do both")
    if blue_team3_data["higher_level_rocket_average"] == 0:
        blue_team3_info.append("Cannot do higher level rocket")
    elif blue_team3_data["higher_level_rocket_average"] <= 1:
        blue_team3_info.append("Can somewhat do higher level rocket")
    else:
        blue_team3_info.append("Can do higher level rocket")
else:
    blue_team3_info.append("Not very good gamepiece bot")

if blue_team3_data["climb"].value < 0.85:
    blue_team3_info.append("Can't climb to level 1 consistently")
elif blue_team3_data["climb"].value <= 1:
    blue_team3_info.append("Consistent level 1 climb")
elif blue_team3_data["climb"].value <= 1.65:
    blue_team3_info.append("Sketchy level 2 climb")
elif blue_team3_data["climb"].value <= 2:
    blue_team3_info.append("Consistent level 2 climb")
elif blue_team3_data["climb"].value <= 2.65:
    blue_team3_info.append("Sketchy level 3 climb")
else:
    blue_team3_info.append("Consistent level 3 climb")

if blue_team3_data["penalty"].value < 1:
    blue_team3_info.append("Not very penalty prone")
elif blue_team3_data["penalty"].value < 2:
    blue_team3_info.append("Be wary of penalties")
else:
    blue_team3_info.append("VERY prone to penalties (maybe give copy of manual?)")


print(red_team1.value)
for info in red_team1_info:
    print(info)
print(red_team2.value)
for info in red_team2_info:
    print(info)
print(red_team3.value)
for info in red_team3_info:
    print(info)
print(blue_team1.value)
for info in blue_team1_info:
    print(info)
print(blue_team2.value)
for info in blue_team2_info:
    print(info)
print(blue_team3.value)
for info in blue_team3_info:
    print(info)