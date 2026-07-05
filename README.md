# Unsloth Verification Datasets

## Purpose
Fine-tuning datasets that teach 3B-class models to use terminal commands for actual verification instead of guessing from training priors. Target: fix "static mind" problem where LLM repeats platform/OS/device mistakes.

## Dataset Contents

| File | Examples | Focus Area |
|------|----------|------------|
| `platform_verification.jsonl` | 12 | OS skin detection, brand identification |
| `device_probe.jsonl` | 10 | Hardware facts (RAM, resolution, kernel) |  
| `environment_routing.jsonl` | 8 | System capability verification |
| `tool_selection.jsonl` | 15 | Natural question → tool routing vs knowledge |

## Format
All files use Unsloth Studio compatible JSONL format with multi-turn conversations including:
- Tool calling chain (terminal command)
- Real output from those commands  
- Final synthesized answer using actual data

## Training Recommendations
- **Base model**: Qwen2.5-3B-Instruct or Phi-3.5-mini-instruct
- **Method**: QLoRA, rank 64-128
- **LR**: 2e-4 
- **Epochs**: 1-2 (behavioral routing preference)
- **Batch size**: 4-8 (depends on VRAM)

## Upload to Unsloth Studio
1. Drag `.jsonl` files into Data Recipes panel
2. Select base model from supported list
3. Train with recommended presets above
4. Test via API endpoint or chat interface
