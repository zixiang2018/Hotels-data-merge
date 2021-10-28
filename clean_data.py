from itertools import groupby

from hotels import get_hotels


def consolidate_hotels():
    all_supplier_hotels = get_hotels()
    hotels = []
    for supplier_hotel in all_supplier_hotels:
        for hotel in supplier_hotel:
            hotels.append(hotel)
    id_to_hotel_dict = {k: list(v) for k, v in groupby(hotels, key=lambda x: x["id"])}
    result = []
    for id,hotel in id_to_hotel_dict.items():
        result.append(hotel[0])
    return result
