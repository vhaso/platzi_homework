from collections import deque
from copy import copy
from numpy import sqrt

class Location:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.streets_from = []
        self.streets_to = []

class Street:
    def __init__(self, start, end, length=None):
        self.start = start
        self.end = end
        self.length = length
        start.streets_from.append(self)
        end.streets_to.append(self)

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, val):
        assert isinstance(val, Location), 'Start is not a Location.'
        self._start = val

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, val):
        assert isinstance(val, Location), 'End is not a Location.'
        self._end = val

    @property
    def length(self):
        if self._length is not None:
            return self._length
        else:
            x1 = self.start.x
            x2 = self.end.x
            y1 = self.start.y
            y2 = self.end.y
            return sqrt((x2-x1)**2 + (y2-y1)**2)

    @length.setter
    def length(self, val):
        self._length = val

class Route:
    def __init__(self, street=None):
        self.streets = [street]
    
    def __str__(self):
        return f'(length: {self.length():0.2f}) ' + ' -> '.join(
            [self.start.name] +
            [street.end.name for street in self.streets]
        )

    @property
    def start(self):
        return self.streets[0].start

    @property
    def end(self):
        return self.streets[-1].end

    def append(self, part):
        assert isinstance(part, (Street, Route)), 'Can only append Street or Route.'
        assert not self.streets or self.end == part.start, "Street doesn't connect."
        if isinstance(part, Street):
            self.streets.append(part)
        elif isinstance(part, Route):
            for street in part.streets:
                self.streets.append(street)

    def length(self):
        return sum([street.length for street in self.streets])

    def connects(self, start, end):
        return self.start == start and self.end == end

    def __contains__(self, location):
        assert isinstance(location, Location)
        return location in [self.start] + [street.end for street in self.streets]
    
    def __copy__(self):
        _self = Route()
        _self.streets = copy(self.streets)
        return _self

def shortest_route(streets, start, end):
    routes = deque([Route(street) for street in start.streets_from])
    shortest_route = None
    print('Routes:')
    while routes:
        route = routes.popleft()
        print(route)
        if route.connects(start, end):
            if not shortest_route or route.length() < shortest_route.length():
                shortest_route = route
        if shortest_route and route.length() >= shortest_route.length():
            continue
        for street in route.end.streets_from:
            if street.end not in route:
                _route = copy(route)
                _route.append(street)
                routes.append(_route)
    return shortest_route

home = Location(0,0,'Home')
cafe = Location(0,1,'Cafe')
restaurant = Location(1,1,'Restaurant')
school = Location(1,2,'School')


streets = (
   Street(home, cafe),
   Street(home, restaurant),
   Street(restaurant, home),
   Street(cafe, restaurant),
   Street(restaurant, school),
)

shortest_route = shortest_route(streets, home, school)
print('Shortest Route:')
print(shortest_route)
