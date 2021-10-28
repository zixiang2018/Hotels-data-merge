import json
import requests

def get_hotel_structure():
    return {
        "id": "",
        "destination_id": "",
        "name": "",
        "location": {
            "lat": "",
            "lng": "",
            "address": "",
            "city": "",
            "country": ""
        },
        "description": "",
        "amenities": {
            "general": "",
            "room": ""
        },
        "images": {
            "rooms": "",
            "site": "",
            "amenities": ""
        },
        "booking_conditions": ""
    }


def get_hotels_from_sup_1(supplier_hotels):
    hotel_from_source_1 = []
    for hotel in supplier_hotels:
        hotel_dict = get_hotel_structure()
        hotel_dict['id'] = hotel['Id']
        hotel_dict['destination_id'] = hotel['DestinationId']
        hotel_dict['name'] = hotel['Name']
        hotel_dict['location']['lat'] = hotel['Latitude']
        hotel_dict['location']['lng'] = hotel['Longitude']
        hotel_dict['location']['address'] = hotel['Address']
        hotel_dict['location']['city'] = hotel['City']
        hotel_dict['location']['country'] = hotel['Country']
        hotel_dict['description'] = hotel['Description']
        hotel_dict['amenities']['general'] = hotel['Facilities'] # Take it as facilities == general amenities 
        hotel_from_source_1.append(hotel_dict)

    return hotel_from_source_1


def get_hotels_from_sup_2(supplier_hotels):
    hotel_from_source_2 = []
    image_info_list = []
    for hotel in supplier_hotels:
        hotel_dict = get_hotel_structure()
        hotel_dict['id'] = hotel['hotel_id']
        hotel_dict['destination_id'] = hotel['destination_id']
        hotel_dict['name'] = hotel['hotel_name']
        hotel_dict['location']['address'] = hotel['location']['address']
        hotel_dict['location']['country'] = hotel['location']['country']
        hotel_dict['description'] = hotel['details']
        hotel_dict['amenities']['general'] = hotel['amenities']['general']
        hotel_dict['amenities']['room'] = hotel['amenities']['room']
        for link in hotel['images']['rooms']:
            image_info_list.append({'link': link['link'], 'description': link['caption']})
        hotel_dict['images']['rooms'] = image_info_list.copy()
        image_info_list = []

        for link in hotel['images']['site']:
            image_info_list.append({'link': link['link'], 'description': link['caption']})
        hotel_dict['images']['site'] = image_info_list.copy()
        image_info_list = []

        hotel_dict['booking_conditions'] = hotel['booking_conditions']
        hotel_from_source_2.append(hotel_dict)

    return hotel_from_source_2


def get_hotels_from_sup_3(supplier_hotels):
    hotel_from_source_3 = []
    image_info_list = []
    for hotel in supplier_hotels:
        hotel_dict = get_hotel_structure()
        hotel_dict['id'] = hotel['id']
        hotel_dict['destination_id'] = hotel['destination']
        hotel_dict['name'] = hotel['name']
        hotel_dict['location']['lat'] = hotel['lat']
        hotel_dict['location']['lng'] = hotel['lng']
        hotel_dict['location']['address'] = hotel['address']
        hotel_dict['description'] = hotel['info']
        hotel_dict['amenities']['room'] = hotel['amenities']
        for link in hotel['images']['rooms']:
            image_info_list.append({'link': link['url'], 'description': link['description']})
        hotel_dict['images']['rooms'] = image_info_list.copy()
        image_info_list = []

        for link in hotel['images']['amenities']:
            image_info_list.append({'link': link['url'], 'description': link['description']})
        hotel_dict['images']['amenities'] = image_info_list.copy()
        image_info_list = []

        hotel_from_source_3.append(hotel_dict)

    return hotel_from_source_3


def get_hotels():
    suppliers = [get_hotels_from_sup_1(json.loads(requests.get("http://www.mocky.io/v2/5ebbea002e000054009f3ffc").text)),
                   get_hotels_from_sup_2(json.loads(requests.get("http://www.mocky.io/v2/5ebbea102e000029009f3fff").text)),
                   get_hotels_from_sup_3(json.loads(requests.get("http://www.mocky.io/v2/5ebbea1f2e00002b009f4000").text))]
    return suppliers