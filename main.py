# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    collbb = pd.read_json('coll bb_SortByConf.json')
    print(collbb[0:100], '\n')
    print("There are " + str(len(collbb)) + " teams")
    print("\n")
    VATeams = collbb[collbb['state'] == "VA"]
    print("There are " + str(len(VATeams)) + " teams in the state of Virginia, and UVA is the best one")
    mascotCount = collbb['name'].value_counts()
    mascotCountDups = mascotCount[mascotCount > 1]
    print("\n")
    print("The list of mascots and the number of times they are duplicated is below:")
    print()
    print(mascotCountDups)

# sources
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html
