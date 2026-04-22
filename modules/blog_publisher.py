"""
blog_publisher.py — Professional landing page + blog articles
Modern design, mobile-first, high-converting layout.
"""
import os, datetime, re


def slugify(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    return slug[:60]


def markdown_to_html(md):
    html = md
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank">\1</a>', html)
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    paragraphs = html.split('\n\n')
    result = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<h') and not p.startswith('<li') and not p.startswith('<ul'):
            p = f'<p>{p}</p>'
        result.append(p)
    return '\n'.join(result)


CSS = """
:root {
  --primary: #6C63FF;
  --secondary: #FF6584;
  --dark: #1a1a2e;
  --card-bg: #ffffff;
  --text: #333;
  --light: #f8f8ff;
  --accent: #43e97b;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; color: var(--text); background: #f4f4f8; }

/* NAV */
nav {
  background: var(--dark);
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 20px rgba(0,0,0,0.3);
}
.logo { color: white; font-size: 1.4em; font-weight: 700; text-decoration: none; }
.logo span { color: var(--primary); }
.nav-links a {
  color: #ccc;
  text-decoration: none;
  margin-left: 20px;
  font-size: 14px;
  transition: color 0.2s;
}
.nav-links a:hover { color: white; }

/* HERO */
.hero {
  background: linear-gradient(135deg, var(--dark) 0%, #16213e 50%, #0f3460 100%);
  color: white;
  text-align: center;
  padding: 80px 20px 100px;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(ellipse at center, rgba(108,99,255,0.15) 0%, transparent 60%);
}
.hero h1 {
  font-size: clamp(2em, 5vw, 3.5em);
  margin-bottom: 20px;
  position: relative;
  line-height: 1.2;
}
.hero h1 span { color: var(--primary); }
.hero p { font-size: 1.2em; opacity: 0.85; max-width: 600px; margin: 0 auto 35px; position: relative; }
.btn-group { display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; position: relative; }
.btn-primary {
  background: var(--primary);
  color: white;
  padding: 15px 35px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 700;
  font-size: 1em;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px rgba(108,99,255,0.4);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 25px rgba(108,99,255,0.5); }
.btn-secondary {
  background: transparent;
  color: white;
  padding: 15px 35px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 700;
  border: 2px solid rgba(255,255,255,0.4);
  transition: all 0.2s;
}
.btn-secondary:hover { background: rgba(255,255,255,0.1); border-color: white; }

/* STATS */
.stats {
  background: var(--primary);
  padding: 25px;
  display: flex;
  justify-content: center;
  gap: 50px;
  flex-wrap: wrap;
}
.stat { text-align: center; color: white; }
.stat-num { font-size: 2em; font-weight: 900; }
.stat-label { font-size: 13px; opacity: 0.85; }

/* PRODUCTS SECTION */
.section { padding: 60px 20px; max-width: 1100px; margin: 0 auto; }
.section-title { text-align: center; font-size: 2em; color: var(--dark); margin-bottom: 10px; }
.section-sub { text-align: center; color: #666; margin-bottom: 40px; font-size: 1.05em; }

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 25px;
}
.product-card {
  background: white;
  border-radius: 16px;
  padding: 30px 25px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
  border: 1px solid #eee;
}
.product-card:hover { transform: translateY(-5px); box-shadow: 0 8px 30px rgba(0,0,0,0.12); }
.product-icon { font-size: 2.5em; margin-bottom: 15px; }
.product-card h3 { color: var(--dark); margin-bottom: 10px; font-size: 1.05em; }
.product-card p { color: #666; font-size: 14px; margin-bottom: 15px; line-height: 1.5; }
.price { font-size: 1.4em; font-weight: 900; color: var(--primary); margin-bottom: 15px; }
.btn-card {
  background: var(--primary);
  color: white;
  padding: 10px 25px;
  border-radius: 50px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  display: inline-block;
  transition: background 0.2s;
}
.btn-card:hover { background: #5a52e0; }

/* AFFILIATE SECTION */
.affiliate-section {
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  padding: 60px 20px;
  color: white;
  text-align: center;
}
.affiliate-section h2 { font-size: 2em; margin-bottom: 10px; }
.affiliate-section p { opacity: 0.8; margin-bottom: 35px; }
.aff-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  max-width: 1000px;
  margin: 0 auto;
}
.aff-card {
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 16px;
  padding: 25px 20px;
  transition: background 0.2s;
}
.aff-card:hover { background: rgba(255,255,255,0.12); }
.aff-card .icon { font-size: 2em; margin-bottom: 12px; }
.aff-card h4 { color: white; margin-bottom: 8px; font-size: 1em; }
.aff-card p { font-size: 13px; opacity: 0.7; margin-bottom: 15px; }
.btn-aff {
  background: var(--accent);
  color: var(--dark);
  padding: 10px 22px;
  border-radius: 50px;
  text-decoration: none;
  font-size: 13px;
  font-weight: 700;
  display: inline-block;
}

/* BLOG SECTION */
.blog-section { padding: 60px 20px; background: var(--light); }
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
  max-width: 1100px;
  margin: 0 auto;
}
.blog-card {
  background: white;
  border-radius: 16px;
  padding: 25px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.07);
  transition: transform 0.2s;
}
.blog-card:hover { transform: translateY(-3px); }
.blog-tag { background: var(--primary); color: white; font-size: 11px; padding: 3px 12px; border-radius: 50px; display: inline-block; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px; }
.blog-card h3 { color: var(--dark); font-size: 1.05em; margin-bottom: 10px; }
.blog-card p { color: #666; font-size: 14px; line-height: 1.6; }

/* CTA BANNER */
.cta-banner {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  padding: 60px 20px;
  text-align: center;
  color: white;
}
.cta-banner h2 { font-size: 2.2em; margin-bottom: 15px; }
.cta-banner p { font-size: 1.1em; opacity: 0.9; margin-bottom: 30px; }

/* FOOTER */
footer {
  background: var(--dark);
  color: #aaa;
  text-align: center;
  padding: 30px 20px;
  font-size: 14px;
}
footer a { color: var(--primary); text-decoration: none; }

/* ARTICLE PAGE */
.article-container { max-width: 780px; margin: 40px auto; padding: 0 20px; }
.article-header { margin-bottom: 30px; }
.article-header h1 { font-size: 2em; color: var(--dark); line-height: 1.3; margin-bottom: 10px; }
.article-meta { color: #888; font-size: 14px; margin-bottom: 20px; }
.article-body { background: white; padding: 40px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); line-height: 1.8; }
.article-body h2 { color: var(--dark); margin: 30px 0 15px; }
.article-body p { margin-bottom: 16px; }
.article-body a { color: var(--primary); }
.article-body ul { padding-left: 25px; margin-bottom: 16px; }
.article-body li { margin-bottom: 8px; }
.promo-box { background: linear-gradient(135deg, #667eea22, #764ba222); border: 2px solid var(--primary); border-radius: 16px; padding: 25px; margin: 30px 0; text-align: center; }
.promo-box h3 { color: var(--dark); margin-bottom: 15px; }

@media (max-width: 600px) {
  .stats { gap: 25px; }
  nav { flex-direction: column; gap: 10px; }
  .article-body { padding: 25px; }
}
"""


def create_homepage(site_dir="site"):
    os.makedirs(site_dir, exist_ok=True)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DreamHaus Digital — Premium Printables & Digital Downloads</title>
<meta name="description" content="Premium digital downloads for ADHD, business, health and creative entrepreneurs. Instant download on Etsy.">
<style>{CSS}</style>
</head>
<body>

<nav>
  <a href="/dreamhaus-marketing/" class="logo">Dream<span>Haus</span> Digital</a>
  <div class="nav-links">
    <a href="https://www.etsy.com/shop/DreamHausDigital" target="_blank">🛍️ Shop</a>
    <a href="https://t.me/dreamhausdigital" target="_blank">📱 Telegram</a>
  </div>
</nav>

<div class="hero">
  <h1>Premium Digital Downloads<br><span>That Actually Work</span></h1>
  <p>Beautifully designed templates, planners & tools. Instant download. Use today.</p>
  <div class="btn-group">
    <a href="https://www.etsy.com/shop/DreamHausDigital" class="btn-primary" target="_blank">🛍️ Shop on Etsy</a>
    <a href="https://t.me/dreamhausdigital" class="btn-secondary" target="_blank">📱 Join Telegram</a>
  </div>
</div>

<div class="stats">
  <div class="stat"><div class="stat-num">21+</div><div class="stat-label">Happy Customers</div></div>
  <div class="stat"><div class="stat-num">8</div><div class="stat-label">Digital Products</div></div>
  <div class="stat"><div class="stat-num">5⭐</div><div class="stat-label">Average Rating</div></div>
  <div class="stat"><div class="stat-num">100%</div><div class="stat-label">Instant Download</div></div>
</div>

<div class="section">
  <h2 class="section-title">Our Digital Downloads</h2>
  <p class="section-sub">Everything you need — beautifully designed, instantly downloadable</p>
  <div class="products-grid">

    <div class="product-card">
      <div class="product-icon">🧠</div>
      <h3>ADHD Dopamine Menu Template</h3>
      <p>Visual productivity tool designed specifically for ADHD brains</p>
      <div class="price">$3.24</div>
      <a href="https://www.etsy.com/listing/4322772731" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

    <div class="product-card">
      <div class="product-icon">💰</div>
      <h3>ADHD Budget Tracker</h3>
      <p>Visual money planner built for neurodivergent financial management</p>
      <div class="price">$12.99</div>
      <a href="https://www.etsy.com/listing/4322774440" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

    <div class="product-card">
      <div class="product-icon">✨</div>
      <h3>Neurodivergent Wellness Bundle</h3>
      <p>Complete ADHD dopamine menu + budget tracker bundle</p>
      <div class="price">$8.99</div>
      <a href="https://www.etsy.com/listing/4341458916" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

    <div class="product-card">
      <div class="product-icon">🌸</div>
      <h3>PCOS Hormone Health Kit</h3>
      <p>Complete symptom, cycle, nutrition & movement tracker</p>
      <div class="price">$9.99</div>
      <a href="https://www.etsy.com/listing/4375567104" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

    <div class="product-card">
      <div class="product-icon">🧹</div>
      <h3>Cleaning Business Starter Pack</h3>
      <p>10 print-ready professional business forms</p>
      <div class="price">$10.99</div>
      <a href="https://www.etsy.com/listing/4343414380" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

    <div class="product-card">
      <div class="product-icon">📊</div>
      <h3>Freelancer Tax Prep Kit</h3>
      <p>23 deductions checklist + quarterly expense tracker</p>
      <div class="price">$9.69</div>
      <a href="https://www.etsy.com/listing/4344064784" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

    <div class="product-card">
      <div class="product-icon">📄</div>
      <h3>Modern ATS Resume Template</h3>
      <p>Beat applicant tracking systems, editable Word & Google Docs</p>
      <div class="price">$6.99</div>
      <a href="https://www.etsy.com/listing/4343163615" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

    <div class="product-card">
      <div class="product-icon">🎨</div>
      <h3>Melting Headphones Logo SVG</h3>
      <p>Editable drip art PNG & SVG for your creative projects</p>
      <div class="price">$1.72</div>
      <a href="https://www.etsy.com/listing/4343397375" class="btn-card" target="_blank">Get Instant Access</a>
    </div>

  </div>
</div>

<div class="affiliate-section">
  <h2>💊 Recommended Health & Business Resources</h2>
  <p>Handpicked products we genuinely recommend</p>
  <div class="aff-grid">

    <div class="aff-card">
      <div class="icon">🧠</div>
      <h4>Pineal Guardian</h4>
      <p>Natural formula for brain health, focus and deep sleep</p>
      <a href="https://pinealguardianvip.com/ds/indexts.php#aff=Ahfirnet" class="btn-aff" target="_blank">Learn More</a>
    </div>

    <div class="aff-card">
      <div class="icon">⚡</div>
      <h4>Advanced Mitochondrial</h4>
      <p>Beat fatigue and restore your natural energy levels</p>
      <a href="https://www.advancedbionutritionals.com/DS24/Advanced-Mitochondrial/Too-Tired-To-Enjoy-It/HD.htm#aff=Ahfirnet" class="btn-aff" target="_blank">Learn More</a>
    </div>

    <div class="aff-card">
      <div class="icon">💪</div>
      <h4>Advanced Amino</h4>
      <p>Stop muscle loss and stay strong at any age</p>
      <a href="https://www.advancedbionutritionals.com/DS24/Advanced-Amino/Muscle-Mass-Loss/HD.htm#aff=Ahfirnet" class="btn-aff" target="_blank">Learn More</a>
    </div>

    <div class="aff-card">
      <div class="icon">💼</div>
      <h4>Online Business Course</h4>
      <p>Build a profitable online business from scratch</p>
      <a href="https://www.checkout-ds24.com/redir/577873/Ahfirnet/" class="btn-aff" target="_blank">Learn More</a>
    </div>

  </div>
</div>

<div class="cta-banner">
  <h2>Ready to Transform Your Life?</h2>
  <p>Join hundreds of customers who use our digital tools every day</p>
  <div class="btn-group">
    <a href="https://www.etsy.com/shop/DreamHausDigital" class="btn-primary" target="_blank">🛍️ Shop All Products</a>
    <a href="https://t.me/dreamhausdigital" class="btn-secondary" target="_blank">📱 Get Daily Tips</a>
  </div>
</div>

<footer>
  <p>© 2026 DreamHaus Digital &nbsp;|&nbsp; <a href="https://www.etsy.com/shop/DreamHausDigital">Etsy Shop</a> &nbsp;|&nbsp; <a href="https://t.me/dreamhausdigital">Telegram</a></p>
</footer>

</body>
</html>"""

    with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # .nojekyll bypasses Jekyll processing
    with open(os.path.join(site_dir, ".nojekyll"), "w") as f:
        f.write("")

    print("[Blog] ✅ Professional homepage created")


def create_jekyll_config(site_dir="site"):
    create_homepage(site_dir)


def publish_article(article, niche, posts_dir="site/_posts"):
    os.makedirs(posts_dir, exist_ok=True)
    today    = datetime.date.today().isoformat()
    slug     = slugify(article["title"])
    filename = f"{today}-{slug}.html"
    filepath = os.path.join(posts_dir, filename)
    content_html = markdown_to_html(article.get('content', ''))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{article['title']} | DreamHaus Digital</title>
<meta name="description" content="{article.get('meta_description', '')}">
<style>{CSS}</style>
</head>
<body>
<nav>
  <a href="/dreamhaus-marketing/" class="logo">Dream<span>Haus</span> Digital</a>
  <div class="nav-links">
    <a href="https://www.etsy.com/shop/DreamHausDigital" target="_blank">🛍️ Shop</a>
    <a href="https://t.me/dreamhausdigital" target="_blank">📱 Telegram</a>
  </div>
</nav>

<div class="article-container">
  <div class="article-header">
    <span class="blog-tag">{niche}</span>
    <h1>{article['title']}</h1>
    <div class="article-meta">📅 {today} &nbsp;|&nbsp; DreamHaus Digital</div>
  </div>

  <div class="promo-box">
    <h3>🛍️ Shop Our Digital Downloads</h3>
    <div class="btn-group" style="justify-content:center;margin-top:15px">
      <a href="https://www.etsy.com/shop/DreamHausDigital" class="btn-primary" target="_blank">Visit Etsy Shop</a>
      <a href="https://t.me/dreamhausdigital" class="btn-secondary" style="color:#333;border-color:#ccc" target="_blank">Join Telegram</a>
    </div>
  </div>

  <div class="article-body">
    {content_html}
  </div>

  <div class="promo-box" style="margin-top:30px">
    <h3>💊 Recommended Resources</h3>
    <div class="btn-group" style="justify-content:center;margin-top:15px;flex-wrap:wrap">
      <a href="https://pinealguardianvip.com/ds/indexts.php#aff=Ahfirnet" class="btn-primary" target="_blank">🧠 Pineal Guardian</a>
      <a href="https://www.advancedbionutritionals.com/DS24/Advanced-Mitochondrial/Too-Tired-To-Enjoy-It/HD.htm#aff=Ahfirnet" class="btn-primary" target="_blank">⚡ Beat Fatigue</a>
    </div>
  </div>
</div>

<footer>
  <p>© 2026 DreamHaus Digital &nbsp;|&nbsp; <a href="https://www.etsy.com/shop/DreamHausDigital">Etsy Shop</a></p>
</footer>
</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[Blog] ✅ {filename}")
    return filepath
