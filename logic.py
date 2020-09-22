import random
from itertools import combinations


def spielplan_doppel(rounds, gruppe_a, gruppe_b):
    group_a = gruppe_a
    group_b = gruppe_b

    if not len(group_a) == len(group_b):
        group_b.append(0)

    teams = []
    plan = []
    current_order = []
    current_aussetzer = []
    current_einzel = []

    for round in range(rounds):
        for player_a in group_a:
            teams.append([player_a, group_b[group_a.index(player_a)]])

        group_b.append(group_b.pop(0))

        random.shuffle(teams)
        for t in teams:
            if 0 in t:
                current_aussetzer = list(t)

                current_aussetzer.remove(0)

                teams.remove(t)

        for t in range(len(teams)):
            if t % 2 == 0:
                if not t == len(teams) - 1:
                    current_order.append([teams[t][0], teams[t][1], teams[t + 1][0], teams[t + 1][1]])
                else:
                    current_einzel = teams[t]

        plan.append([list(current_order), [current_einzel], current_aussetzer, [round + 1]])
        current_order = []
        teams = []

    return plan


def jeder_gegen_jeden(player_list):
    matchplan = spielplan_einzel(player_list)

    plan = []
    current_aussetzer = []
    for round in matchplan:
        for match in round:
            if 0 in match:
                current_aussetzer = list(match)
                current_aussetzer.remove(0)
                round.remove(match)
        plan.append([[], round, current_aussetzer, [matchplan.index(round) + 1]])

    return plan


def runden_einzel(player_list, rounds):
    matchplan = spielplan_einzel(player_list)
    plan = []
    temp_round = []
    current_aussetzer = []
    for i in range(int(rounds)):
        temp_round = list(matchplan[0])
        for match in matchplan[0]:
            if 0 in match:
                current_aussetzer = list(match)
                current_aussetzer.remove(0)
                temp_round.remove(match)

        matchplan.append(matchplan.pop(0))
        plan.append([[], temp_round, current_aussetzer, [i + 1]])

    return plan


def spielplan_einzel(player_list):
    plan = []
    all_matches = []

    if len(player_list) % 2 == 1:
        player_list.append(0)

    for i in range(len(player_list)):

        for t in range(len(player_list)):

            if t > i:
                all_matches.append([player_list[i] if not player_list[i] == "" else i + 1,
                                    player_list[t] if not player_list[t] == "" else t + 1])

    random.shuffle(all_matches)

    for r in range(len(player_list) - 1):
        matches = get_matchday(all_matches, player_list)

        for match in matches:
            all_matches.remove(match)

        plan.append(matches)
        print(str(r) + " / " + str(len(player_list) - 2))
    print("Matchreihenfolge generiert")

    return plan


def get_matchday(all_matches, player_list):
    global matches
    match_not_found = True
    versuche = 100
    while match_not_found:
        match_not_found = False
        current_matchday = []
        matches = []

        for match in all_matches:

            if len(current_matchday) < int(len(player_list)):
                if not match[0] in current_matchday and not match[1] in current_matchday:
                    current_matchday.append(match[0])
                    current_matchday.append(match[1])
            if len(current_matchday) == len(player_list):

                for i in range(len(current_matchday)):

                    if i % 2 == 0:
                        matches.append([current_matchday[i], current_matchday[i + 1]])

                break

        if not len(matches) == len(player_list) / 2:
            print("Matchaufbau fehlgeschlagen")
            versuche -= 1
            random.shuffle(all_matches)
            if versuche > 1:
                match_not_found = True

    return matches


def limited_fields(player_list, rounds, fields):
    global current_aussetzer
    matchplan = spielplan_einzel(player_list)

    matchplan_array =[]
    current_matches =[]
    plan = []
    current_aussetzer = ""
    for round in matchplan:
        for match in round:
            matchplan_array.append(match)

    print(matchplan_array)

    for i in range(int(rounds)):
        for t in range(int(fields)):
            current_matches.append(matchplan_array[0])
            matchplan_array.append(matchplan_array.pop(0))

        for match in current_matches:
            if 0 in match:
                current_aussetzer = list(match)
                current_aussetzer.remove(0)
                current_matches.remove(match)

        plan.append([[], current_matches, current_aussetzer, [i + 1]])
        current_matches = []

    return plan
