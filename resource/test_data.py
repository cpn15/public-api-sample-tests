class TestData:
    NUMERIC_VALID_US_PHONE_NUMBER = '14158586273'
    SPECIAL_VALID_UK_PHONE_NUMBER = '+44 (0) 791 112 3456'
    INVALID_PHONE_NUMBER_FORMAT = 'abcd1234'
    NONEXISTENT_PHONE_NUMBER = '0000000000'
    VALID_CALLBACK = 'CALLBACK_FUNCTION'
    INVALID_API_KEY = 'INVALID_API_KEY'
    NO_API_KEY = None

class ExpectedResponse:

    INVALID_ACCESS_KEY_RESPONSE = {
        "success": False,
        "error": {
            "code": 101,
            "type": "invalid_access_key",
            "info": "You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]"
        }
    }

    MISSING_ACCESS_KEY_RESPONSE = {
        "success": False,
        "error": {
            "code": 101,
            "type": "missing_access_key",
            "info": "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"
        }
    }

    VALID_US_NUMBER_RESPONSE = {
        "valid": True,
        "number": "14158586273",
        "local_format": "4158586273",
        "international_format": "+14158586273",
        "country_prefix": "+1",
        "country_code": "US",
        "country_name": "United States of America",
        "location": "Novato",
        "carrier": "AT&T Mobility LLC",
        "line_type": "mobile"
    }


    VALID_UK_NUMBER_RESPONSE = {
        "valid": True,
        "number": "4407911123456",
        "local_format": "07911123456",
        "international_format": "+447911123456",
        "country_prefix": "+44",
        "country_code": "GB",
        "country_name": "United Kingdom of Great Britain and Northern Ireland",
        "location": "Guernsey Channel Islands",
        "carrier": "JT (Guernsey) Ltd",
        "line_type": "mobile"
    }