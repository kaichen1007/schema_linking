# region generated meta
from ast import List
import typing


class Inputs(typing.TypedDict):
    pool: typing.Any


class Outputs(typing.TypedDict):
    table_info: list[typing.Any]


# endregion

from oocana import Context


def main(params: Inputs, context: Context) -> Outputs:

    pool = params["pool"]

    try:
        connection = pool.get_connection()
        result = []
        if connection.is_connected():
            cursor = connection.cursor()
            # 获取库中所有的表
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for table_name in tables:
                # 获取结构
                cursor.execute(f"SHOW CREATE TABLE {table_name[0]}")
                table_info = cursor.fetchone()
                if table_info:
                    table, create_table_info = table_info
                    # 去除回车 存储到result中
                    result.append(create_table_info.replace("\n", ""))
                # result.update({table_name: columns})
            cursor.close()
    except Error as e:
        print(f"连接mysql失败:{e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("mysql连接关闭")
    return {"table_info": result}
