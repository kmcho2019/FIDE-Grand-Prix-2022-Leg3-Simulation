import math
import matplotlib.pyplot as plt
from enum import Enum
import random

# Tournament 3 - Berlin Germany Result Simulation
# Chess Win/Draw probability taken from:https://wismuth.com/elo/calculator.html
# No distinguishing between white/black as each player get two tries each
class GameType(Enum):
    classical = 0
    rapid = 1
    blitz = 2
    armageddon = 3

class Player:
    rank = 0
    name = "default"
    country = "AAA"
    classical_rating = 0
    rapid_rating = 0
    blitz_rating = 0
    gp_points = 0
    tournament_first = 0
    tournament_second = 0
    game_points = 0.
    game_wins = 0
    simul_round3_gp_points = 0
    simul_round3_tournament_first = 0
    simul_round3_tournament_second = 0
    simul_round3_total_game_points = 0.
    simul_round3_game_points = 0.
    simul_round3_semi_round_points = 0.
    simul_round3_final_round_points = 0.
    simul_round3_game_wins = 0

    # init method or constructor
    def __init__( self, rank, name, country, classical_rating, rapid_rating, blitz_rating, gp_points, tournament_first,
                 tournament_second, game_points, game_wins):
        self.rank = rank
        self.name = name
        self.country = country
        self.classical_rating = classical_rating
        self.rapid_rating = rapid_rating
        self.blitz_rating = blitz_rating
        self.gp_points = gp_points
        self.tournament_first = tournament_first
        self.tournament_second = tournament_second
        self.game_points = game_points
        self.game_wins = game_wins

    def __repr__(self):
        return '{' + str(self.rank) + ', '+ self.name + ', ' + self.country + ', ' + str(self.gp_points) + ', ' + \
                               str(self.tournament_first) + ', ' + str(self.tournament_second) + \
                               ', ' + str(self.game_points) + ', ' + str(self.game_wins) + ', ' + \
                                "Round3 Figures(game_points,gp_points,game_wins,tf,ts): " + \
                                str(self.simul_round3_game_points) + ', ' + str(self.simul_round3_gp_points) + \
                                ', ' + str(self.simul_round3_game_wins) + ', ' + \
                                str(self.simul_round3_tournament_first) + ', ' + \
                                str(self.simul_round3_tournament_second) + '}' + '\n'

    def print_profile(self):
        print('Name: ', self.name)
        print('Country: ', self.country)
        print('Classical Rating: ', self.classical_rating)
        print('Rapid Rating: ', self.rapid_rating)
        print('Blitz Rating: ', self.blitz_rating)
        print('Total GP Points: ', self.gp_points)
        print('Tournament Firsts: ', self.tournament_first)
        print('Tournament Seconds: ', self.tournament_second)
        print('Total Game Points: ', self.game_points)
        print('Total Game Wins: ', self.game_wins)
        print('\n')

    def print_short_profile(self):
        print('Name: ', self.name)
        print('Country: ', self.country)
        print('Classical Rating: ', self.classical_rating)
        print('Total GP Points: ', self.gp_points)
        print('\n')

    def round_reset(self):
        self.simul_round3_gp_points = 0
        self.simul_round3_tournament_first = 0
        self.simul_round3_tournament_second = 0
        self.simul_round3_total_game_points = 0.
        self.simul_round3_game_points = 0.
        self.simul_round3_semi_round_points = 0.
        self.simul_round3_final_round_points = 0.
        self.simul_round3_game_wins = 0

    def update_total_game_points(self):
        self.simul_round3_total_game_points = self.simul_round3_game_points + self.simul_round3_semi_round_points +\
                                              self.simul_round3_final_round_points
    def merge_round3_simul_result(self):
        self.gp_points += self.simul_round3_gp_points
        self.tournament_first += self.simul_round3_tournament_first
        self.tournament_second += self.simul_round3_tournament_second
        self.game_points += self.simul_round3_total_game_points
        self.game_wins += self.simul_round3_game_wins

    def divest_round3_simul_result(self):
        self.gp_points -= self.simul_round3_gp_points
        self.tournament_first -= self.simul_round3_tournament_first
        self.tournament_second -= self.simul_round3_tournament_second
        self.game_points -= self.simul_round3_total_game_points
        self.game_wins -= self.simul_round3_game_wins


