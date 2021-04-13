"""
Random assignment of registered students to available use cases.
2021 Master Studies in "Business Analytics" at HSD University of Applied Science (Düsseldorf, Germany)
Author: Thomas Zeutschler
"""
import random

process = "Results for random assignment of students to use cases in 'Business Analytics A', summer 2021"

students = ["Bennett Glasscock", "Josefa Garay", "Jordan Farnham", "Merlin Hillis", "Klara Yoder",
            "Julietta Solari", "Shayla Talarico", "Santina Jawad", "Lance Dieckman", "Delfina Crutchfield",
            "Marth Baer", "Miguelina Marietta", "Roxie Mccracken", "Michelina Girardin", "Thomas Herold",
            "Donetta Heenan", "Joslyn Rimes", "Lolita Mccray", "Vertie Loomis", "Jeraldine Harrison"]

use_cases = ["001-earthquake", "002-podcast", "003-plane-crash", "004-twitter-sentiment",
             "005-twitter-followers", "006-employee-attrition", "007-parquet-viewer", "008-timeseries-forecasting",
             "009-personal-alexa", "010-snoring-tracker"]


def main():
    min_team_size = 2
    max_team_size = 3
    target_team_size = 3
    min_teams_count = int(len(students) / max_team_size)

    if min_teams_count > len(use_cases):
        print(f"Error: {len(use_cases)} available use cases are not enough "
              f"for {len(students)} students at a max. team size of {max_team_size} students.")
        return

    # shuffle student and team lists
    random.seed()
    random.shuffle(students)
    random.shuffle(use_cases)

    # assign students to teams
    teams = []
    team = {}
    current_team_size = 0
    while students:
        if current_team_size == 0:
            use_case = use_cases.pop()
            team = {"use case": use_case, "students": []}
        student = students.pop()
        team["students"].append(student)
        current_team_size += 1
        if current_team_size >= target_team_size:
            teams.append(team)
            team = {}
            current_team_size = 0

    # append remaining team (if such exists)
    if team:
        teams.append(team)

        # reallocate students to fill up the last team (if required)
        last_team = len(teams) - 1
        prev_team = last_team - 1
        while len(teams[last_team]["students"]) < min_team_size:
            teams[last_team]["students"].append(teams[prev_team]["students"].pop())
            prev_team -= 1

    # sort teams and students within teams for better readability of results
    teams.sort(key=lambda k: k['use case'])
    for team in teams:
        team["students"].sort()

    # print results
    print("*" * len(process))
    print(f"{process}")
    print("*" * len(process))
    for team in teams:
        print(f"use case: {team['use case']}")
        for index, student in enumerate(team["students"]):
            print(f"\t{index + 1}. {student}")


if __name__ == "__main__":
    main()
