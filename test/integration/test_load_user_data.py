import pytest

from src.loader.load_user_data import load_user_data
from utils.db import WarehouseConnection
from utils.sde_config import get_warehouse_creds


@pytest.fixture()
def set_up_tear_down():
    # Clean up existing data
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        curr.execute("Truncate table housing.user;")
    yield
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        curr.execute("Truncate table housing.user;")


class TestLoadUserData:
    def test_load_user_data(self, set_up_tear_down):
        load_user_data()
        with WarehouseConnection(
            get_warehouse_creds()
        ).managed_cursor() as curr:
            curr.execute("select count(*) from housing.user;")
            d = curr.fetchone()

        assert d[0] == 10
