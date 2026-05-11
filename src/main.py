"""
Main script
"""
import os
import time
from dotenv import load_dotenv
from database import get_unscreened_listings, mark_listing_screened
from screener import screen_listing
from notifier import send_notification

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "..", "UpworkScraper", "upwork_listings.db")
ntfy_topic = os.getenv("NTFY_TOPIC")

def main():
    listings = get_unscreened_listings(db_path)
    print(f"Found {len(listings)} unscreened listing(s)")

    for listing in listings:
        try:
            result = screen_listing(listing)
            if result.get("passed"): # json.loads in screen_listing turns JSON boolean into Python boolean
                send_notification(
                    title=listing["listing_title"],
                    message=f"Reason: {result.get('reason')}\nURL: {listing.get('listing_url')}",
                    topic=ntfy_topic
                )
        except Exception as e:
            print(f"Error processing listing {listing.get('listing_id')}: {e}")
        finally:
            mark_listing_screened(db_path, listing["listing_id"])
            time.sleep(2)

if __name__ == "__main__":
    main()