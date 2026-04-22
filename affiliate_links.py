"""
affiliate_links.py
All affiliate links — Digistore24 + Amazon + Etsy
"""

DIGISTORE_ID = "Ahfirnet"
AMAZON_TAG   = "hitorica-20"
ETSY_SHOP    = "https://www.etsy.com/shop/DreamHausDigital"


def amz(asin: str) -> str:
    return f"https://www.amazon.com/dp/{asin}?tag={AMAZON_TAG}"


# ── DIGISTORE24 PRODUCTS ──────────────────────────────────
# Each product has its own unique URL
DIGISTORE_PRODUCTS = {
    "health": [
        {
            "title":      "Advanced Amino — Stop Muscle Loss",
            "url":        "https://www.advancedbionutritionals.com/DS24/Advanced-Amino/Muscle-Mass-Loss/HD.htm#aff=Ahfirnet",
            "commission": "40%+",
            "cta":        "Stop muscle loss and feel stronger at any age — natural solution",
            "image":      "health supplement muscle strength natural",
        },
        {
            "title":      "Advanced Mitochondrial Formula — Beat Fatigue",
            "url":        "https://www.advancedbionutritionals.com/DS24/Advanced-Mitochondrial/Too-Tired-To-Enjoy-It/HD.htm#aff=Ahfirnet",
            "commission": "40%+",
            "cta":        "Too tired to enjoy life? Fix your energy at the cellular level",
            "image":      "energy fatigue tired woman natural supplement",
        },
        {
            "title":      "Pineal Guardian — Brain & Sleep Support",
            "url":        "https://pinealguardianvip.com/ds/indexts.php#aff=Ahfirnet",
            "commission": "40%+",
            "cta":        "Unlock deep sleep and razor sharp focus naturally",
            "image":      "brain health sleep focus natural supplement",
        },
    ],
    "adhd": [
        {
            "title":      "Pineal Guardian — Focus & Clarity",
            "url":        "https://pinealguardianvip.com/ds/indexts.php#aff=Ahfirnet",
            "commission": "40%+",
            "cta":        "Struggling to focus? This natural formula supports brain clarity",
            "image":      "brain focus clarity ADHD natural supplement",
        },
        {
            "title":      "Advanced Mitochondrial — Energy & Focus",
            "url":        "https://www.advancedbionutritionals.com/DS24/Advanced-Mitochondrial/Too-Tired-To-Enjoy-It/HD.htm#aff=Ahfirnet",
            "commission": "40%+",
            "cta":        "Low energy killing your productivity? Fix it at the source",
            "image":      "energy productivity focus brain natural",
        },
    ],
    "business": [
        {
            "title":      "Digital Business Course",
            "url":        "https://www.checkout-ds24.com/redir/577873/Ahfirnet/",
            "commission": "50%+",
            "cta":        "Build a profitable online business starting today",
            "image":      "online business laptop success entrepreneur",
        },
        {
            "title":      "Advanced Amino — Stay Sharp Running Your Business",
            "url":        "https://www.advancedbionutritionals.com/DS24/Advanced-Amino/Muscle-Mass-Loss/HD.htm#aff=Ahfirnet",
            "commission": "40%+",
            "cta":        "Busy entrepreneurs need to stay strong and focused",
            "image":      "entrepreneur health energy business success",
        },
    ],
    "digital_art": [
        {
            "title":      "Digital Business & Design Course",
            "url":        "https://www.checkout-ds24.com/redir/577873/Ahfirnet/",
            "commission": "50%+",
            "cta":        "Turn your design skills into a full-time online income",
            "image":      "digital design course online income laptop",
        },
        {
            "title":      "Pineal Guardian — Creative Flow & Focus",
            "url":        "https://pinealguardianvip.com/ds/indexts.php#aff=Ahfirnet",
            "commission": "40%+",
            "cta":        "Unlock your creative potential with better brain health",
            "image":      "creative focus brain art design natural",
        },
    ],
}

