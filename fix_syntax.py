with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

bad = """    document.addEventListener("DOMContentLoaded", () => {
      const dropdowns_all = document.querySelectorAll(".nav-dropdown");
      dropdowns_all.forEach(dd => {
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

good = """    document.addEventListener("DOMContentLoaded", () => {
      const dropdowns_all = document.querySelectorAll(".nav-dropdown");
      dropdowns_all.forEach(dd => {
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
      });
    });"""

html = html.replace(bad, good)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
