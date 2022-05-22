import random
from typing import Dict, List, Union

import psycopg2.extras as p
from utils.db import WarehouseConnection
from utils.sde_config import get_warehouse_creds


def _get_user_data_insert_query() -> str:
    return """
    INSERT INTO housing.user(
        id,
        name,
        price
    )
    VALUES (
        %(user_id)s,
        %(user_name)s,
        %(price)s
    )
    """


def get_user_data(num_records: int = 10) -> List[Dict[str, Union[int, str]]]:
    return [
        {
            "user_id": random.randint(1, 10000),
            "user_name": random.choice(
                ["john", "jane", "ash", "misty", "brock"]
            ),
            "price": random.randint(10000, 100000),
        }
        for _ in range(num_records)
    ]


def load_user_data():
    user_data = get_user_data()
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        p.execute_batch(curr, _get_user_data_insert_query(), user_data)


if __name__ == "__main__":
    load_user_data()
