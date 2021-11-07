# Hotels-data-merge

# To start API
```bash
py main.py
```

# To run test
```bash
cd ./test
pytest api_test.py
```

# To run docker
```bash
deploy.bat
```

# Retrieve all hotels
```http
GET /api/retrieve_all_hotels
```
### Sample response
```json
[
  {
    "id": "iJhz",
    "destination_id": 5432,
    "name": "Beach Villas Singapore",
    "location": {
      "lat": 1.264751,
      "lng": 103.824006,
      "address": "8 Sentosa Gateway, Beach Villas, 098269",
      "city": "Singapore",
      "country": "Singapore"
    },
    "description": "Surrounded by tropical gardens, these upscale villas in elegant Colonial-style buildings are part of the Resorts World Sentosa complex and a 2-minute walk from the Waterfront train station. Featuring sundecks and pool, garden or sea views, the plush 1- to 3-bedroom villas offer free Wi-Fi and flat-screens, as well as free-standing baths, minibars, and tea and coffeemaking facilities. Upgraded villas add private pools, fridges and microwaves; some have wine cellars. A 4-bedroom unit offers a kitchen and a living room. There's 24-hour room and butler service. Amenities include posh restaurant, plus an outdoor pool, a hot tub, and free parking.",
    "amenities": {
      "general": ["outdoor pool", "indoor pool", "business center", "childcare", "wifi", "dry cleaning", "breakfast"],
      "room": ["aircon", "tv", "coffee machine", "kettle", "hair dryer", "iron", "bathtub"]
    },
    "images": {
      "rooms": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/3.jpg", "description": "Double room" },
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg", "description": "Bathroom" }
      ],
      "site": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/1.jpg", "description": "Front" }
      ],
      "amenities": [
        { "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg", "description": "RWS" }
      ]
    },
    "booking_conditions": [
      "All children are welcome. One child under 12 years stays free of charge when using existing beds. One child under 2 years stays free of charge in a child's cot/crib. One child under 4 years stays free of charge when using existing beds. One older child or adult is charged SGD 82.39 per person per night in an extra bed. The maximum number of children's cots/cribs in a room is 1. There is no capacity for extra beds in the room.",
      "Pets are not allowed.",
      "WiFi is available in all areas and is free of charge.",
      "Free private parking is possible on site (reservation is not needed).",
      "Guests are required to show a photo identification and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Payment before arrival via bank transfer is required. The property will contact you after you book to provide instructions. Please note that the full amount of the reservation is due before arrival. Resorts World Sentosa will send a confirmation with detailed payment information. After full payment is taken, the property's details, including the address and where to collect keys, will be emailed to you. Bag checks will be conducted prior to entry to Adventure Cove Waterpark. === Upon check-in, guests will be provided with complimentary Sentosa Pass (monorail) to enjoy unlimited transportation between Sentosa Island and Harbour Front (VivoCity). === Prepayment for non refundable bookings will be charged by RWS Call Centre. === All guests can enjoy complimentary parking during their stay, limited to one exit from the hotel per day. === Room reservation charges will be charged upon check-in. Credit card provided upon reservation is for guarantee purpose. === For reservations made with inclusive breakfast, please note that breakfast is applicable only for number of adults paid in the room rate. Any children or additional adults are charged separately for breakfast and are to paid directly to the hotel."
    ]
  }
]
```

# Retrieve all hotels by ID
```http
POST /api/retrieve_hotels_by_ids
```

**Request body**
```json
{ "hotel_ids" : ["iJhz","f8c9"]}
```

### Sample response
```json
[
    {
        "amenities": {
            "general": [],
            "room": [
                "Aircon",
                "Tv",
                "Coffee machine",
                "Kettle",
                "Hair dryer",
                "Iron",
                "Tub"
            ]
        },
        "booking_conditions": [],
        "description": "Located at the western tip of Resorts World Sentosa, guests at the Beach Villas are guaranteed privacy while they enjoy spectacular views of glittering waters. Guests will find themselves in paradise with this series of exquisite tropical sanctuaries, making it the perfect setting for an idyllic retreat. Within each villa, guests will discover living areas and bedrooms that open out to mini gardens, private timber sundecks and verandahs elegantly framing either lush greenery or an expanse of sea. Guests are assured of a superior slumber with goose feather pillows and luxe mattresses paired with 400 thread count Egyptian cotton bed linen, tastefully paired with a full complement of luxurious in-room amenities and bathrooms boasting rain showers and free-standing tubs coupled with an exclusive array of ESPA amenities and toiletries. Guests also get to enjoy complimentary day access to the facilities at Asia’s flagship spa – the world-renowned ESPA.",
        "destination_id": 5432,
        "id": "iJhz",
        "images": {
            "amenities": [
                {
                    "description": "RWS",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg"
                },
                {
                    "description": "Sentosa Gateway",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg"
                }
            ],
            "rooms": [
                {
                    "description": "Double room",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg"
                },
                {
                    "description": "Bathroom",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg"
                }
            ],
            "site": []
        },
        "location": {
            "address": "8 Sentosa Gateway, Beach Villas, 098269",
            "city": "",
            "country": "",
            "lat": 1.264751,
            "lng": 103.824006
        },
        "name": "Beach Villas Singapore"
    },
    {
        "amenities": {
            "general": [],
            "room": null
        },
        "booking_conditions": [],
        "description": null,
        "destination_id": 1122,
        "id": "f8c9",
        "images": {
            "amenities": [
                {
                    "description": "Bar",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i57_m.jpg"
                }
            ],
            "rooms": [
                {
                    "description": "Suite",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i10_m.jpg"
                },
                {
                    "description": "Suite - Living room",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/YwAr/i11_m.jpg"
                }
            ],
            "site": []
        },
        "location": {
            "address": null,
            "city": "",
            "country": "",
            "lat": 35.6926,
            "lng": 139.690965
        },
        "name": "Hilton Tokyo Shinjuku"
    }
]
```

