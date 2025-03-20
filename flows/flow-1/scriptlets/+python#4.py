# region generated meta
from typing import Any, Callable


import typing
from mysql.connector.pooling import MySQLConnectionPool


class Inputs(typing.TypedDict):
    host: str
    user: str
    pwd: str
    database: str


class Outputs(typing.TypedDict):
    pool:Any

# endregion

from oocana import Context


def main(params: Inputs, context: Context) -> Outputs:

    # your code
    database = params["database"]
    host = params["host"]
    pwd = params["pwd"]
    user = params["user"]

    # 创建连接池
    pool = MySQLConnectionPool(
        pool_name="mypool",
        pool_size=10,
        host=host,
        user=user,
        password=pwd,
        database=database,
    )
    return { "pool": pool}
