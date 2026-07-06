# Unsloth Verification Datasets

## Purpose
Fine-tuning datasets that teach 3B-class models to use terminal commands for actual verification instead of guessing from training priors. Target: fix "static mind" problem where LLM repeats platform/OS/device mistakes.

## Dataset Contents

| File | Examples | Focus Area |
|------|----------|------------|
| `platform_verification.jsonl` | 20 | OS skin detection, brand identification |
| `device_probe.jsonl` | 17 | Hardware facts (RAM, resolution, kernel) |  
| `environment_routing.jsonl` | 6 | System capability verification |
| `tier2_oxygenos_behaviors.jsonl` | 10 | OxygenOS-specific settings & features |
| `tier3_termux_device.jsonl` | 3 | Termux/Android device probes |
| `multi_step_chains.jsonl` | 5 | Chained tool calls (2-3 tools before answer) |
| `direct_text_responses.jsonl` | 6 | Plain text replies without tool calls |

## Format
All files use Unsloth Studio compatible JSONL format with multi-turn conversations including:
- Tool calling chain (terminal command)
- Real output from those commands  
- Final synthesized answer using actual data

## Fixes Applied (2025-07-05)
- **Unique tool call IDs** — all `tc_*` prefixed, globally unique across dataset
- **Richer system prompts** — expanded from 49 chars to match Hermes' actual multi-paragraph system messages
- **Multi-step chains added** — model now learns 2-3 sequential tool calls before answering
- **Direct text responses added** — 6 examples of assistant replying without tools (prevents empty-response bug)
- **Enriched short answers** — responses under 40 chars elaborated to provide more training signal

## Training Recommendations
- **Base model**: Qwen2.5-3B-Instruct or qwen3.6-class models
- **Method**: QLoRA, rank 128 (full fine-tune for <1B parameter models)
- **LR**: 1-2e-4 
- **Epochs**: 2-3 (behavioral routing preference needs more exposure)
- **Batch size**: 4-8 (depends on VRAM)

## Upload to Unsloth Studio
1. Drag `.jsonl` files into Data Recipes panel
2. Select base model from supported list
3. Train with recommended presets above
4. Test via API endpoint or chat interface
