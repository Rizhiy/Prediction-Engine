from typing import List, Set

# Some types
IntList = List[int]


class GameSpecification:
    def __init__(self, players_per_team: int, teams_in_match: int, player_dim: int, team_dim: int):
        self.players_per_team = players_per_team
        self.teams_in_match = teams_in_match
        self.player_dim = player_dim
        self.team_dim = team_dim


class Skill:
    def __int__(self, mu: IntList, sigma: IntList):
        self.mu = mu
        self.sigma = sigma

    def get_combined_list(self):
        return self.mu + self.sigma


class Performance:
    def __init__(self, performance: IntList):
        self.performance = performance


class Player:
    def __init__(self, player_id: int):
        self.id = player_id
        self.performances = {}
        self.skills = {}


# More type
# TODO: perhaps make classes for these
PlayerResults = Set[(Player, List[float])]
MatchResults = (List[PlayerResults], List[float])


class Match:
    def __init__(self, match_id: int, results: MatchResults):
        self.id = match_id
        self.results = results
