class Schemas:

    PHONE_NUMBER_SCHEMA = {
        "type": "object",
        "properties": {
            "valid": {"type": "boolean"},
            "number": {"type": "string"},
            "local_format": {"type": "string"},
            "international_format": {"type": "string"},
            "country_prefix": {"type": "string"},
            "country_code": {"type": "string"},
            "country_name": {"type": "string"},
            "location": {"type": "string"},
            "carrier": {"type": "string"},
            "line_type": {"type": "string"}
        },
        "required": ["valid", "number", "local_format", "international_format", \
                    "country_code", "country_name", "country_prefix"],
    }

    INVALID_PHONE_NUMBER_SCHEMA = {
        "type": "object",
        "properties": {
            "valid": {"type": "boolean"},
            "number": {"type": "string"},
            "local_format": {"type": ["string", "null"]},
            "international_format": {"type": ["string", "null"]},
            "country_prefix": {"type": ["string", "null"]},
            "country_code": {"type": ["string", "null"]},
            "country_name": {"type": ["string", "null"]},
            "location": {"type": ["string", "null"]},
            "carrier": {"type": ["string", "null"]},
            "line_type": {"type": ["string", "null"]
    }
        },
        "required": [
            "valid",
            "number"
        ],
        "additionalProperties": False
    }


    LIST_OF_COUNTRIES_SCHEMA = {
        "type": "object",
        "patternProperties": {
            "^.*$": {
                "type": "object",
                "properties": {
                    "country_name": {
                        "type": "string"
                    },
                    "dialling_code": {
                        "type": "string"
                    }
                },
                "required": ["country_name", "dialling_code"]
            }
        },
        "additionalProperties": False
    }