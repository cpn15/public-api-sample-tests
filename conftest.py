from resource.api_utils import ApiUtils
import pytest
from config.data import Data

@pytest.fixture(scope='session')
def env():
    return {
        "api_key": Data.API_KEY,
        "base_url": Data.BASE_URL
    }

@pytest.fixture(scope='session')
def api_utils(env):
    return ApiUtils(api_key=env['api_key'], base_url=env['base_url'])