# Retrieve all hotels by destination IDs
```http
POST /api/retrieve_hotels_by_destinations
```

**Request body**
```json
{ "destination_ids" : [5432]}
```

### Sample response
```json
[
    {
        "amenities": {
            "general": [],
            "room": [
                "Aircon",
                "Tv",
                "Coffee machine",
                "Kettle",
                "Hair dryer",
                "Iron",
                "Tub"
            ]
        },
        "booking_conditions": [],
        "description": "Located at the western tip of Resorts World Sentosa, guests at the Beach Villas are guaranteed privacy while they enjoy spectacular views of glittering waters. Guests will find themselves in paradise with this series of exquisite tropical sanctuaries, making it the perfect setting for an idyllic retreat. Within each villa, guests will discover living areas and bedrooms that open out to mini gardens, private timber sundecks and verandahs elegantly framing either lush greenery or an expanse of sea. Guests are assured of a superior slumber with goose feather pillows and luxe mattresses paired with 400 thread count Egyptian cotton bed linen, tastefully paired with a full complement of luxurious in-room amenities and bathrooms boasting rain showers and free-standing tubs coupled with an exclusive array of ESPA amenities and toiletries. Guests also get to enjoy complimentary day access to the facilities at Asia’s flagship spa – the world-renowned ESPA.",
        "destination_id": 5432,
        "id": "iJhz",
        "images": {
            "amenities": [
                {
                    "description": "RWS",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg"
                },
                {
                    "description": "Sentosa Gateway",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg"
                }
            ],
            "rooms": [
                {
                    "description": "Double room",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg"
                },
                {
                    "description": "Bathroom",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg"
                }
            ],
            "site": []
        },
        "location": {
            "address": "8 Sentosa Gateway, Beach Villas, 098269",
            "city": "",
            "country": "",
            "lat": 1.264751,
            "lng": 103.824006
        },
        "name": "Beach Villas Singapore"
    },
    {
        "amenities": {
            "general": [
                "outdoor pool",
                "business center",
                "childcare",
                "parking",
                "bar",
                "dry cleaning",
                "wifi",
                "breakfast",
                "concierge"
            ],
            "room": [
                "aircon",
                "minibar",
                "tv",
                "bathtub",
                "hair dryer"
            ]
        },
        "booking_conditions": [],
        "description": "InterContinental Singapore Robertson Quay is luxury's preferred address offering stylishly cosmopolitan riverside living for discerning travelers to Singapore. Prominently situated along the Singapore River, the 225-room inspiring luxury hotel is easily accessible to the Marina Bay Financial District, Central Business District, Orchard Road and Singapore Changi International Airport, all located a short drive away. The hotel features the latest in Club InterContinental design and service experience, and five dining options including Publico, an Italian landmark dining and entertainment destination by the waterfront.",
        "destination_id": 5432,
        "id": "SjyX",
        "images": {
            "amenities": "",
            "rooms": [
                {
                    "description": "Double room",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i93_m.jpg"
                },
                {
                    "description": "Bathroom",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i94_m.jpg"
                }
            ],
            "site": [
                {
                    "description": "Restaurant",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i1_m.jpg"
                },
                {
                    "description": "Hotel Exterior",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i2_m.jpg"
                },
                {
                    "description": "Entrance",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i5_m.jpg"
                },
                {
                    "description": "Bar",
                    "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i24_m.jpg"
                }
            ]
        },
        "location": {
            "address": "1 Nanson Rd, Singapore 238909",
            "city": "",
            "country": "Singapore",
            "lat": "",
            "lng": ""
        },
        "name": "InterContinental"
    }
]
```