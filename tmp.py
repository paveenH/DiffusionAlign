#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 16:44:13 2025

@author: paveenhuang
"""

from transformers import AutoModelForCausalLM

m = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.3")
print(f"Number of layers: {len(m.model.layers)}")

for i, layer in enumerate(m.model.layers):
    print(f"Layer {i}: {layer.__class__.__name__}")
    
# for name, module in m.named_modules():
#     if name.startswith("model.layers."):
#         print(name)