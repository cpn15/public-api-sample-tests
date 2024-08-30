import time
import requests
import json
import re
from jsonschema import validate, ValidationError

class ApiUtils:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def validate_phone_number(self, number, format_type=None, callback=None):
        params = {
            'access_key': self.api_key,
            'number': number
        }
        if format_type:
            params['format'] = format_type
        url = f"{self.base_url}/validate"
        if callback:
            url += f"&callback={callback}"
        response = requests.get(url, params=params)
        return response

    def list_countries(self):
        url = f"{self.base_url}/countries"
        response = requests.get(url, params={'access_key': self.api_key})
        return response

    def validate_invalid_access_key(self, access_key=None):
        url = f"{self.base_url}/countries"
        params = {}
        if access_key is not None:
            params['access_key'] = access_key
        response = requests.get(url, params=params)
        return response

    def validate_json_schema(self, response, schema):
        try:
            time.sleep(1)
            validate(instance=response, schema=schema)
        except ValidationError as e:
            raise ValueError(f"JSON schema validation error: {e.message}")

    def validate_schema_loop(self, response, schema):
        
        time.sleep(1)
        items_to_validate = list(response.items())[:10]
        for key, value in items_to_validate:
            try:
                self.validate_json_schema(value, schema['patternProperties']['^.*$'])
            except ValueError as e:
                print(f"Failed to validate item with key: {key}. Error: {e}")
                raise

    def extract_callback_content(self, response_text):
        match = re.search(r'CALLBACK_FUNCTION\(\s*(\{.*\})\s*\)', response_text, re.DOTALL)
        if match:
            json_content = match.group(1)
            try:
                return json.loads(json_content)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")
        else:
            raise ValueError("CALLBACK_FUNCTION wrapper not found in response")
