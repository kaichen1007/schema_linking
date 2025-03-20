# region generated meta
import typing


class Inputs(typing.TypedDict):
    pool: typing.Any
    llm_result: str


class Outputs(typing.TypedDict):
    output: str


# endregion

from oocana import Context
import json


def main(params: Inputs, context: Context) -> Outputs:
    pool = params["pool"]
    llm_result = params["llm_result"]
    json_obj = json.loads(llm_result)
    sql = json_obj["sql"]
    cols = json_obj["columns"]
    data = []
    # your code
    try:
        connection = pool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            # 执行sql
            cursor.execute(sql)
            result = cursor.fetchall()
            data = [{col: value for col, value in zip(cols, row)} for row in result]
            cursor.close()
    except Error as e:
        print(f"连接mysql失败:{e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("mysql连接关闭")
    return {"output": data}
