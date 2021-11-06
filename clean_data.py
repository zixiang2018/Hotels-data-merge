from itertools import groupby
from hotels import get_hotels
import json

def consolidate_hotels():
    # Get hotels
    all_supplier_hotels = get_hotels()
    hotels = []

    # Merge all the hotels
    for supplier_hotel in all_supplier_hotels:
        for hotel in supplier_hotel:
            hotels.append(hotel)

    # Group the hotels by its ID to merge duplicated hotels with same name
    id_to_hotel_dict = {k: list(v) for k, v in groupby(hotels, key=lambda x: x["id"])}

    # Prepare data for returning
    result = []
    for id,hotel in id_to_hotel_dict.items():
        result.append(hotel[0])
    return result
