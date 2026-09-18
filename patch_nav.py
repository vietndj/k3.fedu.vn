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

# The new navigation HTML
new_nav = """<nav class="sticky-nav" style="display: flex; gap: 16px; align-items: center; overflow: visible;">
    <!-- ĐỊNH DẠNG -->
    <div class="nav-dropdown" id="navFormatDropdown" style="position: relative;">
      <button type="button" class="nav-dropdown-btn" aria-haspopup="true" aria-expanded="false" style="background: none; border: none; cursor: pointer; display: flex; align-items: center; gap: 4px; font-weight: 600;">
        <span>🎬 4 Định Dạng</span>
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
      <div class="nav-dropdown-menu" role="menu" style="position: absolute; top: 100%; left: 0; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px; min-width: 280px; display: none; flex-direction: column; z-index: 100; padding: 8px; border: 1px solid #eee;">
        <a href="https://fedu.vn/course/voiceover.html" class="nav-dd-item" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block;">
            <div style="font-size: 11px; opacity: 0.7; font-weight: 700; margin-bottom: 4px;">ĐỊNH DẠNG 01</div>
            <div style="font-weight: 600;">Voice-Over & Thao Tác</div>
        </a>
        <a href="https://fedu.vn/course/walkandtalk.html" class="nav-dd-item" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block;">
            <div style="font-size: 11px; opacity: 0.7; font-weight: 700; margin-bottom: 4px;">ĐỊNH DẠNG 02</div>
            <div style="font-weight: 600;">Walk & Talk</div>
        </a>
        <a href="https://fedu.vn/course/talkinghead.html" class="nav-dd-item" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block;">
            <div style="font-size: 11px; opacity: 0.7; font-weight: 700; margin-bottom: 4px;">ĐỊNH DẠNG 03</div>
            <div style="font-weight: 600;">Talking Head</div>
        </a>
        <a href="https://fedu.vn/course/storytelling.html" class="nav-dd-item" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block;">
            <div style="font-size: 11px; opacity: 0.7; font-weight: 700; margin-bottom: 4px;">ĐỊNH DẠNG 04</div>
            <div style="font-weight: 600;">Storytelling 2.5</div>
        </a>
      </div>
    </div>

    <!-- CÔNG CỤ -->
    <a href="https://fedu.vn/course/3congcu.html" style="font-weight: 600; color: #1e293b; text-decoration: none;">Công cụ</a>

    <!-- Ý TƯỞNG -->
    <div class="nav-dropdown" style="position: relative;">
      <button type="button" class="nav-dropdown-btn" aria-haspopup="true" aria-expanded="false" style="background: none; border: none; cursor: pointer; display: flex; align-items: center; gap: 4px; font-weight: 600;">
        <span>Ý tưởng</span>
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
      <div class="nav-dropdown-menu" role="menu" style="position: absolute; top: 100%; left: 0; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px; min-width: 280px; display: none; flex-direction: column; z-index: 100; padding: 8px; border: 1px solid #eee;">
        <a href="https://ytuong.fedu.vn" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block; font-weight: 500;">Kho Ý Tưởng</a>
        <a href="https://fedu.vn/k/logickenh-cac-trend-ap-dung-trong-lam-noi-dung-the-nao.html" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block; font-weight: 500;">Các trend áp dụng trong làm nội dung thế nào?</a>
      </div>
    </div>

    <!-- CASE -->
    <div class="nav-dropdown" style="position: relative;">
      <button type="button" class="nav-dropdown-btn" aria-haspopup="true" aria-expanded="false" style="background: none; border: none; cursor: pointer; display: flex; align-items: center; gap: 4px; font-weight: 600;">
        <span>Case</span>
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"></polyline></svg>
      </button>
      <div class="nav-dropdown-menu" role="menu" style="position: absolute; top: 100%; left: 0; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px; min-width: 320px; display: none; flex-direction: column; z-index: 100; padding: 8px; border: 1px solid #eee;">
        <a href="https://fedu.vn/k/logickenh-gymcoach.html" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block; font-weight: 500;">Case Study Gym Coach Bị Giới Hạn</a>
        <a href="https://fedu.vn/k/logickenh-baohiem.html" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block; font-weight: 500;">Case Study Chị Liên Bảo Hiểm</a>
        <a href="https://fedu.vn/k/logickenh-bep-duc.html" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block; font-weight: 500;">Case Study Bếp Đức</a>
        <a href="https://fedu.vn/k/logickenh-tattoo.html" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block; font-weight: 500;">Case Study Tattoo</a>
        <a href="https://fedu.vn/k/logickenh-tuanminh.html" style="padding: 12px; text-decoration: none; color: #333; border-radius: 6px; display: block; font-weight: 500;">Case Tuấn Minh</a>
      </div>
    </div>
  </nav>

  <script>
    // Xử lý sự kiện hover cho các menu dropdown mới
    document.addEventListener("DOMContentLoaded", function() {
        const dropdowns = document.querySelectorAll(".nav-dropdown");
        dropdowns.forEach(dropdown => {
            let timeout;
            dropdown.addEventListener("mouseenter", () => {
                clearTimeout(timeout);
                dropdown.querySelector(".nav-dropdown-menu").style.display = "flex";
            });
            dropdown.addEventListener("mouseleave", () => {
                timeout = setTimeout(() => {
                    dropdown.querySelector(".nav-dropdown-menu").style.display = "none";
                }, 100);
            });
        });
    });
  </script>
"""

# Tìm block <nav class="sticky-nav"> ... </nav>
nav_pattern = re.compile(r'<nav class="sticky-nav">.*?</nav>', re.DOTALL)
html = nav_pattern.sub(new_nav, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
