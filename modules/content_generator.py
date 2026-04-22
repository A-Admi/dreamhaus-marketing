"""
content_generator.py — AI content for blog articles
"""
import requests, json, re, time
from config import GROQ_API_KEY, GEMINI_API_KEY, CLAUDE_API_KEY

GROQ_URL   = "https://api.groq.com/openai/v1/chat/completions"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
CLAUDE_URL = "https://api.anthropic.com/v1/messages"
GROQ_HEADERS   = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
CLAUDE_HEADERS = {"x-api-key": CLAUDE_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"}


def _call_ai(prompt, max_tokens=2000):
    # Groq
    if GROQ_API_KEY and "YOUR_" not in GROQ_API_KEY:
        try:
            r = requests.post(GROQ_URL, headers=GROQ_HEADERS,
                json={"model": "llama-3.3-70b-versatile",
                      "messages": [{"role": "user", "content": prompt}],
                      "temperature": 0.8, "max_tokens": max_tokens}, timeout=60)
            if r.status_code == 200:
                print("[AI] ✅ Groq")
                return r.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"[AI] Groq: {e}")

    # Gemini
    if GEMINI_API_KEY and "YOUR_" not in GEMINI_API_KEY:
        try:
            r = requests.post(GEMINI_URL,
                json={"contents": [{"parts": [{"text": prompt}]}],
                      "generationConfig": {"temperature": 0.8, "maxOutputTokens": max_tokens}}, timeout=60)
            if r.status_code == 200:
                print("[AI] ✅ Gemini")
                return r.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            print(f"[AI] Gemini: {e}")

    # Claude
    if CLAUDE_API_KEY and "YOUR_" not in CLAUDE_API_KEY:
        try:
            r = requests.post(CLAUDE_URL, headers=CLAUDE_HEADERS,
                json={"model": "claude-3-5-haiku-20241022", "max_tokens": max_tokens,
                      "messages": [{"role": "user", "content": prompt}]}, timeout=60)
            if r.status_code == 200:
                print("[AI] ✅ Claude")
                return r.json()["content"][0]["text"]
        except Exception as e:
            print(f"[AI] Claude: {e}")

    return None


def _parse(raw):
    raw = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', raw)
    raw = re.sub(r'```json\s*|```\s*', '', raw).strip()
    s, e = raw.find('{'), raw.rfind('}') + 1
    if s < 0: raise ValueError("No JSON")
    result, in_str, esc = [], False, False
    for ch in raw[s:e]:
        if esc: result.append(ch); esc = False
        elif ch == '\\': result.append(ch); esc = True
        elif ch == '"': result.append(ch); in_str = not in_str
        elif in_str and ch == '\n': result.append('\\n')
        elif in_str and ch == '\r': result.append('\\r')
        else: result.append(ch)
    return json.loads(''.join(result))


def generate_seo_article(topic, niche, etsy_products, amazon_products, amazon_tag):
    etsy_str   = "\n".join([f"- [{p['title']}]({p['url']}) — {p['price']}" for p in etsy_products[:3]])
    amazon_str = "\n".join([f"- [{p['title']}]({p['url']})" for p in amazon_products[:2]])

    prompt = f"""Write a high-quality SEO blog post: "{topic}"
Niche: {niche}

Rules:
- 800-1000 words, markdown format with ## headers
- Helpful educational content
- Mention these Etsy products naturally 2-3 times:
{etsy_str}
- Mention these Amazon products naturally 1-2 times:
{amazon_str}
- End with clear CTA to shop

Return ONLY valid JSON no markdown:
{{"title":"SEO title under 60 chars","meta_description":"under 155 chars","content":"full markdown article","tags":["tag1","tag2","tag3","tag4","tag5"]}}"""

    raw = _call_ai(prompt, 3000)
    if raw:
        try: return _parse(raw)
        except: pass

    return {
        "title": topic,
        "meta_description": f"Best {niche} tools and resources",
        "content": f"# {topic}\n\nDiscover our collection of {niche} tools at [DreamHausDigital]({etsy_str})",
        "tags": [niche, "printable", "digital", "download"],
    }


def generate_pinterest_pin(product):
    prompt = f"""Create viral Pinterest pin for: {product['title']} — {product['price']}
Keywords: {', '.join(product['keywords'])}

Return ONLY valid JSON:
{{"title":"pin title under 100 chars","description":"200-300 chars with CTA","hashtags":["#tag1","#tag2","#tag3","#tag4","#tag5"]}}"""

    raw = _call_ai(prompt, 400)
    if raw:
        try: return _parse(raw)
        except: pass

    return {
        "title": f"{product['title']} — Instant Download",
        "description": f"Get {product['title']} for {product['price']}! Instant digital download.",
        "hashtags": [f"#{k.replace(' ','')}" for k in product['keywords'][:5]],
    }


def generate_reddit_post(topic, product, subreddit):
    return {
        "title": f"Sharing what helped me with {topic}",
        "body": f"Hey everyone! {topic}\n\nFound this helpful: {product['url']}",
    }
