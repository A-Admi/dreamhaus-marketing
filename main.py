"""
main.py — DreamHaus Digital Full Automation
Daily: Blog + Telegram posts with Etsy + Digistore24 + Amazon affiliate links
"""
import os, sys, time, datetime, random, subprocess
sys.path.insert(0, os.path.dirname(__file__))

from modules.content_generator import generate_seo_article, generate_pinterest_pin
from modules.telegram_poster   import run_daily_posts
from modules.blog_publisher    import publish_article, create_jekyll_config, create_homepage
from modules.topic_tracker     import get_fresh_topic
from modules.affiliate_links   import get_links_for_niche, ETSY_PRODUCTS, AMAZON_PRODUCTS
from config import AMAZON_TAG, SITE_URL, GITHUB_USERNAME, SITE_REPO

NICHES = ["adhd", "business", "health", "digital_art"]


def run_niche(niche: str):
    print(f"\n{'='*55}")
    print(f"  NICHE: {niche.upper()}")
    print(f"{'='*55}")

    links          = get_links_for_niche(niche)
    etsy_products  = links["etsy"]
    amazon_products = AMAZON_PRODUCTS.get(niche, [])

    if not etsy_products:
        print(f"[Main] No products for: {niche}")
        return

    # Fresh unique topic
    topic = get_fresh_topic(niche)
    print(f"\n📝 Topic: {topic}")

    # 1. Generate SEO blog article
    print("\n[1/3] Generating SEO article...")
    article = generate_seo_article(
        topic           = topic,
        niche           = niche,
        etsy_products   = etsy_products,
        amazon_products = amazon_products,
        amazon_tag      = AMAZON_TAG,
    )
    print(f"      ✅ {article['title']}")

    # 2. Publish to GitHub Pages
    print("\n[2/3] Publishing to blog...")
    today    = datetime.date.today().isoformat()
    slug     = article['title'].lower().replace(' ', '-')[:50]
    blog_url = f"{SITE_URL}/{niche}/{today}-{slug}"
    publish_article(article, niche)

    # 3. Post to Telegram (blog + Etsy + Digistore24)
    print("\n[3/3] Posting to Telegram channel...")
    run_daily_posts(
        niche    = niche,
        links    = links,
        article  = article,
        blog_url = blog_url,
    )

    print(f"\n✅ {niche} complete!")


def run():
    print(f"\n{'='*55}")
    print(f"  🛍️  DREAMHAUS DIGITAL AUTOMATION")
    print(f"  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*55}")

    # Setup blog on first run
    if not os.path.exists("site/_config.yml"):
        create_jekyll_config()
        create_homepage()

    # Today's niche — cycles daily
    day_num      = datetime.date.today().toordinal()
    todays_niche = NICHES[day_num % len(NICHES)]
    print(f"\n📅 Today's niche: {todays_niche}")

    run_niche(todays_niche)

    # Commit + push blog
    print("\n[Git] Publishing blog...")
    try:
        subprocess.run(["git", "config", "user.email", "bot@dreamhaus.com"], check=False)
        subprocess.run(["git", "config", "user.name",  "DreamHausBot"],      check=False)
        subprocess.run(["git", "add", "site/", "data/"],                      check=False)
        subprocess.run(["git", "commit", "-m",
                        f"Blog: {datetime.date.today()} — {todays_niche}"],   check=False)
        subprocess.run(["git", "push"],                                        check=False)
        print("[Git] ✅ Blog published")
    except Exception as e:
        print(f"[Git] {e}")

    print(f"\n{'='*55}")
    print(f"  ✅ DAILY AUTOMATION COMPLETE")
    print(f"  📱 Telegram : @dreamhausdigital")
    print(f"  🌐 Blog     : {SITE_URL}")
    print(f"  🛍️  Etsy     : https://www.etsy.com/shop/DreamHausDigital")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    run()
