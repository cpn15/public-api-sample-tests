import pytest
from resource.test_data import TestData, ExpectedResponse
from resource.schema import Schemas

@pytest.mark.parametrize("number,expected_statuscode,\
                         verification_status, expected_response", [
    (TestData.NUMERIC_VALID_US_PHONE_NUMBER, 200,\
      True, ExpectedResponse.VALID_US_NUMBER_RESPONSE),
    (TestData.SPECIAL_VALID_UK_PHONE_NUMBER, 200, True,\
      ExpectedResponse.VALID_UK_NUMBER_RESPONSE),
])
def test_valid_phone_number(api_utils, number, expected_statuscode,\
                             verification_status, expected_response):
    response = api_utils.validate_phone_number(number)
    assert response.status_code == expected_statuscode

    data = response.json()
    api_utils.validate_json_schema(data, Schemas.PHONE_NUMBER_SCHEMA)

    assert data.get('valid') == verification_status
    assert data == expected_response

@pytest.mark.parametrize("number, expected_statuscode, verification_status", [
    (TestData.INVALID_PHONE_NUMBER_FORMAT, 200, False),
    (TestData.NONEXISTENT_PHONE_NUMBER, 200, False),
])
def test_invalid_phone_number(api_utils, number, expected_statuscode,\
                               verification_status):
    response = api_utils.validate_phone_number(number)
    assert response.status_code == expected_statuscode

    data = response.json()
    api_utils.validate_json_schema(data, Schemas.INVALID_PHONE_NUMBER_SCHEMA)

    assert data.get('valid') == verification_status

@pytest.mark.parametrize("callback,expected_statuscode, format_type" , [
    (TestData.VALID_CALLBACK, 200, 1)
])
def test_jsonp_callback_with_formatting(api_utils, callback, \
                                        expected_statuscode, format_type):
    response = api_utils.validate_phone_number(
        TestData.NUMERIC_VALID_US_PHONE_NUMBER, 
        format_type=format_type,
        callback=callback
    )
    assert response.status_code == expected_statuscode

    data = api_utils.extract_callback_content(response.text)
    api_utils.validate_json_schema(data, Schemas.PHONE_NUMBER_SCHEMA)

def test_list_countries(api_utils):
    response = api_utils.list_countries()
    assert response.status_code == 200
    data = response.json()
    api_utils.validate_schema_loop(data, Schemas.LIST_OF_COUNTRIES_SCHEMA)

@pytest.mark.parametrize("access_key,expected_response", [
    (TestData.INVALID_API_KEY, ExpectedResponse.INVALID_ACCESS_KEY_RESPONSE),
    (TestData.NO_API_KEY, ExpectedResponse.MISSING_ACCESS_KEY_RESPONSE)
])
def test_invalid_access_keys(api_utils, access_key, expected_response):
    response = api_utils.validate_invalid_access_key(access_key)
    assert response.status_code == 200  # Should verify status code as 403 but API gets 200 
    data = response.json()
    assert data == expected_response
