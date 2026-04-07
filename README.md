# MCP Security Research

Research project exploring Model Context Protocol (MCP) tool usage 
and related LLM security attacks including prompt injection, 
tool poisoning, and data exfiltration.

---

## What is this project?

This project investigates how AI models interact with external tools 
through MCP, and how attackers can exploit that connection. 
All attacks were tested on Claude (Anthropic) using both the 
Claude.ai chat interface and the Anthropic API via Python.

---

## Files

| File | Description |
|---|---|
| `1_MCP_Summary.pdf` | What MCP is and how LLMs use tools |
| `2_Hands_On_Examples.pdf` | 3 attack interactions tested on Claude with screenshots |
| `2_Hands_On_Examples.md` | Same examples in markdown format with embedded code |
| `3_Attack_Summary.pdf` | What tool poisoning is and why it is dangerous |
| `4_Attack_Dataset.csv` | 5 attack entries with prompts, goals, and categories |
| `5_Final_Report.pdf` | Patterns, effectiveness rankings, and defenses |

---

## Code

All Python scripts are in the `/code` folder:

| Script | Attack Type | What it does |
|---|---|---|
| `prompt_injection.py` | Prompt Injection | Sends malicious prompt to override a system prompt containing a hidden secret |
| `tool_poisoning.py` | Tool Poisoning | Registers a delete_logs MCP tool and sends a destructive prompt to trigger it |
| `data_exfiltration.py` | Data Exfiltration | Registers a get_system_config MCP tool and attempts to retrieve sensitive files |

> Note: Scripts require a valid Anthropic API key to run.
> Replace `"your_api_key"` in each file with your actual key.

---

## Attack Categories Covered

- **Prompt Injection** — Tricks the LLM into ignoring its instructions
- **Tool Poisoning** — Hides malicious instructions inside MCP tool descriptions
- **Data Exfiltration** — Abuses tool calls to retrieve sensitive data

---

## Key Findings

- All three attacks were blocked by Claude's built-in safety guardrails
- Tool poisoning is the most dangerous — hidden in metadata, invisible to users
- Data exfiltration is hardest to detect — disguised as legitimate requests
- No single defense is sufficient — a layered approach is needed

---

## Defenses

1. Allowlist approved MCP tools and verify descriptions at registration
2. Require human approval before executing destructive actions
3. Apply least privilege — tools only access what they need
4. Sanitize inputs and outputs to catch injection patterns
5. Monitor tool calls for unusual or unauthorized behavior

---

## Tools Used

- Claude.ai (chat interface testing)
- Anthropic API (Python-based testing)
- VS Code (Python development)
- Python libraries: `anthropic`, `json`
