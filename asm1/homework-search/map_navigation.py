# map_navigation.py

import sys
import search
import random

# Module Classes

class Road:
    def __init__(self, city1, city2, cost):
        if city1 == city2:
            raise Exception("Just road between 2 different cities")
        self.city1 = city1
        self.city2 = city2
        self.cost = cost
    
    def __hash__(self):
        c1 = hash(self.city1)
        c2 = hash(self.city2)
        return hash(c1 + c2 + self.cost)
    
    def __eq__(self, other):
        return (self.city1 == other.city1 and self.city2 == other.city2) or (self.city1 == other.city2 and self.city2 == other.city1)
    
    def __str__(self):
        return f"({self.city1}-----{self.cost}------{self.city2})"
    
    def checkCity(self, city):
        return city == self.city1 or city == self.city2

    def nextCity(self, city):
        return self.city1 if self.city2 == city else self.city2

class Map:
    def __init__(self):
        self.roads = []

    def addRoad(self, road):
        if road not in self.roads:
            self.roads.append(road)
    
    def legalMoves(self, city):
        # Return roads that can be taken given a city (state)
        roads = [road for road in self.roads if road.checkCity(city)]
        return roads

class MapNavigationProblem(search.SearchProblem):
    def __init__(self, map, from_city, to_city):
        self.map = map
        self.current_city = from_city
        self.destination = to_city
    
    def getStartState(self):
        return self.current_city
    
    def isGoalState(self, state):
        return state == self.destination
    
    def getSuccessors(self, city):
        succ = []
        for road in self.map.legalMoves(city):
            next_city = road.nextCity(city)
            cost = road.cost
            succ.append((next_city, road, cost))
        return succ

    def getCostOfActions(self, actions):
        return sum(action.cost for action in actions)

def createMap():
    map = Map()
    map.addRoad(Road('Oradea', 'Zerind', 71))
    map.addRoad(Road('Zerind', 'Arad', 75))
    map.addRoad(Road('Oradea', 'Sibiu', 151))
    map.addRoad(Road('Arad', 'Sibiu', 140))
    map.addRoad(Road('Arad', 'Timisoara', 118))
    map.addRoad(Road('Timisoara', 'Lugoj', 111))
    map.addRoad(Road('Lugoj', 'Mehadia', 70))
    map.addRoad(Road('Mehadia', 'Drobeta', 75))
    map.addRoad(Road('Craiova', 'Drobeta', 120))
    map.addRoad(Road('Craiova', 'Rimnicu Vilcea', 146))
    map.addRoad(Road('Craiova', 'Pitesti', 138))
    map.addRoad(Road('Pitesti', 'Rimnicu Vilcea', 97))
    map.addRoad(Road('Sibiu', 'Rimnicu Vilcea', 80))
    map.addRoad(Road('Sibiu', 'Fagaras', 99))
    map.addRoad(Road('Fagaras', 'Bucharest', 211))
    map.addRoad(Road('Pitesti', 'Bucharest', 101))
    map.addRoad(Road('Giurgiu', 'Bucharest', 90))
    map.addRoad(Road('Urziceni', 'Bucharest', 85))
    map.addRoad(Road('Urziceni', 'Hirsova', 98))
    map.addRoad(Road('Eforie', 'Hirsova', 86))
    map.addRoad(Road('Urziceni', 'Vaslui', 142))
    map.addRoad(Road('Iasi', 'Vaslui', 92))
    # map.addRoad(Road('Iasi', 'Neamt', 87))
    
    return map

def heuristic(state, problem):
    """
        Heuristic function from anywhere to Bucharest according from the book
    """

    d = {
        'Arad' : 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Drobeta': 242,
        'Eforie': 161,
        'Fagaras': 176,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 100,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374
    }

    if problem.destination == 'Bucharest':
        return d[state]
    return 0

if __name__ == '__main__':
    map = createMap()
    current_city = 'Oradea'
    destination_city = 'Bucharest'

    problem = MapNavigationProblem(map, current_city, destination_city)
    actions = search.dls(problem, 50)

    cost = problem.getCostOfActions(actions)
    print(f"Found a path with {cost} costs")
    path = [current_city]
    temp = current_city
    for a in actions:
        temp = a.nextCity(temp)
        path.append(temp)
    print('-'.join(path))