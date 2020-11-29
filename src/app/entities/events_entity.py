import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.opendata as opendata


class EventsList:
    def __init__(self):
        self.events = opendata.parse_csv_data_events()

    def get_all(self):
        return self.events

    def get_by_activity_id(self, activity_id: str):
        if isinstance(activity_id, str):
            return self.events.get(activity_id)
        else:
            return activity_id

    def get_id_by_name(self, event_name: str):
        for e_id in self.events:
            if self.events.get(e_id)['NOMBRE'] == event_name:
                return e_id
        return f'"{event_name}" not found in events 2020.'

    def get_id_by_event_id(self, event_id: str):
        for e_id in self.events:
            if self.events.get(e_id)['ID_EVENTO'] == event_id:
                return e_id
        return f'An event with the ID: {event_id} has not been found.'
    
    def get_id_by_location_id(self, location_id: str):
        for e_id in self.events:
            if self.events.get(e_id)['ID_LUGAR'] == location_id:
                return e_id
        return f'An event with the loation ID: {location_id} has not been found.'
    
    def get_id_by_category(self, category: str):
        for e_id in self.events:
            if self.events.get(e_id)['CATEGORIA'] == category:
                return e_id
        return f'An event with the category: {category} has not been found.'
    