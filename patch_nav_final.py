import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix assets and links
html = html.replace('href="./', 'href="https://fedu.vn/course/')
html = html.replace('src="./', 'src="https://fedu.vn/course/')
html = html.replace("url('./", "url('https://fedu.vn/course/")
html = html.replace("url('assets/", "url('https://fedu.vn/course/assets/")
html = html.replace('src="assets/', 'src="https://fedu.vn/course/assets/')
html = html.replace('href="assets/', 'href="https://fedu.vn/course/assets/')

new_nav = """<nav class="sticky-nav">
    <!-- 4 ĐỊNH DẠNG -->
    <div class="nav-dropdown" id="navFormatDropdown">
      <button type="button" class="nav-dropdown-btn" aria-haspopup="true" aria-expanded="false">
        <span>🎬 4 Định Dạng</span>
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
      <div class="nav-dropdown-menu" role="menu">
      <div class="nav-dd-card">
        <a href="https://fedu.vn/course/voiceover.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__tag">ĐỊNH DẠNG 01</span>
            <span class="nav-dd-item__name">Voice-Over & Thao Tác</span>
          </div>
        </a>
        <a href="https://fedu.vn/course/walkandtalk.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__tag">ĐỊNH DẠNG 02</span>
            <span class="nav-dd-item__name">Walk & Talk</span>
          </div>
        </a>
        <a href="https://fedu.vn/course/talkinghead.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__tag">ĐỊNH DẠNG 03</span>
            <span class="nav-dd-item__name">Talking Head</span>
          </div>
        </a>
        <a href="https://fedu.vn/course/storytelling.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__tag">ĐỊNH DẠNG 04</span>
            <span class="nav-dd-item__name">Storytelling 2.5</span>
          </div>
        </a>
      </div>
      </div>
    </div>

    <!-- CÔNG CỤ -->
    <a href="https://fedu.vn/course/3congcu.html" class="nav-dropdown-btn" style="text-decoration: none; padding: 4px 10px;">
      <span>🛠 Công cụ</span>
    </a>

    <!-- Ý TƯỞNG -->
    <div class="nav-dropdown" id="navIdeaDropdown">
      <button type="button" class="nav-dropdown-btn" aria-haspopup="true" aria-expanded="false">
        <span>💡 Ý tưởng</span>
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
      <div class="nav-dropdown-menu" role="menu">
      <div class="nav-dd-card">
        <a href="https://ytuong.fedu.vn" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__name">Kho Ý Tưởng</span>
          </div>
        </a>
        <a href="https://fedu.vn/k/logickenh-cac-trend-ap-dung-trong-lam-noi-dung-the-nao.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__name">Các trend áp dụng trong làm nội dung</span>
          </div>
        </a>
      </div>
      </div>
    </div>

    <!-- CASE -->
    <div class="nav-dropdown" id="navCaseDropdown">
      <button type="button" class="nav-dropdown-btn" aria-haspopup="true" aria-expanded="false">
        <span>📚 Case</span>
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
      <div class="nav-dropdown-menu" role="menu">
      <div class="nav-dd-card">
        <a href="https://fedu.vn/k/logickenh-gymcoach.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__name">Case Study: Dịch Vụ Gym Coach Bị Giới Hạn</span>
          </div>
        </a>
        <a href="https://fedu.vn/k/logickenh-baohiem.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__name">Case Study Chị Liên: Bảo Hiểm</span>
          </div>
        </a>
        <a href="https://fedu.vn/k/logickenh-bep-duc.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__name">Case Study Bếp Đức: Lê Quỳnh Anh</span>
          </div>
        </a>
        <a href="https://fedu.vn/k/logickenh-tattoo.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__name">Case Study Tattoo: Đào Trung Nghĩa</span>
          </div>
        </a>
        <a href="https://fedu.vn/k/logickenh-tuanminh.html" class="nav-dd-item">
          <div class="nav-dd-item__info">
            <span class="nav-dd-item__name">Case Tuấn Minh: Bán Đồng Hồ, Bếp Nem...</span>
          </div>
        </a>
      </div>
      </div>
    </div>
  </nav>
"""

# Tìm block <nav class="sticky-nav"> ... </nav>
nav_pattern = re.compile(r'<nav class="sticky-nav">.*?</nav>', re.DOTALL)
html = nav_pattern.sub(new_nav, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
