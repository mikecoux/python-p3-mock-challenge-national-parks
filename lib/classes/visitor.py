class Visitor:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_parks = []

    # @property
    def get_name(self):
        return self._name

    # @get_name.setter
    def set_name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 15 and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception
        
    name = property(get_name, set_name)

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks:
            self._national_parks.append(new_national_park)
        return self._national_parks