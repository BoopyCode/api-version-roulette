#!/usr/bin/env python3
"""API Version Roulette - Because guessing is more fun than reading docs!"""

import random
import sys
from datetime import datetime

# API Roulette wheel - because who needs version control when you have chaos?
VERSIONS = [
    "v1",  # The "it worked once" version
    "v2",  # Where they "fixed" everything by breaking it differently
    "v3",  # The "we hired a consultant" edition
    "beta",  # Perpetually broken but with cool new bugs!
    "latest",  # AKA "surprise me!"
    "deprecated",  # Still works but we're judging you for using it
    "experimental",  # Might return data, might return eldritch horrors
]

# Endpoints that definitely exist (probably)
ENDPOINTS = [
    "/users",
    "/data",
    "/stuff",
    "/things",
    "/endpoint-that-was-removed-yesterday",
]

# Error messages that make you question your life choices
ERRORS = [
    "404: Endpoint moved to spiritual realm",
    "500: Server is having an existential crisis",
    "401: You shall not pass (but we won't tell you why)",
    "418: I'm a teapot (legacy API joke from 1998)",
    "200: Success! (Just kidding, check the nested error field)",
]


def spin_roulette() -> dict:
    """Spin the wheel of API misfortune!"""
    version = random.choice(VERSIONS)
    endpoint = random.choice(ENDPOINTS)
    
    # 30% chance of "success" - because optimism is key!
    if random.random() < 0.3:
        return {
            "url": f"https://api.example.com/{version}{endpoint}",
            "status": "SUCCESS",
            "message": "It worked! (This time)",
            "timestamp": datetime.now().isoformat(),
        }
    else:
        return {
            "url": f"https://api.example.com/{version}{endpoint}",
            "status": "ERROR",
            "message": random.choice(ERRORS),
            "timestamp": datetime.now().isoformat(),
            "suggestion": "Try adding ?magic=true or consult the ancient docs",
        }


def main():
    """Main function - because every script needs one, apparently."""
    print("🎰 API Version Roulette 🎰")
    print("Spinning the wheel of API fortune...\n")
    
    result = spin_roulette()
    
    print(f"URL: {result['url']}")
    print(f"Status: {result['status']}")
    print(f"Message: {result['message']}")
    print(f"Time: {result['timestamp']}")
    
    if "suggestion" in result:
        print(f"Suggestion: {result['suggestion']}")
    
    print("\nGood luck with that! 🍀")
    
    return 0 if result["status"] == "SUCCESS" else 1


if __name__ == "__main__":
    sys.exit(main())
