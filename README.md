## API VALIDATION

- **HTTP Status Code:** - **HTTP Status Code:** The script mainly validates for a "200 OK" status, as the API currently only returns this status. However, the script can be extended to handle other status codes such as "201 Created", "400 Bad Request", and "403 Forbidden" if required in the future.

- **Schema Validation:** Validates the response against predefined schemas in `schema.py` to ensure the correct structure and data types.

- **Content Validation:** Uses `pytest` parametrize to compare actual responses with expected values from `test_data.py`, checking both valid and invalid inputs.

- - **API Validation:** Ensures the phone number's validity by checking that the `valid` field in the response is either `True` or `False`. The validation also includes testing various formats, such as numeric and special character formats, to ensure the API correctly handles and accepts different input types as specified in the API documentation.

## TEST CASES OVERVIEW

Below are the test cases covered for NUMVERIFY API. Details such as parameters, steps and expected results are provided on the next section.

| **Test Case**                     | **Type**     |
|---------------------------------- |--------------|
| **Validate Phone Number**         | Positive     |
| **Invalid Phone Number**          | Negative     |
| **JSONP Callback with Formatting**| Positive     |
| **List Countries**                | Positive     |
| **Invalid Access Keys**           | Negative     |


### 1. `test_valid_phone_number`

| **Parameter**           | **Description**                                                                      |
|-------------------------|--------------------------------------------------------------------------------------|
| `number`                | Validates US and UK phone numbers                                                    |
| `expected_statuscode`   | Expected HTTP status code : 200                                                      |
| `verification_status`   | Expects "True" as the test cases uses valid phone numbers                            |
| `expected_response`     | Matches the response with the expected response for a valid US or UK phone number    |

| **Steps**                                                                          | **Expected Result**                              |
|------------------------------------------------------------------------------------|--------------------------------------------------|
| Call `validate_phone_number` with test phone number.                               |                                                  |
| Verify the HTTP status code of the response.                                       | HTTP status code should be 200.                  |
| Validate the JSON schema of the response using `PHONE_NUMBER_SCHEMA`.              | Response should match the `PHONE_NUMBER_SCHEMA`. |
| Check if the `valid` field in the response matches expected `verification_status`. | `valid` field should be equal to "True".         |
| Ensure the entire response matches the `expected_response`.                        | Entire response should match `expected_response`.|

### 2. `test_invalid_phone_number`

| **Parameter**           | **Description**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| `number`                | Validates an invalid phone number format and a non-existent phone number                                         |
| `expected_statuscode`   | Expected HTTP status code : 200 (As designed, gives 200 status code but indicates unverified number information) |
| `verification_status`   | Expects "False" as the test cases uses invalid phone numbers                                                     |

| **Step**                                                                      | **Expected Result**                                          |
|-------------------------------------------------------------------------------|--------------------------------------------------------------|
| Call `validate_phone_number` with the provided phone number.                  | -                                                            |
| Verify the HTTP status code of the response.                                  | HTTP status code should be 200.                              |
| Validate the JSON schema of the response using `INVALID_PHONE_NUMBER_SCHEMA`. | Response should match the `INVALID_PHONE_NUMBER_SCHEMA`.     |
| Check if the `valid` field in the response is `False`.                        | `valid` field should be `False`.                             |


### 3. `test_jsonp_callback_with_formatting`

| **Parameter**           | **Description**                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------|
| `callback`              | Callback function name for JSONP                                                                          |
| `expected_statuscode`   | Expected HTTP status code 200 for successful callback handling                                            |
| `format_type`           | Format type to apply to the response.                                                                     |

| **Step**                                                                                      | **Expected Result**                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Call `validate_phone_number` with the provided callback and format type.                      | HTTP status code should be 200.                                      |
| Extract the JSON content from the callback-wrapped response using `extract_callback_content`. |  JSON content is extracted                                           |
| Validate the JSON schema of the extracted data using `PHONE_NUMBER_SCHEMA`.                   |JSON schema of the extracted data should match `PHONE_NUMBER_SCHEMA`. |

### 4. `test_list_countries`

| **Step**                                                                   | **Expected Result**                                   |
|----------------------------------------------------------------------------|-------------------------------------------------------|
| Call `list_countries` to get the list of countries.                        |                                                       |
| Verify the HTTP status code of the response.                               | HTTP status code should be 200.                       |
| Validate the JSON schema of the response using `LIST_OF_COUNTRIES_SCHEMA`. | Response should match the `LIST_OF_COUNTRIES_SCHEMA`. |

### 5. `test_invalid_access_keys`

| **Parameter**           | **Description**                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------|
| `access_key`            | Access key used for validation (e.g., invalid or missing API key).                                        |
| `expected_response`     | Expected JSON response when the access key is invalid or missing.                                         |

| **Step**                                                            | **Expected Result**                                                   |
|---------------------------------------------------------------------|-----------------------------------------------------------------------|
| Call `validate_invalid_access_key` with the provided access key.    |                                                                       |
| Verify the HTTP status code of the response.                        | HTTP status code should be 200. (I expect 403 but is 200 as designed).|
| Check if the response matches the `expected_response`.              | Response should match the `expected_response`.                        |
