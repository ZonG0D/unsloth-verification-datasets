# Unsloth Verification Datasets 

A specialized collection of high-quality conversational datasets designed for fine-tuning LLMs on agentic workflows, system capability verification, and tool-use precision. All datasets are provided in **ChatML / OpenAI Conversational format**, making them directly compatible with [Unsloth Studio](https://unsloth.ai/) and various training recipes.

## Repository Structure

All datasets are organized in the `data/` directory to separate raw training materials from project documentation.

```text
.
├── README.md # This file
└── data/ # Training Datasets (.jsonl)
 ├── agentic_reasoning.jsonl # Complex multi-step chains
 ├── env_routing.jsonl # Environment capability checks
 ├── error_handling.jsonl # Robustness & fallback handling
 ├── hardware_probe.jsonl # Device/Hardware capabilities
 ├── meta_conversations.jsonl # Conversational meta-interactions
 ├── mixed_routing.jsonl # Complex routing logic
 ├── platform_oxygenos.jsonl # OxygenOS specific behaviors
 ├── platform_termux.jsonl # Termux environment behavior
 ├── platform_verify.jsonl # General platform verification
 ├── sys_prompt_variations.jsonl # System prompt robustness tests
 ├── text_only_replies.jsonl # Direct non-tool responses
 └── tool_execution_chains.jsonl # Standard execution flows
```

## Dataset Taxonomy (Training Objectives)

Use these categories to select specific data slices for focused fine-tuning:

| Category | Datasets | Training Objective |
| :--- | :--- | :--- |
| **Agentic Intelligence** | `agentic_reasoning`, `tool_execution_chains` | Master multi-step tool calling and complex reasoning chains. |
| **System Robustness** | `error_handling`, `sys_prompt_variations` | Teach the model to handle errors gracefully and follow diverse system prompts. |
| **Platform Awareness** | `hardware_probe`, `platform_oxygenos`, `platform_termux`, `platform_verify` | Deep understanding of device hardware, OS behaviors (OxygenOS), and terminal environments. |
| **Conversation Flow** | `meta_conversations`, `text_only_replies`, `mixed_routing` | Improve natural conversational flow, meta-talk, and intelligent response routing. |

## Data Format Specification

Each entry in the `.jsonl` files follows a strict ChatML structure:

```json
{
 "messages": [
 {"role": "system", "content": "...(Expanded Hermes-style Prompt)..."},
 {"role": "user", "content": "...(Natural Language Query)..."},
 {
 "role": "assistant", 
 "content": null, 
 "tool_calls": [{"type": "function", "id": "tc_...", "function": {"name": "...", "arguments": "{...}"}}]
 },
 {"role": "tool", "content": "...(Result)...", "tool_call_id": "tc_..."},
 {"role": "assistant", "content": "...(Final Answer)..."}
 ]
}
```

### Key Technical Improvements (v2.0)
- **Standardized Naming**: Unified `snake_case` naming for easy script integration.
- **Tool ID Integrity**: Guaranteed unique and perfectly matched tool call/response IDs (`tc_***`).
- **Semantic Alignment**: Filenames now match the internal `metadata.category` fields.
- **Zero Duplicates**: Strictly deduplicated across all categories using content hashing.

---
*Maintained for high-precision agent training.*