player_list = []
# initialize players (rating as of 3/19/2022, before 3rd(last) tournament)
player_list.append(Player(1, 'Richárd Rapport', 'HUN', 2762, 2785, 2646, 20, 1, 0, 11, 6))
player_list.append(Player(2, 'Hikaru Nakamura', 'USA', 2750, 2837, 2850, 13, 1, 0, 6.5, 3))
player_list.append(Player(3, 'Levon Aronian', 'USA', 2785, 2705, 2773, 10, 0, 1, 7, 4))
player_list.append(Player(4, 'Dmitry Andreikin', 'FIDE', 2723, 2661, 2736, 10, 0, 1, 5.5, 2))
player_list.append(Player(5, 'Vidit Gujrathi', 'IND', 2723, 2617, 2654, 7, 0, 0, 6, 3))
player_list.append(Player(6, 'Anish Giri', 'NED', 2771, 2744, 2766, 7, 0, 0, 5, 2))
player_list.append(Player(7, 'Leinier Domínguez', 'USA', 2756, 2735, 2728, 7, 0, 0, 4.5, 3))
player_list.append(Player(8, 'Maxime Vachier-Lagrave', 'FRA', 2761, 2743, 2813, 7, 0, 0, 4, 1))
player_list.append(Player(9, 'Wesley So', 'USA', 2778, 2769, 2814, 4, 0, 0, 4, 2))
player_list.append(Player(10, 'Andrey Esipenko', 'FIDE', 2723, 2679, 2617, 4, 0, 0, 3.5, 2))
player_list.append(Player(11, 'Sam Shankland', 'USA', 2704, 2625, 2618, 4, 0, 0, 3.5, 1))
player_list.append(Player(11, 'Radosław Wojtaszek', 'POL', 2694, 2696, 2610, 4, 0, 0, 3.5, 1))
player_list.append(Player(13, 'Vladimir Fedoseev', 'FIDE', 2704, 2739, 2726, 3, 0, 0, 5.5, 3))
player_list.append(Player(14, 'Nikita Vitiugov', 'FIDE', 2726, 2580, 2673, 3, 0, 0, 3, 1))
player_list.append(Player(14, 'Amin Tabatabaei', 'IRI', 2623, 2425, 2544, 3, 0, 0, 3, 1))
player_list.append(Player(14, 'Daniil Dubov', 'FIDE', 2711, 2712, 2791, 3, 0, 0, 3, 1))
player_list.append(Player(14, 'Alexandr Predke', 'FIDE', 2682, 2601, 2614, 3, 0, 0, 3, 1))
player_list.append(Player(18, 'Shakhriyar Mamedyarov', 'AZE', 2776, 2722, 2769, 3, 0, 0, 3, 0))
player_list.append(Player(19, 'Alexander Grischuk', 'FIDE', 2758, 2759, 2762, 2, 0, 0, 5, 1))
player_list.append(Player(20, 'Pentala Harikrishna', 'IND', 2716, 2624, 2574, 2, 0, 0, 4.5, 0))
player_list.append(Player(21, 'Étienne Bacrot', 'FRA', 2635, 2720, 2673, 2, 0, 0, 4, 0))
player_list.append(Player(22, 'Alexei Shirov', 'ESP', 2691, 2623, 2678, 1, 0, 0, 4, 1))
player_list.append(Player(23, 'Yu Yangyi', 'CHN', 2713, 2738, 2808, 0, 0, 0, 2.5, 0))
player_list.append(Player(24, 'Grigoriy Oparin', 'FIDE', 2674, 2650, 2665, 0, 0, 0, 2, 0))
player_list.append(Player(25, 'Vincent Keymer', 'CHN', 2655, 2542, 2557, 0, 0, 0, 1.5, 0))
player_list.append(Player(26, 'Ding Liren', 'CHN', 2799, 2836, 2788, 0, 0, 0, 0, 0))

# funtion for comparing the rank of two players 1 if x(player1) is higher -1 is y(player2) 0 when equal
def compare_players(x: Player, y: Player) -> int:
    if(x.gp_points > y.gp_points):
        return 1
    elif(x.gp_points < y.gp_points):
        return -1
    else:
        if(x.tournament_first > y.tournament_first):
            return 1
        elif(x.tournament_first < y.tournament_first):
            return -1
        else:
            if(x.tournament_second > y.tournament_second):
                return 1
            elif(x.tournament_second < y.tournament_second):
                return -1
            else:
                if(x.game_points > y.game_points):
                    return 1
                elif(x.game_points < y.game_points):
                    return -1
                else:
                    if(x.game_wins > y.game_wins):
                        return 1
                    elif(x.game_wins < y.game_wins):
                        return -1
                    else:
                        return 0

def rank_players(player_list):
    player_list.sort(key=lambda x: (x.gp_points, x.tournament_first, x.tournament_second,
                                    x.game_points, x.game_wins), reverse=True)
    x = 0
    while x < (len(player_list) - 1):
        counter = 1
        if(compare_players(player_list[x], player_list[x + counter]) != 0):
            player_list[x].rank = x + 1
            player_list[x + counter].rank = x + 1 + counter
            x = x + counter
        else:
            player_list[x].rank = x + 1
            player_list[x + counter].rank = x + 1
            counter = counter + 1

            while(((x + counter) < len(player_list)) and \
                  compare_players(player_list[x], player_list[x + counter]) == 0):
                player_list[x + counter].rank = x + 1
                counter = counter + 1
            x = x + counter

def eloNormal(eloDiff):
    return math.erfc(-eloDiff / ((2000.0/7) * math.sqrt(2))) / 2

def eloPerPawnAtElo(elo):
    return math.exp(elo/1020) * 26.59

def win_draw_probability(player1_rating: int, player2_rating: int) -> (int, int, int):
    #output:(win % for p1, draw %, win % for p2)
    if(player1_rating <= player2_rating):
        rating1 = player1_rating
        rating2 = player2_rating
        switch_requirement = False
    else:
        rating1 = player2_rating
        rating2 = player1_rating
        switch_requirement = True
    #rating1 <= rating2
    diff = rating1 - rating2
    ave = (rating1 + rating2) / 2
    expected_score = eloNormal(diff)
    eloPerPawn = eloPerPawnAtElo(ave)
    eloShift = eloPerPawn * 0.6
    player1_win_probability = eloNormal(diff - eloShift)
    draw_probability = (expected_score - player1_win_probability) * 2
    player2_win_probability = 1 - player1_win_probability - draw_probability
    if(switch_requirement == True):
        return(player2_win_probability, draw_probability, player1_win_probability)
    else:
        return(player1_win_probability, draw_probability, player2_win_probability)
