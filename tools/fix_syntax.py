import re

with open("hesapla.html", "r", encoding="utf-8") as f:
    content = f.read()

# Locate the orphaned section from window.setBaScene to origRender
target_start = content.find("window.setBaScene = function(scKey) {")
target_end = content.find("// Hook contract update into main render cycle")

if target_start != -1 and target_end != -1:
    clean_replacement = """window.setBaScene = function(scKey) {
        const sc = baPhotoScenes[scKey];
        if (!sc) return;
        const beforeImg = document.getElementById('baBeforeImg');
        const afterImg = document.getElementById('baAfterImg');
        const label = document.getElementById('baAfterLabel');
        const desc = document.getElementById('baSceneDesc');

        if (beforeImg) beforeImg.src = sc.before;
        if (afterImg) afterImg.src = sc.after;
        if (label) label.textContent = sc.label;
        if (desc) desc.textContent = sc.desc;

        ['baRoomLiving', 'baRoomBath', 'baRoomPenthouse'].forEach(id => {
          const btn = document.getElementById(id);
          if (!btn) return;
          const isTarget = (id === 'baRoomLiving' && scKey === 'kitchen') ||
                           (id === 'baRoomBath' && scKey === 'bath') ||
                           (id === 'baRoomPenthouse' && scKey === 'living');
          if (isTarget) {
            btn.className = 'ba-room-btn py-2 px-3 rounded-xl font-black bg-amber-500 text-slate-950 shadow-md transition-all flex items-center gap-1.5';
          } else {
            btn.className = 'ba-room-btn py-2 px-3 rounded-xl font-bold text-slate-400 hover:text-white hover:bg-slate-900 transition-all flex items-center gap-1.5';
          }
        });
      };

      const baRangeInput = document.getElementById('baRangeInput');
      const baBeforeClip = document.getElementById('baBeforeClip');
      const baDividerLine = document.getElementById('baDividerLine');
      const baSliderPctText = document.getElementById('baSliderPctText');

      if (baRangeInput && baBeforeClip && baDividerLine) {
        baRangeInput.addEventListener('input', e => {
          const val = parseFloat(e.target.value);
          baBeforeClip.style.clipPath = `inset(0 ${100 - val}% 0 0)`;
          baDividerLine.style.left = `${val}%`;
          if (baSliderPctText) baSliderPctText.textContent = `%${Math.round(val)} Önce / %${Math.round(100 - val)} Sonra`;
        });
      }

      // React-Bits: Spotlight Mouse Takipçisi
      document.addEventListener('mousemove', (e) => {
        document.querySelectorAll('.spotlight-card').forEach(card => {
          const rect = card.getBoundingClientRect();
          card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
          card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
        });
      });

      """
    content = content[:target_start] + clean_replacement + content[target_end:]
    print("✅ Orphaned 3D kodları temizlendi ve Before/After motoru bağlandı.")

# Also replace update3dStudio() call at end with setBaScene('kitchen')
content = content.replace("update3dStudio();", "setBaScene('kitchen');")

with open("hesapla.html", "w", encoding="utf-8") as f:
    f.write(content)

print("hesapla.html kaydedildi.")
