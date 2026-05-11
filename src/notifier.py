"""
Notification functions
"""

import requests

def send_notification(title:str, message: str, topic: str, priority: int = 3) -> None:
    response = requests.post(
        url=f"https://ntfy.sh/{topic}",
        data=message.encode("utf-8"),
        headers={
            "Title": title,
            "Priority": str(priority),
            "Tags": "briefcase",
        },
    )
    response.raise_for_status()