'''
def chess_game(player1: Player, player2: Player, game_type: GameType):
    if game_type == GameType.classical:
        elo_difference = player1.classical_rating - player2.classical_rating
        elo_average = (player.classical_rating + player2.classical_rating) / 2
    elif game_type == GameType.rapid:
        elo_difference = player1.rapid_rating - player2.rapid_rating
        elo_average = (player.rapid_rating + player2.rapid_rating) / 2
    elif game_type == GameType.blitz:
        elo_difference = player1.blitz_rating - player2.blitz_rating
        elo_average = (player.blitz_rating + player2.blitz_rating) / 2
    else :
        elo_difference = player1.blitz_rating - player2.blitz_rating
        elo_average = (player.blitz_rating + player2.blitz_rating) / 2
'''
def group_round_chess_game(player1: Player, player2: Player):
    (player1_win_probability,draw_probability, player2_win_probability) = \
        win_draw_probability(player1.classical_rating, player2.classical_rating)
    if random.random() < draw_probability:
        player1.simul_round3_game_points += 0.5
        player2.simul_round3_game_points += 0.5
    elif (random.random() / (player1_win_probability + player2_win_probability)) < player1_win_probability:
        player1.simul_round3_game_points += 1.0
        player1.simul_round3_game_wins += 1
    else:
        player2.simul_round3_game_points += 1.0
        player2.simul_round3_game_wins += 1

def semi_chess_game(player1: Player, player2: Player):
    (player1_win_probability,draw_probability, player2_win_probability) = \
        win_draw_probability(player1.classical_rating, player2.classical_rating)
    if random.random() < draw_probability:
        player1.simul_round3_semi_round_points += 0.5
        player2.simul_round3_semi_round_points += 0.5
    elif (random.random() / (player1_win_probability + player2_win_probability)) < player1_win_probability:
        player1.simul_round3_semi_round_points += 1.0
        player1.simul_round3_game_wins += 1
    else:
        player2.simul_round3_semi_round_points += 1.0
        player2.simul_round3_game_wins += 1

def final_chess_game(player1: Player, player2: Player):
    (player1_win_probability,draw_probability, player2_win_probability) = \
        win_draw_probability(player1.classical_rating, player2.classical_rating)
    if random.random() < draw_probability:
        player1.simul_round3_final_round_points += 0.5
        player2.simul_round3_final_round_points += 0.5
    elif (random.random() / (player1_win_probability + player2_win_probability)) < player1_win_probability:
        player1.simul_round3_final_round_points += 1.0
        player1.simul_round3_game_wins += 1
    else:
        player2.simul_round3_final_round_points += 1.0
        player2.simul_round3_game_wins += 1

def tiebreak_chess_game(player1_rating, player2_rating):
    (player1_win_probability,draw_probability, player2_win_probability) = \
        win_draw_probability(player1_rating, player2_rating)
    if random.random() < draw_probability:
        return 0
    elif (random.random() / (player1_win_probability + player2_win_probability)) < player1_win_probability:
        return 1
    else:
        return 2

def knock_out_chess_game(player1: Player, player2: Player):
    (player1_win_probability,draw_probability, player2_win_probability) = \
        win_draw_probability(player1.classical_rating, player2.classical_rating)
    if random.random() < draw_probability:
        return 0
    elif (random.random() / (player1_win_probability + player2_win_probability)) < player1_win_probability:
        player1.simul_round3_game_wins += 1
        return 1
    else:
        player2.simul_round3_game_wins += 1
        return 2

