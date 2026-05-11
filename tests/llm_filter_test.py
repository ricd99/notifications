import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import json
from llm_filter import screen_listing

with open("../data/consts/test_listings.json") as f:
    test_listings = json.load(f)

for listing in test_listings:
    result = screen_listing(test_listing)
    print(result)