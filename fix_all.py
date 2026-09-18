import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix broken links
def link_replacer(match):
    page = match.group(1)
    if "http" in page:
        return match.group(0)
    return f'href="https://fedu.vn/course/{page}"'

html = re.sub(r'href="([a-zA-Z0-9-]*\.html)"', link_replacer, html)

# Fix sticky nav overflow clipping
html = html.replace("overflow-x: auto;", "/* overflow-x: auto; removed */")
html = html.replace("overflow-y: visible !important;", "/* overflow-y: visible !important; removed */")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
