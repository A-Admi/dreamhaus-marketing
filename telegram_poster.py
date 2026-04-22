"""
telegram_poster.py — Post to Telegram channel via Bot API
No approval needed. Works immediately.
"""
import requests, urllib.parse, time, random
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def _generate_image_url(prompt: str) -> str:
    """Generate product image via Pollinations (free)."""
    styled = (
        f"{prompt}, aesthetic digital product mockup, "
        f"clean minimal design, pastel colors, professional, no text"
    )
    encoded = urllib.parse.quote(styled)
    return (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width=1080&height=1080&nologo=true&model=flux"
    )


def send_photo(image_url: str, caption: str) -> bool:
    """Send a photo with caption to the channel."""
    if not TELEGRAM_BOT_TOKEN or "YOUR_" in TELEGRAM_BOT_TOKEN:
        print("[Telegram] No token — skipping")
        return False
    try:
        r = requests.post(
            f"{TELEGRAM_URL}/sendPhoto",
            json={
                "chat_id":    TELEGRAM_CHANNEL_ID,
                "photo":      image_url,
                "caption":    caption[:1024],
                "parse_mode": "HTML",
            },
            timeout=30,
        )
        if r.status_code == 200:
            print(f"[Telegram] ✅ Photo posted")
            return True
        print(f"[Telegram] {r.status_code}: {r.text[:200]}")
    except Exception as e:
        print(f"[Telegram] Error: {e}")
    return False


def send_message(text: str) -> bool:
    """Send a text message to channel."""
    if not TELEGRAM_BOT_TOKEN or "YOUR_" in TELEGRAM_BOT_TOKEN:
        return False
    try:
        r = requests.post(
            f"{TELEGRAM_URL}/sendMessage",
            json={
                "chat_id":    TELEGRAM_CHANNEL_ID,
                "text":       text[:4096],
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
            },
            timeout=30,
        )
        return r.status_code == 200
    except Exception as e:
        print(f"[Telegram] {e}")
        return False


def post_etsy_product(product: dict) -> bool:
    """Post an Etsy product with image and buy link."""
    keywords = " ".join([f"#{k.replace(' ', '')}" for k in product["keywords"][:5]])

    caption = (
        f"🛍️ <b>{product['title']}</b>\n\n"
        f"💰 Only <b>{product['price']}</b> — Instant Digital Download!\n\n"
        f"✅ Download instantly after purchase\n"
        f"✅ Print at home or use digitally\n"
        f"✅ Lifetime access\n\n"
        f"👉 <a href='{product['url']}'>Buy Now on Etsy</a>\n\n"
        f"{keywords}\n"
        f"#etsyshop #digitaldownload #printable #instantdownload"
    )

    image_prompt = f"{product['title']} digital download aesthetic product mockup"
    image_url    = _generate_image_url(image_prompt)

    return send_photo(image_url, caption)


def post_affiliate_product(product: dict, source: str = "digistore") -> bool:
    """Post an affiliate product recommendation."""
    caption = (
        f"💡 <b>Recommended Resource</b>\n\n"
        f"📚 <b>{product['title']}</b>\n\n"
        f"✨ {product.get('cta', 'Check this out!')}\n\n"
        f"🔗 <a href='{product['url']}'>Learn More</a>\n\n"
        f"#selfimprovement #productivity #digitaltools"
    )

    image_prompt = f"{product['title']} digital course online learning aesthetic"
    image_url    = _generate_image_url(image_prompt)

    return send_photo(image_url, caption)


def post_blog_article(article: dict, blog_url: str) -> bool:
    """Share a new blog post to the channel."""
    message = (
        f"📖 <b>New Article</b>\n\n"
        f"<b>{article['title']}</b>\n\n"
        f"{article.get('meta_description', '')}\n\n"
        f"👉 <a href='{blog_url}'>Read Full Article</a>\n\n"
        f"🛍️ <a href='https://www.etsy.com/shop/DreamHausDigital'>Shop Our Products</a>\n\n"
        f"#tips #productivity #digitaldownloads"
    )
    return send_message(message)


def run_daily_posts(niche: str, links: dict, article: dict, blog_url: str) -> dict:
    """
    Daily Telegram posting schedule:
    1. Blog article share
    2. Best Etsy product for niche
    3. Top Digistore24 affiliate product
    """
    results = {}

    # Post 1 — Blog article
    print("[Telegram] Posting blog article...")
    results["blog"] = post_blog_article(article, blog_url)
    time.sleep(5)

    # Post 2 — Etsy product
    etsy_products = links.get("etsy", [])
    if etsy_products:
        product = random.choice(etsy_products)
        print(f"[Telegram] Posting Etsy product: {product['title']}")
        results["etsy"] = post_etsy_product(product)
        time.sleep(5)

    # Post 3 — Digistore affiliate
    ds_products = links.get("digistore", [])
    if ds_products:
        ds_product = random.choice(ds_products)
        print(f"[Telegram] Posting affiliate: {ds_product['title']}")
        results["affiliate"] = post_affiliate_product(ds_product)

    return results
