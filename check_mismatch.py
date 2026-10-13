"""
SokoniHub System Gold Pair Test Assertion Driver
Verifies full marks rubric criteria for KND-01 (clear) and NK-99 (flagged).
"""
import sys
from mismatch import run_catalog_pipeline

def verify_gold_pair_behavior():
    print("=== Executing Gold Pair Cross-Modal Assertions ===")
    
    # Execute the processing pipeline
    report = run_catalog_pipeline(catalog_path="catalog.json", threshold=0.25)
    insights = report["insights"]
    
    knd_checked = False
    nk_checked = False
    
    for entry in insights:
        if entry["sku"] == "KND-01":
            # KND-01 must clear out fine without flags
            assert entry["mismatch_flagged"] is False, "Gold Check Failure: KND-01 should pass safely!"
            assert entry["agreement_score"] > 0.80, "Gold Check Failure: KND-01 mapping score is too low!"
            knd_checked = True
            print("✓ Gold Pair Assertion Pass: KND-01 cleared safely with high consistency score.")
            
        if entry["sku"] == "NK-99":
            # NK-99 matches sisal tags against Nike text -> Must flag a mismatch instantly
            assert entry["mismatch_flagged"] is True, "Gold Check Failure: NK-99 must be flagged as a mismatch!"
            assert entry["agreement_score"] == 0.0, "Gold Check Failure: NK-99 mismatch score must be 0.0!"
            nk_checked = True
            print("✓ Gold Pair Assertion Pass: NK-99 correctly caught and flagged for severe cross-modal mismatch.")

    if not (knd_checked and nk_checked):
        print("CRITICAL LOGIC FAILURE: Golden SKUs missing from the matching cycle.", file=sys.stderr)
        sys.exit(1)
        
    print("=== [ALL MULTIMODAL GOLD ASSERTIONS RETURNED GREEN MARKS] ===")

if __name__ == "__main__":
    verify_gold_pair_behavior()
