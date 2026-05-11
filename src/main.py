"""
Main script
"""
import os
from dotenv import load_dotenv
from database import get_unscreened_listings, mark_listing_screened
from screener import screen_listing
from notifier import send_notification

# load_dotenv()
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "..", "UpworkScraper", "upwork_jobs.db")
# ntfy_topic = os.getenv("NTFY_TOPIC")

# def main():
#     listings = get_unscreened_listings(db_path)
#     print(f"Found {len(listings)} unscreened listing(s)")

#     for listing in listings:
#         try:
#             result = screen_listing(listing)
#             if result.get("passed"): # json.loads in screen_listing turns JSON boolean into Python boolean
#                 send_notification(
#                     title=listing
#                 )