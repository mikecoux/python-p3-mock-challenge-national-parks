class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    # @property
    def get_name(self):
        return self._name

    # @get_name.setter
    def set_name(self, name):
        if not hasattr(self, "name") and isinstance(name, str):
            self._name = name
        else:
            raise Exception("National Parks cannot be renamed.")
        
    name = property(get_name, set_name)

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)
        return set(self._visitors)
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        most_visits = 0
        best_visitor = None
        for visitor in self._visitors:
            visit_count = self._visitors.count(visitor)
            if visit_count > most_visits:
                most_visits = visit_count
                best_visitor = visitor

        return best_visitor