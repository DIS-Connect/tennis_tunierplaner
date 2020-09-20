import app
import random
def spielplan_zufaelliges_doppel(spieler, runden, gruppen=0):
    plan = []
    number_list = []

    for i in range(spieler):
        number_list.append(i + 1)

    for i in range(runden):
        current_round = get_current_round(number_list, plan, i)
        plan.append(current_round)
    return plan

def get_current_round(number_list, plan, round_number):



    random.shuffle(number_list)

    current_order = list(number_list)

    current_round = []
    current_aussetzer = 0
    teams = []
    #Aussetzer herausfinden, falls es einen gibt:
    if len(current_order)%2 == 1:
        falscher_aussetzer = True
        while falscher_aussetzer:
            falscher_aussetzer = False
            for p in plan:
                if p[0]["aussetzer"] == current_order[-1]:
                    falscher_aussetzer = True
                    random.shuffle(number_list)
                    current_order = list(number_list)

        current_aussetzer = current_order.pop()


    for s in range(len(number_list)):


        if s % 2 == 0:

            if len(current_order) > (s + 1):
                teams.append({"p1": current_order[s], "p2": current_order[s + 1]})

    current_round.append({"teams": list(teams), "aussetzer": current_aussetzer})

    return current_round