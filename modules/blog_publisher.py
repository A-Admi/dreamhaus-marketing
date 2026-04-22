"""
blog_publisher.py — Publishes SEO articles as plain HTML to GitHub Pages
No Jekyll needed — works immediately.
"""
import os, datetime, re


def slugify(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    return slug[:60]


def markdown_to_html(md):
    """Simple markdown to HTML converter."""
    html = md
    # Headers
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    # Links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank">\1</a>', html)
    # Bullet points
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>\n?)+', r'<ul>\g<0></ul>', html)
    # Paragraphs
    paragraphs = html.split('\n\n')
    result = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<h') and not p.startswith('<ul'):
            p = f'<p>{p}</p>'
        result.append(p)
    return '\n'.join(result)


def create_article_html(article, niche, date_str):
    """Create a full HTML page for an article."""
    content_html = markdown_to_html(article.get('content', ''))
    tags = article.get('tags', [])
    tags_html = ' '.join([f'<span class="tag">#{t}</span>' for t in tags])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{article['title']} | DreamHaus Digital</title>
<meta name="description" content="{article.get('meta_description', '')}">
<style>
  body {{ font-family: Georgia, serif; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; line-height: 1.7; }}
  h1 {{ color: #2c3e50; border-bottom: 3px solid #e74c3c; padding-bottom: 10px; }}
  h2 {{ color: #34495e; margin-top: 30px; }}
  a {{ color: #e74c3c; }}
  .tag {{ background: #f8f9fa; padding: 4px 10px; border-radius: 20px; font-size: 13px; margin: 3px; display: inline-block; }}
  .nav {{ background: #2c3e50; padding: 15px; margin-bottom: 30px; border-radius: 8px; }}
  .nav a {{ color: white; text-decoration: none; margin-right: 20px; font-size: 14px; }}
  .shop-btn {{ background: #e74c3c; color: white; padding: 12px 25px; border-radius: 5px; text-decoration: none; display: inline-block; margin: 10px 5px; font-weight: bold; }}
  .shop-btn:hover {{ background: #c0392b; }}
  .affiliate-box {{ background: #fff3cd; border: 1px solid #ffc107; padding: 20px; border-radius: 8px; margin: 25px 0; }}
  .meta {{ color: #888; font-size: 14px; margin-bottom: 20px; }}
  footer {{ margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; text-align: center; color: #888; font-size: 13px; }}
</style>
</head>
<body>
<div class="nav">
  <a href="/dreamhaus-marketing/">🏠 Home</a>
  <a href="https://www.etsy.com/shop/DreamHausDigital" target="_blank">🛍️ Etsy Shop</a>
  <a href="https://t.me/dreamhausdigital" target="_blank">📱 Telegram</a>
</div>

<h1>{article['title']}</h1>
<div class="meta">📅 {date_str} &nbsp;|&nbsp; 🏷️ {niche.upper()}</div>

<div class="affiliate-box">
  💡 <strong>Shop Our Digital Downloads:</strong><br><br>
  <a href="https://www.etsy.com/shop/DreamHausDigital" class="shop-btn" target="_blank">🛍️ Visit Etsy Shop</a>
  <a href="https://t.me/dreamhausdigital" class="shop-btn" target="_blank">📱 Join Telegram</a>
</div>

{content_html}

<div class="affiliate-box">
  <strong>🌟 Recommended Resources:</strong><br><br>
  <a href="https://www.etsy.com/shop/DreamHausDigital" class="shop-btn" target="_blank">Get Our Printables</a>
  <a href="https://pinealguardianvip.com/ds/indexts.php#aff=Ahfirnet" class="shop-btn" target="_blank">Brain Health Supplement</a>
  <a href="https://www.advancedbionutritionals.com/DS24/Advanced-Mitochondrial/Too-Tired-To-Enjoy-It/HD.htm#aff=Ahfirnet" class="shop-btn" target="_blank">Boost Your Energy</a>
</div>

<div>{tags_html}</div>

<footer>
  <p>© 2026 DreamHaus Digital | <a href="https://www.etsy.com/shop/DreamHausDigital">Etsy Shop</a></p>
</footer>
</body>
</html>"""


def publish_article(article, niche, posts_dir="site/_posts"):
    os.makedirs(posts_dir, exist_ok=True)
    today    = datetime.date.today().isoformat()
    slug     = slugify(article["title"])
    filename = f"{today}-{slug}.html"
    filepath = os.path.join(posts_dir, filename)

    html = create_article_html(article, niche, today)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[Blog] ✅ {filename}")
    return filepath


def create_homepage(site_dir="site"):
    """Create homepage index.html — GitHub Pages serves this immediately."""
    os.makedirs(site_dir, exist_ok=True)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DreamHaus Digital — Premium Printables & Digital Downloads</title>
<meta name="description" content="Premium digital downloads for ADHD, business, health and more. Instant download on Etsy.">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: Georgia, serif; color: #333; }}
  header {{ background: #2c3e50; color: white; padding: 40px 20px; text-align: center; }}
  header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
  header p {{ font-size: 1.2em; opacity: 0.9; }}
  .hero {{ background: #e74c3c; color: white; padding: 40px 20px; text-align: center; }}
  .hero a {{ background: white; color: #e74c3c; padding: 15px 35px; border-radius: 5px; text-decoration: none; font-size: 1.2em; font-weight: bold; display: inline-block; margin: 10px; }}
  .categories {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 40px 20px; max-width: 1000px; margin: 0 auto; }}
  .card {{ background: white; border: 1px solid #ddd; border-radius: 10px; padding: 25px; width: 220px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
  .card h3 {{ margin-bottom: 10px; color: #2c3e50; }}
  .card p {{ font-size: 14px; color: #666; margin-bottom: 15px; }}
  .card a {{ background: #e74c3c; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-size: 14px; }}
  .affiliates {{ background: #f8f9fa; padding: 40px 20px; text-align: center; }}
  .affiliates h2 {{ margin-bottom: 25px; color: #2c3e50; }}
  .aff-btn {{ background: #27ae60; color: white; padding: 12px 25px; border-radius: 5px; text-decoration: none; margin: 8px; display: inline-block; font-weight: bold; }}
  footer {{ background: #2c3e50; color: white; text-align: center; padding: 20px; font-size: 14px; }}
  footer a {{ color: #e74c3c; }}
</style>
</head>
<body>

<header>
  <h1>🌟 DreamHaus Digital</h1>
  <p>Premium Digital Downloads — Instant Access</p>
</header>

<div class="hero">
  <h2>Transform Your Life With Our Digital Tools</h2>
  <p style="margin:15px 0">ADHD planners, business templates, health trackers & more</p>
  <a href="https://www.etsy.com/shop/DreamHausDigital" target="_blank">🛍️ Shop Now on Etsy</a>
  <a href="https://t.me/dreamhausdigital" target="_blank">📱 Join Our Telegram</a>
</div>

<div class="categories">
  <div class="card">
    <h3>🧠 ADHD Tools</h3>
    <p>Dopamine menus, budget trackers, wellness bundles</p>
    <a href="https://www.etsy.com/listing/4322772731" target="_blank">Shop Now</a>
  </div>
  <div class="card">
    <h3>💼 Business</h3>
    <p>Cleaning business forms, tax kits, resume templates</p>
    <a href="https://www.etsy.com/listing/4343414380" target="_blank">Shop Now</a>
  </div>
  <div class="card">
    <h3>🏥 Health</h3>
    <p>PCOS hormone kit, cycle tracker, wellness planner</p>
    <a href="https://www.etsy.com/listing/4375567104" target="_blank">Shop Now</a>
  </div>
  <div class="card">
    <h3>🎨 Digital Art</h3>
    <p>SVG logos, drip art, editable design files</p>
    <a href="https://www.etsy.com/listing/4343397375" target="_blank">Shop Now</a>
  </div>
</div>

<div class="affiliates">
  <h2>💊 Recommended Health Products</h2>
  <a class="aff-btn" href="https://pinealguardianvip.com/ds/indexts.php#aff=Ahfirnet" target="_blank">🧠 Pineal Guardian — Brain & Focus</a>
  <a class="aff-btn" href="https://www.advancedbionutritionals.com/DS24/Advanced-Mitochondrial/Too-Tired-To-Enjoy-It/HD.htm#aff=Ahfirnet" target="_blank">⚡ Advanced Mitochondrial — Beat Fatigue</a>
  <a class="aff-btn" href="https://www.advancedbionutritionals.com/DS24/Advanced-Amino/Muscle-Mass-Loss/HD.htm#aff=Ahfirnet" target="_blank">💪 Advanced Amino — Stop Muscle Loss</a>
  <a class="aff-btn" href="https://www.checkout-ds24.com/redir/577873/Ahfirnet/" target="_blank">💰 Online Business Course</a>
</div>

<footer>
  <p>© 2026 DreamHaus Digital | <a href="https://www.etsy.com/shop/DreamHausDigital">Etsy Shop</a> | <a href="https://t.me/dreamhausdigital">Telegram</a></p>
</footer>

</body>
</html>"""

    with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("[Blog] ✅ Homepage created")


def create_jekyll_config(site_dir="site"):
    """Create .nojekyll to bypass Jekyll and serve HTML directly."""
    os.makedirs(site_dir, exist_ok=True)
    with open(os.path.join(site_dir, ".nojekyll"), "w") as f:
        f.write("")
    print("[Blog] ✅ .nojekyll created")
