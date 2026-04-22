"""
topic_tracker.py — Tracks used topics to avoid repetition
"""
import os, json, datetime, random

USED_FILE = "data/used_topics.json"

CONTENT_TOPICS = {
    "adhd": [
        "10 ADHD productivity hacks that actually work",
        "Why dopamine menus are changing ADHD management",
        "The ADHD tax and how to stop losing money",
        "Best budget trackers for ADHD brains in 2026",
        "How to build a morning routine with ADHD",
        "ADHD and money why budgeting feels impossible",
        "Visual planning tools for neurodivergent people",
        "ADHD friendly meal planning that works",
        "How to use a dopamine menu for daily motivation",
        "ADHD focus supplements that actually help",
    ],
    "business": [
        "How to start a cleaning business with no money",
        "10 tax deductions every freelancer misses",
        "ATS resume tips that get you interviews in 2026",
        "Free business forms every cleaning company needs",
        "How to file taxes as a self-employed freelancer",
        "Starting a side hustle as a cleaning business",
        "Best tools for freelancers working from home",
        "How to get your first cleaning business client",
        "Resume mistakes that get you rejected instantly",
        "How to price your freelance services correctly",
    ],
    "health": [
        "PCOS symptoms nobody talks about",
        "How to track your cycle with PCOS",
        "Hormone health tools that help women with PCOS",
        "PCOS and nutrition what actually works",
        "Managing PCOS symptoms with daily tracking",
        "Best journals for women with hormonal imbalances",
        "Natural ways to boost energy with PCOS",
        "PCOS meal planning made simple",
        "How mitochondrial health affects womens energy",
        "Natural supplements that help with PCOS symptoms",
    ],
    "digital_art": [
        "How to use SVG files for your small business",
        "Best free tools for editing SVG files on Cricut",
        "Drip art logos and why they are trending in 2026",
        "How to customize digital downloads for Cricut",
        "Top digital art trends for small businesses",
        "How to sell SVG files on Etsy successfully",
        "Cricut project ideas using SVG files",
        "How to create a logo for your small business",
    ],
}


def _load():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(USED_FILE):
        return {}
    with open(USED_FILE) as f:
        return json.load(f)


def _save(data):
    os.makedirs("data", exist_ok=True)
    with open(USED_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_fresh_topic(niche):
    used = _load()
    used_for_niche = used.get(niche, [])
    available = [t for t in CONTENT_TOPICS.get(niche, []) if t not in used_for_niche]

    if not available:
        print(f"[Topics] Resetting {niche} pool")
        used_for_niche = []
        available = list(CONTENT_TOPICS.get(niche, ["General tips"]))

    topic = random.choice(available)
    used_for_niche.append(topic)
    used[niche] = used_for_niche
    used["last_updated"] = str(datetime.date.today())
    _save(used)
    print(f"[Topics] ✅ '{topic}'")
    return topic
