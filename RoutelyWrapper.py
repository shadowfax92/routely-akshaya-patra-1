from MapsRequestAPI import  *
from DBStuffAPI import *
from XlsxReader import *

center_1_latlng = {}
center_1_latlng['lat'] = 13.001658
center_1_latlng['lng'] = 77.551099

class XlxsToMapsWrapper:
    LAT_LOG_FILE_NAME = '../akshaya-patra-data/lon and log details-xls.xlsx'
    def __init__(self):
        self.lat_lng_db = LngLatDB()
        pass

    def getLatLngData(self, file_name=LAT_LOG_FILE_NAME):
        self.rows = readXlsx(file_name, sheet=1, header=True)
        self.lat_lng_db.add_to_db(self.rows)


class GetAndStoreCost:
    def __init__(self):
        self.lat_lng_db = LngLatDB()
        self.lat_lng_cost_db = LngLatCostDB()
        self.maps_request_api = MapsAPI()
        pass

    def compute_costs(self):
        all_rows_list = self.lat_lng_db.get_all()
        #print all_rows_list[0:4]
        count = 0
        for row in all_rows_list:
            if u'log' in row and u'lon' in row:
                lng = row[u'log']
                lat = row[u'lon']
                dest_coor = {}
                dest_coor['lat'] = lat
                dest_coor['lng'] = lng
                print dest_coor
                cost = self.maps_request_api.get_cost_from_coor(origin_coor=center_1_latlng, dest_coor=dest_coor)
                print cost

            if count == 4:
                break
            count += 1



def main():
    xlxs_to_maps = XlxsToMapsWrapper()
    xlxs_to_maps.getLatLngData()

    # Compute the cost of all Schools from all centers for clustering
    get_and_store_cost = GetAndStoreCost()
    get_and_store_cost.compute_costs()

    return

if __name__ == '__main__':
    main()
