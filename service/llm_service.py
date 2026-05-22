from openai import OpenAI # pyright: ignore[reportMissingImports]
from config import llm_config

client = OpenAI(
    api_key= llm_config.api_key,
    base_url = llm_config.base_url)


def call_llm(question:str):
    if(question.strip() == "" or question == None):
        return {"success":False,"error":"请输入问题"}

    try :
        response = client.chat.completions.create(
            model = "deepseek-v4-pro",
            messages = [
                {"role":"system","content":"you are a helpful asistent"},
                {"role":"user","content":question}
            ],
            stream = False,
            reasoning_effort = "high",
            extra_body = {"thinking":{"type":"enabled"}}
            )
        return {"answer":response.choices[0].message.content}
    except Exception as e:
        print(e)
        return{"success":False,"error":"请输入问题"}