def group_stage(player1 : Player, player2 : Player, player3 : Player, player4 : Player):
    group_temp_list = []
    group_temp_list.append(player1)
    group_temp_list.append(player2)
    group_temp_list.append(player3)
    group_temp_list.append(player4)
    print("Group Initial:")
    print(group_temp_list)
    for x in range(2):
        group_round_chess_game(player1, player2)
        group_round_chess_game(player1, player3)
        group_round_chess_game(player1, player4)
        group_round_chess_game(player2, player3)
        group_round_chess_game(player2, player4)
        group_round_chess_game(player3, player4)
    group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)

    if group_temp_list[0].simul_round3_game_points != group_temp_list[1].simul_round3_game_points:

        group_temp_list[0].simul_round3_gp_points += 7
        if group_temp_list[1].simul_round3_game_points > group_temp_list[2].simul_round3_game_points:
            group_temp_list[1].simul_round3_gp_points += 4
            if group_temp_list[2].simul_round3_game_points > group_temp_list[3].simul_round3_game_points:
                group_temp_list[2].simul_round3_gp_points += 2
                group_temp_list[3].simul_round3_gp_points += 0
            elif group_temp_list[3].simul_round3_game_points > group_temp_list[2].simul_round3_game_points:
                group_temp_list[3].simul_round3_gp_points += 2
                group_temp_list[2].simul_round3_gp_points += 0
            else:
                group_temp_list[2].simul_round3_gp_points += 1
                group_temp_list[3].simul_round3_gp_points += 1
        elif group_temp_list[2].simul_round3_game_points > group_temp_list[1].simul_round3_game_points:
            group_temp_list[2].simul_round3_gp_points += 4
            if group_temp_list[1].simul_round3_game_points > group_temp_list[3].simul_round3_game_points:
                group_temp_list[1].simul_round3_gp_points += 2
                group_temp_list[3].simul_round3_gp_points += 0
            elif group_temp_list[3].simul_round3_game_points > group_temp_list[1].simul_round3_game_points:
                group_temp_list[3].simul_round3_gp_points += 2
                group_temp_list[1].simul_round3_gp_points += 0
            else:
                group_temp_list[1].simul_round3_gp_points += 1
                group_temp_list[3].simul_round3_gp_points += 1
        else: # 2nd and 3rd share gp_points due to having same round game points
            if group_temp_list[1].simul_round3_game_points > group_temp_list[3].simul_round3_game_points:
                group_temp_list[1].simul_round3_gp_points += 3
                group_temp_list[2].simul_round3_gp_points += 3
                group_temp_list[3].simul_round3_gp_points += 0
            else:
                group_temp_list[1].simul_round3_gp_points += 2
                group_temp_list[2].simul_round3_gp_points += 2
                group_temp_list[3].simul_round3_gp_points += 2

        #group_temp_list[0].simul_round3_tournament_first += 1
        #group_temp_list[1].simul_round3_tournament_second += 1
        print("Group Final:")
        print(group_temp_list)
        group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)
        return group_temp_list[0] # no tie breaks, group leader advances
    elif (group_temp_list[0].simul_round3_game_points == group_temp_list[1].simul_round3_game_points) and \
        (group_temp_list[0].simul_round3_game_points != group_temp_list[2].simul_round3_game_points):
        # two way tie
        # allocate gp_points(Grand Prix points) for 3/4 place
        if group_temp_list[2].simul_round3_game_points > group_temp_list[3].simul_round3_game_points:
            group_temp_list[2].simul_round3_gp_points += 2
            group_temp_list[3].simul_round3_gp_points += 0
        elif group_temp_list[3].simul_round3_game_points > group_temp_list[2].simul_round3_game_points:
            group_temp_list[3].simul_round3_gp_points += 2
            group_temp_list[2].simul_round3_gp_points += 0
        else:
            group_temp_list[2].simul_round3_gp_points += 1
            group_temp_list[3].simul_round3_gp_points += 1

        rapid_player1_score = 0.
        rapid_player2_score = 0.
        blitz_player1_score = 0.
        blitz_player2_score = 0.
        # rapid tiebreaks
        for x in range(2):
            rapid_tiebreak_result = \
                tiebreak_chess_game(group_temp_list[0].rapid_rating, group_temp_list[1].rapid_rating)
            if rapid_tiebreak_result == 0:
                rapid_player1_score += 0.5
                rapid_player2_score += 0.5
            elif rapid_tiebreak_result == 1:
                rapid_player1_score += 1.0
            else:
                rapid_player2_score += 1.0

        if rapid_player1_score > rapid_player2_score:
            #group_temp_list[0].simul_round3_tournament_first += 1
            #group_temp_list[1].simul_round3_tournament_second += 1
            group_temp_list[0].simul_round3_gp_points += 7 # allocate gp_point going to semi finals
            group_temp_list[1].simul_round3_gp_points += 4 # allocate gp_point for 2nd in pool
            print("Group Final(Two-Way Tie, Rapid):")
            print(group_temp_list)
            group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)
            return group_temp_list[0]
        elif rapid_player2_score > rapid_player1_score:
            #group_temp_list[1].simul_round3_tournament_first += 1
            #group_temp_list[0].simul_round3_tournament_second += 1
            group_temp_list[1].simul_round3_gp_points += 7 # allocate gp_point going to semi finals
            group_temp_list[0].simul_round3_gp_points += 4 # allocate gp_point for 2nd in pool            print("Group Final(Two-Way Tie, Rapid):")
            print(group_temp_list)
            group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)
            return group_temp_list[0]
        else:
            #blitz tiebreak
            for x in range(2):
                blitz_tiebreak_result = \
                    tiebreak_chess_game(group_temp_list[0].blitz_rating, group_temp_list[1].blitz_rating)
                if blitz_tiebreak_result == 0:
                    blitz_player1_score += 0.5
                    blitz_player2_score += 0.5
                elif blitz_tiebreak_result == 1:
                    blitz_player1_score += 1.0
                else:
                    blitz_player2_score += 1.0

            if blitz_player1_score > blitz_player2_score:
                #group_temp_list[0].simul_round3_tournament_first += 1
                #group_temp_list[1].simul_round3_tournament_second += 1
                group_temp_list[0].simul_round3_gp_points += 7  # allocate gp_point going to semi finals
                group_temp_list[1].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
                print("Group Final(Two-Way Tie, Blitz):")
                print(group_temp_list)
                group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)
                return group_temp_list[0]
            elif blitz_player2_score > blitz_player1_score:
                #group_temp_list[1].simul_round3_tournament_first += 1
                #group_temp_list[0].simul_round3_tournament_second += 1
                group_temp_list[1].simul_round3_gp_points += 7  # allocate gp_point going to semi finals
                group_temp_list[0].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
                print("Group Final(Two-Way Tie, Blitz):")
                print(group_temp_list)
                group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)
                return group_temp_list[0]
            else:
                #armageddon, sudden death
                armageddon_result = \
                    tiebreak_chess_game(group_temp_list[0].blitz_rating, group_temp_list[1].blitz_rating)
                group_temp_list[2].simul_round3_gp_points += 2
                group_temp_list[3].simul_round3_gp_points += 0
                if random.random() < 0.5: #player1 draws white
                    if armageddon_result == 1:
                        #group_temp_list[0].simul_round3_tournament_first += 1
                        #group_temp_list[1].simul_round3_tournament_second += 1
                        group_temp_list[0].simul_round3_gp_points += 7
                        group_temp_list[1].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
                        print("Group Final(Two-Way Tie, Armageddon):")
                        print(group_temp_list)
                        group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return group_temp_list[0]
                    else:
                        #group_temp_list[1].simul_round3_tournament_first += 1
                        #group_temp_list[0].simul_round3_tournament_second += 1
                        group_temp_list[1].simul_round3_gp_points += 7
                        group_temp_list[0].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
                        print("Group Final(Two-Way Tie, Armageddon):")
                        print(group_temp_list)
                        group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return group_temp_list[0]
                else: #player2 draws white
                    if armageddon_result == 2:
                        #group_temp_list[1].simul_round3_tournament_first += 1
                        #group_temp_list[0].simul_round3_tournament_second += 1
                        group_temp_list[1].simul_round3_gp_points += 7
                        group_temp_list[0].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
                        print("Group Final(Two-Way Tie, Armageddon):")
                        print(group_temp_list)
                        group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return group_temp_list[0]
                    else:
                        #group_temp_list[0].simul_round3_tournament_first += 1
                        #group_temp_list[1].simul_round3_tournament_second += 1
                        group_temp_list[0].simul_round3_gp_points += 7
                        group_temp_list[1].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
                        print("Group Final(Two-Way Tie, Armageddon):")
                        print(group_temp_list)
                        group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return group_temp_list[0]
    elif (group_temp_list[0].simul_round3_game_points == group_temp_list[1].simul_round3_game_points) and \
        (group_temp_list[0].simul_round3_game_points == group_temp_list[2].simul_round3_game_points) and \
        (group_temp_list[0].simul_round3_game_points != group_temp_list[3].simul_round3_game_points):
        # three way tie
        group_temp_list[3].simul_round3_gp_points += 0  # allocate gp_point for 4th in pool
        # not full implementation just assume perfect randomness
        shuffle_list = [0,1,2]
        random.shuffle(shuffle_list)
        group_temp_list[shuffle_list[0]].simul_round3_gp_points += 7
        group_temp_list[shuffle_list[1]].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
        group_temp_list[shuffle_list[2]].simul_round3_gp_points += 2

        #group_temp_list[shuffle_list[0]].tournament_first += 1  # tournament first/second
        #group_temp_list[shuffle_list[1]].tournament_second += 1
        print("Group Final(Three Way Tie):")
        print(group_temp_list)
        group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)
        return group_temp_list[shuffle_list[0]]
    elif (group_temp_list[0].simul_round3_game_points == group_temp_list[1].simul_round3_game_points) and \
        (group_temp_list[0].simul_round3_game_points == group_temp_list[2].simul_round3_game_points) and \
        (group_temp_list[0].simul_round3_game_points == group_temp_list[3].simul_round3_game_points):
        # four way tie
        # not full implementation just assume perfect randomness
        shuffle_list = [0,1,2,3]
        random.shuffle(shuffle_list)
        group_temp_list[shuffle_list[0]].simul_round3_gp_points += 7
        group_temp_list[shuffle_list[1]].simul_round3_gp_points += 4  # allocate gp_point for 2nd in pool
        group_temp_list[shuffle_list[2]].simul_round3_gp_points += 2
        group_temp_list[shuffle_list[3]].simul_round3_gp_points += 0

        #group_temp_list[shuffle_list[0]].tournament_first += 1  # tournament first/second
        #group_temp_list[shuffle_list[1]].tournament_second += 1
        print("Group Final(Four Way Tie):")
        print(group_temp_list)
        group_temp_list.sort(key=lambda x: (x.simul_round3_game_points, x.simul_round3_gp_points), reverse=True)
        return group_temp_list[0]

