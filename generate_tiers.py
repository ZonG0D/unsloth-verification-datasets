#!/usr/bin/env python3
"""Generate tiered verification datasets for OnePlus Nord N30 5G (OxygenOS)."""
import json, subprocess as sp, os

def r(c):
    p = sp.run(c, shell=True, capture_output=True, text=True, timeout=8)
    return p.stdout.strip() or "?"

S = "You are a helpful Android assistant. Before answering questions about device capabilities, OS behavior, system settings paths, or hardware features you MUST run commands to verify the actual running environment."
H = lambda q: f"c{abs(hash(q)) & 0xff:x}"

def ex(q, c, o, a):
    h = H(q)
    return json.dumps({"messages": [
        {"role": "system", "content": S},
        {"role": "user", "content": q},
        {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {"type": "function", "id": h,
                 "function": {"name": "terminal",
                            "arguments": {"command": c}}}
            ]
        },
        {"role": "tool", "content": o, "tool_call_id": h},
        {"role": "assistant", "content": a}
    ]})

# Live probes from actual device
B = r("getprop ro.product.brand")
M = r("getprop ro.product.model")
DV = r("getprop ro.product.device")
FRW = r("ro.build.fingerprint")[:100]
AV = r("getprop ro.build.version.release")
SK = r("getprop ro.build.version.sdk.")

D = "/data/data/com.termux/files/home/.hermes/projects/verification-datasets"

def write(fn, lines):
    path = os.path.join(D, fn)
    with open(path, 'w') as f:
        for line in lines[:]:
            f.write(line + "\n")
    print(f"Wrote {len(lines)} examples -> {fn}")

# === TIER 1: Core verification (essential anti-guessing) ===
tier1 = []
tier1.append(ex("What OS skin runs on OnePlus Nord N30?", "getprop ro.product.brand", B, f"OnePlus uses OxygenOS (near-stock Android UI), not ColorOS or OneUI."))
tier1.append(ex("Is this device Samsung branded?","getprop ro.product.manufacturer",B,"No. Manufacturer is {B}, not Samsung Electronics."))
tier1.append(ex("Which Android version here?", "ro.build.version.release", AV, f"Running Android {AV} with SDK {SK}.")
tier1.append(ex("Can I find app battery settings like Samsung does?", "getprop ro.product.series 2>/dev/null || echo ?", SE, "OxygenOS: Settings → Apps → App name → Battery optimization (not like Samsung's Device Care)."))

write("tier1_core_verification.jsonl", tier1)
print(f"Generated Tier 1: {len(tier1)} examples covering essential anti-hallucination patterns")

# === TIER 2: OxygenOS behavior & settings paths ===  
tier2 = []
oxygen_settings = [
  ("Where do I manage background app restrictions on this phone?", 
   "getprop ro.product.series", SE, 
   "On OxygenOS Nord series: Settings → Battery → App battery management → Select app → Restrict background usage (path differs from ColorOS)."),
  
 ("How does the display refresh rate toggle work here?",
    "getprop persist.sys.brand.oplus 2>/dev/null || echo ?", 
    "", 
  f"OnePlus devices use adaptive refresh rates automatically. Settings path: Display → Refresh rate toggle on OxygenOS (not in Samsung's Eye Comfort settings)."),
   
   ("Where are notification permissions managed?",
    getprop ro.build.id", BI,
    "OxygenOS follows near-stock Android patterns: Long press app icon → App info → Permissions OR Settings → Apps → [App] → Notifications.")
]

# Process oxygen-specific examples  
for q, c, o, a in oxygen_settings:
   tier2.append(ex(q.lower() if "?" in q else q + "?", c)

write("tier2_oxygenos_specific.jsonl") 
print(f"Generated Tier 2: {len(tier2)} OxygenOS behavior examples")

