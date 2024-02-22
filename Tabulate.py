from tabulate import tabulate
table={
    "Pokemon_Name": ["Pikachu","Squirtle","Charmander"],
    "Type": ["electric","Water","Fire"]
}
print(tabulate(table,headers="keys",tablefmt="fancy_grid",showindex="always"))


table=[
    ["Pokemon_Name","Type"],
    ["Pikachu","electric"],
    ["Squirtle","Water"],
    ["Charmander","Fire"]
       ]
print(tabulate(table,headers="firstrow",tablefmt="psql",showindex="always"))
