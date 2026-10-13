# Advanced Multimodal AI (SokoniHub)

## Overview
This repository deploys a cross-modal AI validation pipeline for SokoniHub, combining listing photography metadata tags with textual title descriptions to surface product consistency insights. The system computes alignment metrics using a token-matching engine anchored by clear model declarations. It processes sidecar vision tags and voice note transcripts under zero-cost fallbacks.

## Encoder honesty
- **encoder_pin.json:** Pinned cleanly to `lab-bow-v1` tracking under revision `a4f1082c9e7b23838491cdae021a37c95e6f3322`.
- **Did transformers run?** no (Processed via the standard library tag-intersection proxy fallback).

## Join
- **How to run mismatch.py and check_mismatch.py:** Execute `python mismatch.py` in your terminal to build the database records, then run `python check_mismatch.py` to assert constraints.
- **Gold pair result:** `KND-01` clears safely with no issues; `NK-99` is flagged with an agreement score of `0.0` due to a severe mismatch between its Nike text and sisal image tags.

## Insights
- **Path to insights.json:** Exported directly to `insights.json` in the root working directory.

## Tools
- **hf_pipeline.yaml:** Managed locally via the configuration file `hf_pipeline.yaml`.
- **DALL-E / SD / stub:** stub (Circle matching verification).
- **Provenance path:** Tracked explicitly inside `gen_twin.json` pointing to prompt pins in `generation_prompt.txt`.

## Analytics
- **rates.json (quote n):** Computes overall system metrics across an authentic teaching slice sample size of `n=3`.
- **vocab_gaps:** Outlined transparently inside `vocab_gaps.json` covering regional vocabulary variations like `kiondo`.

## Ethics
- **Link ethics_note.md:** The policy documentation is located at [ethics_note.md](ethics_note.md).
- **Review path in one sentence:** Flagged listings are routed to manual operations workspaces for human verification before any enforcement occurs.

## Fallbacks declared
- [x] no GPU / no transformers
- [x] no OpenAI image key (stub)
- [x] no Whisper (sidecars)
- [x] n is a teaching slice

## Checklist
- [x] NK-99 flagged, KND-01 clear
- [x] outputs/ not mixed into gold images/
- [x] no unhackable claims
- [x] Weeks 5/7/8/9 reuse documented

