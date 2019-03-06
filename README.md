# scouting-suggestions
A python proof of concept for displaying a summary and suggestions of data in FRC scouting

This is will be eventually ported to Excel, so you don't have to save, alt-tab, run python program, and then look at the results. This is just a proof of concept since python's a lot easier to work with than Excel

Currently, this only shows an outline, not suggestions. Those are harder to write concrete rules for, so those will come later.

## Getting Started
You need the module ```openpyxl```; install from pip  
You also need the scouting database in the same folder as the program, named 'scouting.xlsx' (helpfully provided with the repo!)

## How to Use
1. Go to Abbreviated NMA
2. Enter match number
3. Save file
4. Run python program

Because python cannot evaluate formulas, saving the file is necessary as Excel saves a temporary copy of the data itself, not the formulas, in the .xlsx, which python can read.

## TODO
- Add logic flow chart for summary
