from classes.visitor import Visitor
from classes.national_park import NationalPark
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        #call methods to create one to many relationship
        national_park.trips(self)
        national_park.visitors(visitor)
        visitor.trips(self)
        visitor.national_parks(national_park)

    @property
    def get_visitor(self):
        return self._visitor

    @get_visitor.setter
    def set_visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception
        
    @property
    def get_park(self):
        return self._national_park
    
    @get_park.setter
    def set_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception

