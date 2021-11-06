import requests
import json
from jsonschema import validate
from jsonschema import Draft4Validator

schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "destination_id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "location": {
          "type": "object",
          "properties": {
            "lat": {
              "type": "number"
            },
            "lng": {
              "type": "number"
            },
            "address": {
              "type": "string"
            },
            "city": {
              "type": "string"
            },
            "country": {
              "type": "string"
            }
          },
          "required": [
            "lat",
            "lng",
            "address",
            "city",
            "country"
          ]
        },
        "description": {
          "type": "string"
        },
        "amenities": {
          "type": "object",
          "properties": {
            "general": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "room": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            }
          },
          "required": [
            "general",
            "room"
          ]
        },
        "images": {
          "type": "object",
          "properties": {
            "rooms": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "link": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "link",
                    "description"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "link": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "link",
                    "description"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "link": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "link",
                    "description"
                  ]
                }
              ]
            },
            "site": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "link": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "link",
                    "description"
                  ]
                }
              ]
            },
            "amenities": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "link": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "link",
                    "description"
                  ]
                }
              ]
            }
          },
          "required": [
            "rooms",
            "site",
            "amenities"
          ]
        },
        "booking_conditions": {
          "type": "array",
          "items": [
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            },
            {
              "type": "string"
            }
          ]
        }
      },
      "required": [
        "id",
        "destination_id",
        "name",
        "location",
        "description",
        "amenities",
        "images",
        "booking_conditions"
      ]
    }
  ]
}

host_url = "http://localhost:5000"

def test_retrieve_hotels():
    response = requests.get(host_url+"/retrieve_hotels")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    resp_body = response.json()
    validate(instance=resp_body, schema=schema)