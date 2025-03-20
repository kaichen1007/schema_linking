# region generated meta
from cmd import PROMPT
from openai._client import OpenAI


import typing


class Inputs(typing.TypedDict):
    table_info: list[typing.Any]
    user_input: str
    model: str
    api_key: str
    base_url: str


class Outputs(typing.TypedDict):
    output: str


# endregion

from oocana import Context
from openai import OpenAI


def main(params: Inputs, context: Context) -> Outputs:
    model = params["model"]
    api_key = params["api_key"]
    base_url = params["base_url"]
    table_info = params["table_info"]
    user_input = params["user_input"]
    json_obj = '{"thoughts":"thoughts summary to say to user","direct_response":"If the context is sufficient to answer user, reply directly without sql","sql":"SQL Query to run","display_type":"Data display method","columns":["All columns in a SQL query"]}'
    PROMPT = f"""
  # 请根据用户选择可用表结构定义来回答用户问题。
  # 表结构的定义：
    {table_info}
  # 约束：
    ## 1. 请根据用户问题理解用户意图，使用给出表结构定义创建一个语法正确的mysql sql，如果不需要sql，则直接回答用户问题。
    ## 2. 除非用户在问题中指定了他希望获得的具体数据行数，否则始终将查询限制为最多50 个结果。
    ## 3. 只能使用表结构信息中提供的表来生成 sql，如果无法根据提供的表结构中生成 sql，请说：“提供的表结构信息不足以生成 sql 查询。” 禁止随意捏造信息。
    ## 4. 请注意生成SQL时不要弄错表和列的关系
    ## 5. 请检查SQL的正确性，并保证正确的情况下优化查询性能
    ## 6. 请使用COMMENT来当做字段的名称，若没有COMMENT则使用字段名称
  # 例：
    SELECT student_id AS student_id, student_name AS 学生姓名, major AS 专业 , year_of_enrollment AS 入学年份, student_age AS 学生年龄 FROM students LIMIT 50;
  # 用户的问题：
    {user_input}
  # 请一步一步思考并按照以下JSON格式回复：
    {json_obj}
  确保返回正确的json并且可以被Python json.loads方法解析。
  """
    print(f"提示词{PROMPT}")
    client: OpenAI = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": user_input},
        ],
    )
    return {"output": completion.choices[0].message.content}
