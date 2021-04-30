# map_navigation.py

import sys
import search
import random

# Module Classes

class City:
    def __init__(self, name, road=[]):
        self.name = name
        self.road = road
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __str__(self):
        return self.name

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
        return City(self.city1) if self.city2 == city.name else City(self.city2)

class Map:
    def __init__(self):
        self.cities = []

    def addCity(self, city):
        if city not in self.cities:
            self.cities.append(city)
    
    def legalMoves(self, city):
        # Return roads that can be taken given a city (state)
        for c in self.cities:
            if c == city:
                return c.road

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

    r1 = Road('Oradea', 'Zerind', 71)
    r2 = Road('Zerind', 'Arad', 75)
    r3 = Road('Oradea', 'Sibiu', 151)
    r4 = Road('Arad', 'Sibiu', 140)
    r5 = Road('Arad', 'Timisoara', 118)
    r6 = Road('Timisoara', 'Lugoj', 111)
    r7 = Road('Lugoj', 'Mehadia', 70)
    r8 = Road('Mehadia', 'Drobeta', 75)
    r9 = Road('Craiova', 'Drobeta', 120)
    r10 = Road('Craiova', 'Rimnicu Vilcea', 146)
    r11 = Road('Craiova', 'Pitesti', 138)
    r12 = Road('Pitesti', 'Rimnicu Vilcea', 97)
    r13 = Road('Sibiu', 'Rimnicu Vilcea', 80)
    r14 = Road('Sibiu', 'Fagaras', 99)
    r15 = Road('Fagaras', 'Bucharest', 211)
    r16 = Road('Pitesti', 'Bucharest', 101)
    r17 = Road('Giurgiu', 'Bucharest', 90)
    r18 = Road('Urziceni', 'Bucharest', 85)
    r19 = Road('Urziceni', 'Hirsova', 98)
    r20 = Road('Eforie', 'Hirsova', 86)
    r21 = Road('Urziceni', 'Vaslui', 142)
    r22 = Road('Iasi', 'Vaslui', 92)

    map.addCity(City('Oradea', [r1, r3]))
    map.addCity(City('Zerind', [r1, r2]))
    map.addCity(City('Arad', [r2, r4, r5]))
    map.addCity(City('Sibiu', [r3, r4, r13, r14]))
    map.addCity(City('Timisoara', [r5, r6]))
    map.addCity(City('Lugoj', [r6, r7]))
    map.addCity(City('Mehadia', [r7, r8]))
    map.addCity(City('Drobeta', [r8, r9]))
    map.addCity(City('Craiova', [r9, r10, r11]))
    map.addCity(City('Rimnicu Vilcea', [r10, r12, r13]))
    map.addCity(City('Pitesti', [r11, r12, r16]))
    map.addCity(City('Fagaras', [r14, r15]))
    map.addCity(City('Bucharest', [r15, r16, r17, r18]))
    map.addCity(City('Urziceni', [r18, r19, r21]))
    map.addCity(City('Hirsova', [r19, r20]))
    map.addCity(City('Vaslui', [r21, r22]))
    map.addCity(City('Eforie', [r20]))
    map.addCity(City('Giurgiu', [r17]))
    map.addCity(City('Iasi', [r22]))


    # map.addRoad(Road('Iasi', 'Neamt', 87)
    
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

    if problem.destination.name == 'Bucharest':
        return d[state.name]
    return 0

if __name__ == '__main__':
    map = createMap()
    current_city = City('Oradea')
    destination_city = City('Bucharest')

    problem = MapNavigationProblem(map, current_city, destination_city)
    actions = search.dls(problem, 9)

    if type(actions) == list:
        cost = problem.getCostOfActions(actions)
        print(f"Found a path with {cost} costs")
        path = [current_city.name]
        temp = current_city
        for a in actions:
            temp = a.nextCity(temp)
            path.append(temp.name)
        print('-'.join(path))