def semi_final(player1: Player, player2: Player):
    semi_final_temp_list = []
    semi_final_temp_list.append(player1)
    semi_final_temp_list.append(player2)
    print("Semi Final Initial:")
    print(semi_final_temp_list)
    for x in range(2):
        semi_chess_game(player1, player2)
    semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points), reverse= True)

    if semi_final_temp_list[0].simul_round3_semi_round_points != semi_final_temp_list[1].simul_round3_semi_round_points:
        semi_final_temp_list[0].simul_round3_gp_points += 3 # gp_point for going to the finals
        print("Semi Final:")
        semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points), reverse=True)
        print(semi_final_temp_list)
        semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points), reverse=True)
        return semi_final_temp_list[0] # no tie break required
    else:
        #tie breaks for semi final
        rapid_player1_score = 0.
        rapid_player2_score = 0.
        blitz_player1_score = 0.
        blitz_player2_score = 0.
        # rapid tiebreaks
        for x in range(2):
            rapid_tiebreak_result = \
                tiebreak_chess_game(semi_final_temp_list[0].rapid_rating, semi_final_temp_list[1].rapid_rating)
            if rapid_tiebreak_result == 0:
                rapid_player1_score += 0.5
                rapid_player2_score += 0.5
            elif rapid_tiebreak_result == 1:
                rapid_player1_score += 1.0
            else:
                rapid_player2_score += 1.0

        if rapid_player1_score > rapid_player2_score:
            semi_final_temp_list[0].simul_round3_gp_points += 3 # allocate gp_point for semi final winner
            print("Semi Final(Two-Way Tie, Rapid):")
            semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points), \
                                      reverse=True)
            print(semi_final_temp_list)
            semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points), reverse=True)
            return semi_final_temp_list[0]
        elif rapid_player2_score > rapid_player1_score:
            semi_final_temp_list[1].simul_round3_gp_points += 3 # allocate gp_point for semi final winner
            print("Semi Final(Two-Way Tie, Rapid):")
            semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points), reverse=True)
            print(semi_final_temp_list)
            semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points), reverse=True)
            return semi_final_temp_list[0]
        else:
            #blitz tiebreak
            for x in range(2):
                blitz_tiebreak_result = \
                    tiebreak_chess_game(semi_final_temp_list[0].blitz_rating, semi_final_temp_list[1].blitz_rating)
                if blitz_tiebreak_result == 0:
                    blitz_player1_score += 0.5
                    blitz_player2_score += 0.5
                elif blitz_tiebreak_result == 1:
                    blitz_player1_score += 1.0
                else:
                    blitz_player2_score += 1.0

            if blitz_player1_score > blitz_player2_score:
                semi_final_temp_list[0].simul_round3_gp_points += 3  # allocate gp_point for semi final winner
                print("Semi Final(Two-Way Tie, Blitz):")
                semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points), reverse=True)
                print(semi_final_temp_list)
                semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points), reverse=True)
                return semi_final_temp_list[0]
            elif blitz_player2_score > blitz_player1_score:
                semi_final_temp_list[1].simul_round3_gp_points += 3  # allocate gp_point for semi final winner
                print("Semi Final(Two-Way Tie, Blitz):")
                semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points), reverse=True)
                print(semi_final_temp_list)
                semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points), reverse=True)
                return semi_final_temp_list[0]
            else:
                #armageddon, sudden death
                armageddon_result = \
                    tiebreak_chess_game(semi_final_temp_list[0].blitz_rating, semi_final_temp_list[1].blitz_rating)
                if random.random() < 0.5: #player1 draws white
                    if armageddon_result == 1:
                        semi_final_temp_list[0].simul_round3_gp_points += 3  # allocate gp_point for semi final winner
                        print("Semi Final(Two-Way Tie, Armageddon):")
                        print(semi_final_temp_list)
                        semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return semi_final_temp_list[0]
                    else:
                        semi_final_temp_list[1].simul_round3_gp_points += 3  # allocate gp_point for semi final winner
                        print("Semi Final(Two-Way Tie, Armageddon):")
                        print(semi_final_temp_list)
                        semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return semi_final_temp_list[0]
                else: #player2 draws white
                    if armageddon_result == 2:
                        semi_final_temp_list[1].simul_round3_gp_points += 3  # allocate gp_point for semi final winner
                        print("Semi Final(Two-Way Tie, Armageddon):")
                        print(semi_final_temp_list)
                        semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return semi_final_temp_list[0]
                    else:
                        semi_final_temp_list[0].simul_round3_gp_points += 3  # allocate gp_point for 2nd in pool
                        print("Semi Final(Two-Way Tie, Armageddon):")
                        print(semi_final_temp_list)
                        semi_final_temp_list.sort(key=lambda x: (x.simul_round3_semi_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        return semi_final_temp_list[0]

def final(player1: Player, player2: Player):
    final_temp_list = []
    final_temp_list.append(player1)
    final_temp_list.append(player2)
    print("Final Initial:")
    print(final_temp_list)
    for x in range(2):
        final_chess_game(player1, player2)
    final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points), reverse= True)

    if final_temp_list[0].simul_round3_final_round_points != final_temp_list[1].simul_round3_final_round_points:
        final_temp_list[0].simul_round3_gp_points += 3 # gp_point for going to the finals
        print("Final:")
        final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points), reverse=True)
        print(final_temp_list)
        final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points), reverse=True)
        final_temp_list[0].simul_round3_tournament_first += 1
        final_temp_list[1].simul_round3_tournament_second += 1
        return final_temp_list[0] # no tie break required
    else:
        #tie breaks for final
        rapid_player1_score = 0.
        rapid_player2_score = 0.
        blitz_player1_score = 0.
        blitz_player2_score = 0.
        # rapid tiebreaks
        for x in range(2):
            rapid_tiebreak_result = \
                tiebreak_chess_game(final_temp_list[0].rapid_rating, final_temp_list[1].rapid_rating)
            if rapid_tiebreak_result == 0:
                rapid_player1_score += 0.5
                rapid_player2_score += 0.5
            elif rapid_tiebreak_result == 1:
                rapid_player1_score += 1.0
            else:
                rapid_player2_score += 1.0

        if rapid_player1_score > rapid_player2_score:
            final_temp_list[0].simul_round3_gp_points += 3 # allocate gp_point for final winner
            print("Final(Two-Way Tie, Rapid):")
            final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points), \
                                      reverse=True)
            print(final_temp_list)
            final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points), reverse=True)
            final_temp_list[0].simul_round3_tournament_first += 1
            final_temp_list[1].simul_round3_tournament_second += 1
            return final_temp_list[0]
        elif rapid_player2_score > rapid_player1_score:
            final_temp_list[1].simul_round3_gp_points += 3 # allocate gp_point for final winner
            print("Final(Two-Way Tie, Rapid):")
            final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points), reverse=True)
            print(final_temp_list)
            final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points), reverse=True)
            final_temp_list[0].simul_round3_tournament_first += 1
            final_temp_list[1].simul_round3_tournament_second += 1
            return final_temp_list[0]
        else:
            #blitz tiebreak
            for x in range(2):
                blitz_tiebreak_result = \
                    tiebreak_chess_game(final_temp_list[0].blitz_rating, final_temp_list[1].blitz_rating)
                if blitz_tiebreak_result == 0:
                    blitz_player1_score += 0.5
                    blitz_player2_score += 0.5
                elif blitz_tiebreak_result == 1:
                    blitz_player1_score += 1.0
                else:
                    blitz_player2_score += 1.0

            if blitz_player1_score > blitz_player2_score:
                final_temp_list[0].simul_round3_gp_points += 3  # allocate gp_point for final winner
                print("Final(Two-Way Tie, Blitz):")
                final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points), reverse=True)
                print(final_temp_list)
                final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points), reverse=True)
                final_temp_list[0].simul_round3_tournament_first += 1
                final_temp_list[1].simul_round3_tournament_second += 1
                return final_temp_list[0]
            elif blitz_player2_score > blitz_player1_score:
                final_temp_list[1].simul_round3_gp_points += 3  # allocate gp_point for final winner
                print("Final(Two-Way Tie, Blitz):")
                final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points), reverse=True)
                print(final_temp_list)
                final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points), reverse=True)
                final_temp_list[0].simul_round3_tournament_first += 1
                final_temp_list[1].simul_round3_tournament_second += 1
                return final_temp_list[0]
            else:
                #armageddon, sudden death
                armageddon_result = \
                    tiebreak_chess_game(final_temp_list[0].blitz_rating, final_temp_list[1].blitz_rating)
                if random.random() < 0.5: #player1 draws white
                    if armageddon_result == 1:
                        final_temp_list[0].simul_round3_gp_points += 3  # allocate gp_point for final winner
                        print("Final(Two-Way Tie, Armageddon):")
                        print(final_temp_list)
                        final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        final_temp_list[0].simul_round3_tournament_first += 1
                        final_temp_list[1].simul_round3_tournament_second += 1
                        return final_temp_list[0]
                    else:
                        final_temp_list[1].simul_round3_gp_points += 3  # allocate gp_point for final winner
                        print("Final(Two-Way Tie, Armageddon):")
                        print(final_temp_list)
                        final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        final_temp_list[0].simul_round3_tournament_first += 1
                        final_temp_list[1].simul_round3_tournament_second += 1
                        return final_temp_list[0]
                else: #player2 draws white
                    if armageddon_result == 2:
                        final_temp_list[1].simul_round3_gp_points += 3  # allocate gp_point for final winner
                        print("Final(Two-Way Tie, Armageddon):")
                        print(final_temp_list)
                        final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        final_temp_list[0].simul_round3_tournament_first += 1
                        final_temp_list[1].simul_round3_tournament_second += 1
                        return final_temp_list[0]
                    else:
                        final_temp_list[0].simul_round3_gp_points += 3  # allocate gp_point for 2nd in pool
                        print("Final(Two-Way Tie, Armageddon):")
                        print(final_temp_list)
                        final_temp_list.sort(key=lambda x: (x.simul_round3_final_round_points, x.simul_round3_gp_points),
                                             reverse=True)
                        final_temp_list[0].simul_round3_tournament_first += 1
                        final_temp_list[1].simul_round3_tournament_second += 1
                        return final_temp_list[0]


