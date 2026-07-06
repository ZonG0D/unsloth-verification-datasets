# Unsloth Verification Datasets

## Purpose
Fine-tuning datasets that teach 3B-class models to use terminal commands for actual verification instead of guessing from training priors. Target: fix "static mind" problem where LLM repeats platform/OS/device mistakes.

## Dataset Contents

| File | Examples | Focus Area |
|------|----------|------------|
| `platform_verification.jsonl` | 20 | OS/brand anti-hallucination |
| `device_probe.jsonl` | 17 | Hardware specs (RAM, kernel, arch) |
| `environment_routing.jsonl` | 6 | Dev tool presence checks |
| `tier2_oxygenos_behaviors.jsonl` | 10 | OxygenOS settings & paths |
| `tier3_termux_device.jsonl` | 3 | Termux sandbox probes |
| `multi_step_chains.jsonl` | 5 | Sequential 2-3 tool calls |
| `multi_step_reasoning.jsonl` | 4 | Intermediate analysis between steps |
| `direct_text_responses.jsonl` | 6 | Plain text replies without tools |
| `mixed_response_routing.jsonl` | 12 | Direct answer vs tool call routing (50/50) |
| `system_prompt_generalization.jsonl` | 6 | Short + full Hermes system prompts |
| `error_handling.jsonl` | 8 | Command failures → graceful responses |
| `meta_conversation.jsonl` | 4 | Multi-turn follow-ups + constraints |

**Total: 101 examples across 12 files**

## Format
All files use Unsloth Studio compatible JSONL format with multi-turn conversations including:
- Tool calling chain (terminal command)
- Real output from those commands  
- Final synthesized answer using actual data

## Fixes Applied (2026-07-06)
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
