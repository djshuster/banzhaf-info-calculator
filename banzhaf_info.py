# Created by David Shuster
# Last updated 14 Dec., 2020

# This program takes in data from electionData.csv
# and outputs the "Ratio of Banzhaf Index to Fraction of Vote" for each party in results.csv.
# The default quota is 61. To use a different quota,
# enter the new quota as a whole number in the command line when running the program.
# For example "py banzhaf_info.py 90" will set the quota to 90.
# For more detailed information, check out README.txt.

import coalitions
import csv
import sys

def main():
    parties={}
    if (len(sys.argv)==2):
        quota = int(sys.argv[1])
    else:
        quota = 61

    # 1 argument: returns True if the seat count for the list of party-lists sums up to or past the quota.
    # 3 arguments: If removing=True and removed has a value, then removed holds the name of the removed party;
    # then return false if and only if the party-lists' seats cannot sum to 61 without the removed party.
    # In other words, if this latter use scenario returns false, then the removed party is a critical voter.
    def majority(name_list, removing=False, removed=""):
        sum = 0
        for name in name_list:
            sum += int(parties[name]["seats"])
        if(removing and removed!=""):
            sum-= int(parties[removed]["seats"])
        return (sum>=quota)

    # import information from electionData.csv
    with open('electionData.csv') as myFile:
        data = csv.reader(myFile, delimiter=',')
        for row in data:
            if (row[0]==""):
                break
            if (row[0]=="Name of list"):
                continue
            party_info={}
            party_info["fraction_of_vote"] = float(row[2])/100
            party_info["seats"] = row[3]
            party_info["Bpower"] = 0
            party_info["Bindex"] = 0
            parties[row[0]] = party_info
        names = parties.keys()
        coalition_list = coalitions.list_of_lists(list(names))

    # establish the Banzhaf power of each coalition
    for coalition in coalition_list:
        if majority(coalition):
            for party in coalition:
                if(not majority(coalition, removing=True, removed=party)):
                    parties[party]["Bpower"] +=1

    # find the total Banzhaf power
    total_Bpower = 0
    for name in names:
        total_Bpower+=parties[name]["Bpower"]

    # write the results into results.csv
    with open('results.csv', 'w', newline='') as csvfile:
        field1 = 'Knesset Elected List Names'
        field2 = 'Ratio of Banzhaf Index to Fraction of Vote'
        writer = csv.DictWriter(csvfile, fieldnames=[field1, field2])
        writer.writeheader()
        for name in names:
            parties[name]["Bindex"] = parties[name]["Bpower"] / total_Bpower
            ratio = round(parties[name]["Bindex"] / parties[name]["fraction_of_vote"], 2)
            writer.writerow({field1: name, field2: ratio})
            print(name, "has a Banzhaf index/(fraction of vote) ratio of ", ratio)

if __name__ == '__main__':
    main()