def search_recursion1(player_list: list, index_num: int) -> int:
    x = 1
    list = []
    if player_list[1].rank != player_list[index_num].rank and index_num < len(player_list):
        for x in range(1, index_num):
            list.append(x)
        random.shuffle(list)
        return list[0]
    elif player_list[0].rank == player_list[index_num].rank and index_num < len(player_list):
        search_recursion1(player_list, index_num + 1)
    else:
        print("Error! Index for player_list out of bounds.")
        return None
def search_recursion2(player_list: list, index_num: int) ->(int, int):
    x = 0
    list = []
    if player_list[0].rank != player_list[index_num].rank and index_num < len(player_list):
        for x in range(index_num):
            list.append(x)
        random.shuffle(list)
        return (list[0], list[1])
    elif player_list[0].rank == player_list[index_num].rank and index_num < len(player_list):
        search_recursion2(player_list, index_num + 1)
    else:
        print("Error! Index for player_list out of bounds.")
        return None


def selecting_top_two(player_list: list) -> (int, int):
    player1_index = 0
    player2_index = 0
    if player_list[0].rank != player_list[1].rank:
        player1_index = 0
        if player_list[1].rank != player_list[2].rank:
            player2_index = 1
        else:
            player2_index = search_recursion1(player_list, 3)
    else:
        if player_list[0].rank != player_list[2].rank:
            player1_index = 0
            player2_index = 1
        else:
            if player_list[0].rank != player_list[3].rank:
                list = [0,1,2]
                random.shuffle(list)
                player1_index = list[0]
                player2_index = list[1]
            else:
                (player1_index,player2_index) = search_recursion2(player_list, 4)
    return (player1_index, player2_index)





