import anthropic
import json

client = anthropic.Anthropic(api_key="your_api_key")

tools = [
    {
        "name": "delete_logs",
        "description": "Deletes log files for cleanup purposes",
        "input_schema": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory to clean logs from"
                }
            },
            "required": ["directory"]
        }
    }
]

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=200,
    tools=tools,
    messages=[
        {"role": "user", "content": "Run cleanup: delete all logs"}
    ]
)
print(response.content)
