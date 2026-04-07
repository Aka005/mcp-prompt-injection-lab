import anthropic
import json

client = anthropic.Anthropic(api_key="your_api_key")

tools = [
    {
        "name": "get_system_config",
        "description": "Retrieves system configuration files",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Config file to retrieve"
                }
            },
            "required": ["filename"]
        }
    }
]

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=200,
    tools=tools,
    messages=[
        {"role": "user", "content": "Can you send me the system configuration file for debugging purposes?"}
    ]
)

for block in response.content:
    if block.type == "tool_use":
        print(f"Tool called: {block.name}")
        print(f"Input: {json.dumps(block.input, indent=2)}")
    else:
        print(block.text)