# ── AMAZON PRODUCTS ───────────────────────────────────────
AMAZON_PRODUCTS = {
    "adhd": [
        {"title": "The ADHD Advantage Book",     "url": amz("1583335080"), "price": "$15"},
        {"title": "ADHD Planner for Adults",     "url": amz("B09ADHD123"), "price": "$14"},
        {"title": "Focus Timer for ADHD",        "url": amz("B07FOCUS12"), "price": "$25"},
    ],
    "business": [
        {"title": "Self-Employed Tax Guide",     "url": amz("1260462021"), "price": "$20"},
        {"title": "Small Business Planner",      "url": amz("B08BIZPLAN"), "price": "$16"},
        {"title": "Profit First for Business",   "url": amz("073521414X"), "price": "$18"},
    ],
    "health": [
        {"title": "PCOS Diet & Wellness Book",   "url": amz("1628602120"), "price": "$18"},
        {"title": "Hormone Balance Journal",     "url": amz("B09HORMONE"), "price": "$12"},
        {"title": "Women Health Tracker",        "url": amz("B08HEALTH1"), "price": "$14"},
    ],
    "digital_art": [
        {"title": "Cricut Joy Machine",          "url": amz("B09CRICUT1"), "price": "$179"},
        {"title": "Procreate for iPad Guide",    "url": amz("B09PROCRT1"), "price": "$20"},
    ],
}

# ── ETSY PRODUCTS ─────────────────────────────────────────
ETSY_PRODUCTS = [
    {
        "title":    "ADHD Dopamine Menu Template",
        "url":      "https://www.etsy.com/listing/4322772731",
        "price":    "$3.24",
        "niche":    "adhd",
        "keywords": ["ADHD", "dopamine menu", "neurodivergent", "productivity", "planner"],
    },
    {
        "title":    "ADHD Budget Tracker",
        "url":      "https://www.etsy.com/listing/4322774440",
        "price":    "$12.99",
        "niche":    "adhd",
        "keywords": ["ADHD", "budget tracker", "money planner", "neurodivergent", "finance"],
    },
    {
        "title":    "Neurodivergent Wellness Bundle",
        "url":      "https://www.etsy.com/listing/4341458916",
        "price":    "$8.99",
        "niche":    "adhd",
        "keywords": ["neurodivergent", "wellness", "ADHD", "planner", "bundle"],
    },
    {
        "title":    "PCOS Hormone Health Kit",
        "url":      "https://www.etsy.com/listing/4375567104",
        "price":    "$9.99",
        "niche":    "health",
        "keywords": ["PCOS", "hormone", "health tracker", "cycle tracker", "women health"],
    },
    {
        "title":    "Cleaning Business Starter Pack",
        "url":      "https://www.etsy.com/listing/4343414380",
        "price":    "$10.99",
        "niche":    "business",
        "keywords": ["cleaning business", "business forms", "small business", "printable"],
    },
    {
        "title":    "Freelancer Tax Prep Kit",
        "url":      "https://www.etsy.com/listing/4344064784",
        "price":    "$9.69",
        "niche":    "business",
        "keywords": ["freelancer", "tax", "self employed", "deductions", "tax prep"],
    },
    {
        "title":    "Modern ATS Resume Template",
        "url":      "https://www.etsy.com/listing/4343163615",
        "price":    "$6.99",
        "niche":    "business",
        "keywords": ["resume template", "ATS resume", "job application", "CV template"],
    },
    {
        "title":    "Melting Headphones Logo SVG",
        "url":      "https://www.etsy.com/listing/4343397375",
        "price":    "$1.72",
        "niche":    "digital_art",
        "keywords": ["SVG", "logo", "headphones", "drip art", "digital download"],
    },
]


def get_links_for_niche(niche: str) -> dict:
    return {
        "etsy":      [p for p in ETSY_PRODUCTS if p["niche"] == niche],
        "digistore": DIGISTORE_PRODUCTS.get(niche, []),
        "amazon":    AMAZON_PRODUCTS.get(niche, []),
    }
