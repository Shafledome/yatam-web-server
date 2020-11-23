import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utilities.opendata as opendata


class TrafficList:
    def __init__(self):
        self.traffic_cuts = opendata.parse_traffic_json_data()

    def get_all(self):
        return self.traffic_cuts

    def get_by_id(self, traffic_cut_id: int):
        if isinstance(traffic_cut_id, int):
            return self.traffic_cuts.get(traffic_cut_id)
        else:
            return traffic_cut_id

    def get_id_by_name(self, traffic_cut_name: str):
        for tc_id in self.traffic_cuts:
            if self.traffic_cuts.get(tc_id)['name'] == traffic_cut_name:
                return tc_id
        return f'"{traffic_cut_name}" not found in traffic cuts.'

    def get_id_by_coordinates(self, latitude: float, longitude: float):
        for tc_id in self.traffic_cuts:
            if self.traffic_cuts.get(tc_id)['coordinates'] == [latitude, longitude]:
                return tc_id
        return f'A traffic cut with the coordinates: {latitude, longitude} has not being found.'