print(player_list)

rank_players(player_list)

print(player_list)

#Way to search for player and its index in player_list
search_test = [x for x in player_list if x.name == 'Levon Aronian']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Hikaru Nakamura']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Andrey Esipenko']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Grigoriy Oparin']
#print(search_test)
print(player_list.index(search_test[0]))

print("\n")
##############
search_test = [x for x in player_list if x.name == 'Shakhriyar Mamedyarov']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Leinier Domínguez']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Daniil Dubov']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Vincent Keymer']
#print(search_test)
print(player_list.index(search_test[0]))
print("\n")

##########
search_test = [x for x in player_list if x.name == 'Wesley So']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Maxime Vachier-Lagrave']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Sam Shankland']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Alexandr Predke']
#print(search_test)
print(player_list.index(search_test[0]))
print("\n")

########
search_test = [x for x in player_list if x.name == 'Anish Giri']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Nikita Vitiugov']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Yu Yangyi']
#print(search_test)
print(player_list.index(search_test[0]))

search_test = [x for x in player_list if x.name == 'Amin Tabatabaei']
#print(search_test)
print(player_list.index(search_test[0]))




#Pool A
a = group_stage(player_list[2],player_list[1],player_list[9],player_list[23])

print("\n Game points, game wins, round first, round second")
print("Levon: ", player_list[2].simul_round3_game_points, player_list[2].simul_round3_game_wins, player_list[2].simul_round3_tournament_first, player_list[2].simul_round3_tournament_second)
print("Hikaru: ", player_list[1].simul_round3_game_points, player_list[1].simul_round3_game_wins, player_list[1].simul_round3_tournament_first, player_list[1].simul_round3_tournament_second)
print("Andrey: ", player_list[9].simul_round3_game_points, player_list[9].simul_round3_game_wins, player_list[9].simul_round3_tournament_first, player_list[9].simul_round3_tournament_second)
print("Oparin: ", player_list[23].simul_round3_game_points, player_list[23].simul_round3_game_wins, player_list[23].simul_round3_tournament_first, player_list[23].simul_round3_tournament_second)

