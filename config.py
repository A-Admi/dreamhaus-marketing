# ============================================================
#  DREAMHAUS DIGITAL — Full Automation Config
#  Fill keys → add to GitHub Secrets → delete from here
# ============================================================

# ── AI APIs ──────────────────────────────────────────────
GROQ_API_KEY   = "YOUR_GROQ_API_KEY_HERE"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
CLAUDE_API_KEY = "YOUR_CLAUDE_API_KEY_HERE"

# ── Etsy Shop ─────────────────────────────────────────────
ETSY_SHOP_URL  = "https://www.etsy.com/shop/DreamHausDigital"
ETSY_SHOP_NAME = "DreamHausDigital"

# ── Amazon Associates ─────────────────────────────────────
# Your Store ID from Amazon Associates dashboard
AMAZON_TAG = "hitorica-20"

# ── Pinterest API ─────────────────────────────────────────
# Get from: https://developers.pinterest.com → My Apps → Create App
# Scopes needed: boards:read, boards:write, pins:read, pins:write
PINTEREST_ACCESS_TOKEN = "YOUR_PINTEREST_ACCESS_TOKEN_HERE"
PINTEREST_BOARD_IDS = {
    "adhd":        "YOUR_ADHD_BOARD_ID",
    "business":    "YOUR_BUSINESS_BOARD_ID",
    "health":      "YOUR_HEALTH_BOARD_ID",
    "digital_art": "YOUR_DIGITAL_ART_BOARD_ID",
}

# ── Instagram ─────────────────────────────────────────────
# Requirements: Instagram Business account linked to Facebook Page
# Get from: https://developers.facebook.com → Instagram Graph API
# Permissions: instagram_basic, instagram_content_publish
INSTAGRAM_ACCESS_TOKEN = "YOUR_INSTAGRAM_ACCESS_TOKEN_HERE"
INSTAGRAM_USER_ID      = "YOUR_INSTAGRAM_USER_ID_HERE"

# ── GitHub Pages ──────────────────────────────────────────
GITHUB_USERNAME = "A-Admi"
SITE_REPO       = "history-secrets"
SITE_URL        = "https://A-Admi.github.io/history-secrets"

# ── Your Etsy Products ────────────────────────────────────
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
        "keywords": ["cleaning business", "business forms", "printable", "small business"],
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

# ── Amazon Affiliate Products ─────────────────────────────
AMAZON_PRODUCTS = [
    {"title": "The ADHD Advantage Book",        "asin": "1583335080", "niche": "adhd"},
    {"title": "Bullet Journal Notebook",         "asin": "B07D95KXPQ", "niche": "adhd"},
    {"title": "PCOS Diet Book",                  "asin": "1628602120", "niche": "health"},
    {"title": "Self-Employed Tax Guide",         "asin": "1260462021", "niche": "business"},
    {"title": "Small Business Planner",          "asin": "B08BPLANNR", "niche": "business"},
]

# ── Content Topics Per Niche ──────────────────────────────
CONTENT_TOPICS = {
    "adhd": [
        "10 ADHD productivity hacks that actually work",
        "Why dopamine menus are changing ADHD management",
        "The ADHD tax and how to stop losing money",
        "Best budget trackers for ADHD brains in 2026",
        "How to build a morning routine with ADHD",
        "ADHD and money why budgeting feels impossible",
        "Visual planning tools for neurodivergent people",
        "ADHD friendly meal planning guide",
    ],
    "business": [
        "How to start a cleaning business with no money",
        "10 tax deductions every freelancer misses",
        "ATS resume tips that get you interviews in 2026",
        "Free business forms every cleaning company needs",
        "How to file taxes as a self-employed freelancer",
        "Starting a side hustle as a cleaning business",
        "Best tools for freelancers working from home",
    ],
    "health": [
        "PCOS symptoms nobody talks about",
        "How to track your cycle with PCOS",
        "Hormone health tools that help women with PCOS",
        "PCOS and nutrition what actually works",
        "Managing PCOS symptoms with daily tracking",
        "Best journals for women with hormonal imbalances",
    ],
    "digital_art": [
        "How to use SVG files for your small business",
        "Best free tools for editing SVG files on Cricut",
        "Drip art logos and why they are trending in 2026",
        "How to customize digital downloads for Cricut",
        "Top digital art trends for small businesses",
    ],
}

# ── Telegram ──────────────────────────────────────────────
# Bot token from @BotFather
TELEGRAM_BOT_TOKEN  = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
# Channel ID (e.g. -1003681571454 or @dreamhausdigital)
TELEGRAM_CHANNEL_ID = "-1003681571454"

# ── Digistore24 ───────────────────────────────────────────
DIGISTORE_ID = "Ahfirnet"
