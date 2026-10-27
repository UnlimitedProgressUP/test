import json
from openai import OpenAI

client = OpenAI()

# 1. 定义模型可以使用的工具
def add(a, b):
    return a + b

functions = {"add": add}

tools = [{
    "type": "function",
    "name": "add",
    "description": "计算两个数的和",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"},
        },
        "required": ["a", "b"],
        "additionalProperties": False,
    },
    "strict": True,
}]

# 2. 保存对话和工具执行记录
history = [{"role": "user", "content": "请计算 123 + 456"}]

# 3. Agent 循环，限制次数以防无限运行
for _ in range(5):
    response = client.responses.create(
        model="gpt-4.1",
        instructions="你是一个助手，计算加法时必须使用 add 工具。",
        input=history,
        tools=tools,
    )
    history.extend(response.output)

    calls = [item for item in response.output if item.type == "function_call"]

    # 没有工具调用，说明模型已经给出最终回答
    if not calls:
        print(response.output_text)
        break

    # 执行工具，把结果放回历史，供下一轮模型读取
    for call in calls:
        args = json.loads(call.arguments)
        result = functions[call.name](**args)

        history.append({
            "type": "function_call_output",
            "call_id": call.call_id,
            "output": str(result),
        })
else:
    print("已达到最大循环次数")