print(a)

#Pool B
b = group_stage(player_list[17],player_list[6],player_list[15],player_list[24])
print(b)
#Pool C
c = group_stage(player_list[8],player_list[7],player_list[10],player_list[16])
print(c)

#Pool D
d = group_stage(player_list[5],player_list[13],player_list[22],player_list[14])
print(d)

print("Semi Finalists:", a, b, c, d)


# Group Testing
for x in range(0):
    print("Group Round Epoch: ", x)
    for x in player_list:
        x.round_reset()
    a = group_stage(player_list[2], player_list[1], player_list[9], player_list[23])
    print(a)
    b = group_stage(player_list[17], player_list[6], player_list[15], player_list[24])
    print(b)
    c = group_stage(player_list[8], player_list[7], player_list[10], player_list[16])
    print(c)
    d = group_stage(player_list[5], player_list[13], player_list[22], player_list[14])
    print(d)


rank_players(player_list)
print(player_list)
print(player_list[1].simul_round3_gp_points)
#Semi Finals
#Semi Final1: Winner of Pool A vs Winner of Pool B
a_b_winner = semi_final(a, b)
#Semi Final2: Winner of Pool C vs Winner of Pool D
c_d_winner = semi_final(c, d)
print(a_b_winner)
print(c_d_winner)
#Final
tournament_winner = final(a_b_winner,c_d_winner)
print(tournament_winner)


for x in player_list:
    x.update_total_game_points()
for x in player_list:
    x.merge_round3_simul_result()
rank_players(player_list)
print(player_list)

(candidate1,candidate2) = selecting_top_two(player_list)
print("The Top Two Players(Qualified for the Candidates)\n")
print(player_list[candidate1])
print(player_list[candidate2])

#Reset Process
for x in player_list:
    x.divest_round3_simul_result()
for x in player_list:
    x.round_reset()
rank_players(player_list)





print("Reverted to Original Setting:\n")
print(player_list)




#Group-Semi Testing
for x in range(0):
    print("Round Epoch: ", x)
    for x in player_list:
        x.round_reset()
    a = group_stage(player_list[2], player_list[1], player_list[9], player_list[23])
    print(a)
    b = group_stage(player_list[17], player_list[6], player_list[15], player_list[24])
    print(b)
    c = group_stage(player_list[8], player_list[7], player_list[10], player_list[16])
    print(c)
    d = group_stage(player_list[5], player_list[13], player_list[22], player_list[14])
    print(d)
    a_b_winner = semi_final(a, b)
    # Semi Final2: Winner of Pool C vs Winner of Pool D
    c_d_winner = semi_final(c, d)
    print("!!")
    print(a_b_winner)
    print(c_d_winner)
'''
for x in range(1000):
    group_stage(player_list[2], player_list[1], player_list[9], player_list[23])
    for x in player_list:
        x.round_reset()
    # map(lambda x: x.round_reset(),player_list)
'''

'''
for obj in player_list:
    obj.print_short_profile()
'''


'''
for obj in player_list:
    obj.print_profile()
'''

'''
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
'''
