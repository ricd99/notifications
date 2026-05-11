import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import json
from llm_filter import screen_listing
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "..", "data", "consts", "test_listings.json"), "r") as f:
    test_listings = json.load(f)

for listing in test_listings:
    result = screen_listing(listing)
    print(result)