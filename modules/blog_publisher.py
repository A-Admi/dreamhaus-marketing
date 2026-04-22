"""
blog_publisher.py — Publishes SEO articles to GitHub Pages (Jekyll)
"""
import os, datetime, re


def slugify(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    return slug[:60]


def publish_article(article, niche, posts_dir="site/_posts"):
    os.makedirs(posts_dir, exist_ok=True)
    today    = datetime.date.today().isoformat()
    slug     = slugify(article["title"])
    filename = f"{today}-{slug}.md"
    filepath = os.path.join(posts_dir, filename)
    tags_str = "\n".join([f"  - {t}" for t in article.get("tags", [])])

    content = f"""---
layout: post
title: "{article['title'].replace('"', "'")}"
date: {today}
categories: [{niche}]
tags:
{tags_str}
description: "{article.get('meta_description','').replace('"',"'")}"
---

{article.get('content', '')}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[Blog] ✅ {filename}")
    return filepath


def create_jekyll_config(site_dir="site"):
    os.makedirs(site_dir, exist_ok=True)
    config = """title: "DreamHaus Digital"
description: "Premium digital downloads for ADHD, business, health and more"
url: "https://A-Admi.github.io"
baseurl: "/dreamhaus-marketing"
theme: minima
plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
"""
    with open(os.path.join(site_dir, "_config.yml"), "w") as f:
        f.write(config)
    print("[Blog] ✅ Jekyll config created")


def create_homepage(site_dir="site"):
    os.makedirs(site_dir, exist_ok=True)
    index = """---
layout: home
title: DreamHaus Digital — Premium Printables & Templates
---

## Welcome to DreamHaus Digital 🌟

Your home for **premium digital downloads** that make life easier.

### 🧠 ADHD & Neurodivergent Tools
👉 [Shop ADHD Tools](https://www.etsy.com/shop/DreamHausDigital)

### 💼 Business Templates
👉 [Shop Business Templates](https://www.etsy.com/shop/DreamHausDigital)

### 🏥 Health & Wellness
👉 [Shop Health Tools](https://www.etsy.com/shop/DreamHausDigital)

### 🎨 Digital Art & SVG
👉 [Shop Digital Art](https://www.etsy.com/shop/DreamHausDigital)
"""
    with open(os.path.join(site_dir, "index.md"), "w") as f:
        f.write(index)
    print("[Blog] ✅ Homepage created")
