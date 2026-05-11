"""
Main script
"""

import os

from database import get_unscreened_listings, mark_listing_screened
from screener import screen_listing
from notifier import send_notification