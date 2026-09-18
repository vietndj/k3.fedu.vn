import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Hàm thay thế: Nếu href không bắt đầu bằng # và chưa có target="_blank", thì thêm vào.
def target_replacer(match):
    full_tag = match.group(0)
    href_val = match.group(1)
    
    # Bỏ qua các link mỏ neo nội bộ
    if href_val.startswith("#"):
        return full_tag
        
    # Nếu đã có target="_blank" rồi thì thôi
    if 'target="_blank"' in full_tag or "target='_blank'" in full_tag:
        return full_tag
        
    # Chèn target="_blank" vào sau chữ <a 
    # Thay <a thành <a target="_blank"
    return full_tag.replace('<a ', '<a target="_blank" ', 1)

html = re.sub(r'<a\s+[^>]*href="([^"]+)"[^>]*>', target_replacer, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
