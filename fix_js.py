import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the broken JS for mobile dropdown
bad_js = """    document.addEventListener("DOMContentLoaded", () => {
      const dd = document.querySelector(".nav-dropdown");
      if (!dd) return;
      const btn = dd.querySelector(".nav-dropdown-btn");
      if (btn) {
        btn.addEventListener("click", (e) => {
          e.preventDefault();
          e.stopPropagation();
          dd.classList.toggle("is-open");
          const expanded = dd.classList.contains("is-open");
          btn.setAttribute("aria-expanded", expanded);
        });
      }
      document.addEventListener("click", (e) => {
        if (!dd.contains(e.target)) {
          dd.classList.remove("is-open");
          if (btn) btn.setAttribute("aria-expanded", "false");
        }
      });
    });"""

good_js = """    document.addEventListener("DOMContentLoaded", () => {
      const dropdowns = document.querySelectorAll(".nav-dropdown");
      dropdowns.forEach(dd => {
        const btn = dd.querySelector(".nav-dropdown-btn");
        if (btn) {
          btn.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            // Đóng các menu khác
            dropdowns.forEach(other => {
               if (other !== dd) {
                 other.classList.remove("is-open");
                 const otherBtn = other.querySelector(".nav-dropdown-btn");
                 if(otherBtn) otherBtn.setAttribute("aria-expanded", "false");
               }
            });
            dd.classList.toggle("is-open");
            btn.setAttribute("aria-expanded", dd.classList.contains("is-open"));
          });
        }
      });
      document.addEventListener("click", (e) => {
        dropdowns.forEach(dd => {
          if (!dd.contains(e.target)) {
            dd.classList.remove("is-open");
            const btn = dd.querySelector(".nav-dropdown-btn");
            if (btn) btn.setAttribute("aria-expanded", "false");
          }
        });
      });
    });"""

html = html.replace(bad_js, good_js)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
