import re
import os

print("Applying real architectural photos and removing vector 3D SVGs...")

with open("hesapla.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Tier Card Images to Real Photos
content = content.replace(
    'src="data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="220" viewBox="0 0 400 220"><rect width="100%" height="100%" fill="%23f1f5f9"/><rect x="20" y="20" width="160" height="120" rx="4" fill="%23cbd5e1"/><rect x="200" y="20" width="180" height="180" rx="4" fill="%23e2e8f0"/><text x="50%" y="85%" font-family="sans-serif" font-size="14" font-weight="bold" fill="%2364748b" text-anchor="middle">İSKANDİNAV PRATİK PAKET</text></svg>"',
    'src="images/tier-eco.jpg"'
)
content = content.replace(
    'src="data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="220" viewBox="0 0 400 220"><rect width="100%" height="100%" fill="%23f8fafc"/><rect x="30" y="30" width="150" height="150" rx="6" fill="%23e2e8f0"/><rect x="200" y="30" width="170" height="90" rx="4" fill="%23fed7aa"/><circle cx="285" cy="165" r="30" fill="%23fb923c"/><text x="50%" y="90%" font-family="sans-serif" font-size="14" font-weight="bold" fill="%23ea580c" text-anchor="middle">MODERN KONFOR PAKET</text></svg>"',
    'src="images/tier-std.jpg"'
)
content = content.replace(
    'src="data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="220" viewBox="0 0 400 220"><rect width="100%" height="100%" fill="%230f172a"/><rect x="30" y="30" width="160" height="160" rx="6" fill="%231e293b" stroke="%23f59e0b" stroke-width="2"/><circle cx="285" cy="80" r="40" fill="%23d97706"/><rect x="220" y="140" width="150" height="50" rx="4" fill="%23334155"/><text x="50%" y="90%" font-family="sans-serif" font-size="14" font-weight="bold" fill="%23fde68a" text-anchor="middle">A+ MİMARİ PRESTİJ</text></svg>"',
    'src="images/tier-lux.jpg"'
)
print("✅ Tier kartı görselleri gerçek mimari fotoğraflara güncellendi.")

# 2. Build the Ultra-Luxury Photographic Before/After Showcase
real_showcase_html = """
            <!-- SAĞ 50%: GERÇEK MİMARİ ÖNCESİ & SONRASI KARŞILAŞTIRMA MOTORU -->
            <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-slate-950 text-white rounded-3xl p-5 sm:p-7 border border-slate-800 shadow-2xl flex flex-col justify-between space-y-4">
              
              <!-- ÜST BAŞLIK & CANLI MEKAN SEÇİCİ SEKMELER -->
              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
                <div>
                  <span class="text-[11px] font-extrabold uppercase tracking-widest text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span> Gerçek Mimari Dönüşüm Karşılaştırması
                  </span>
                  <h3 class="text-base sm:text-lg font-black text-white mt-0.5">Mevcut Eski Yapı vs 2027 Anahtar Teslim Proje</h3>
                </div>

                <!-- 3 MEKAN SEÇİCİ SEKMELER -->
                <div class="flex items-center gap-1.5 bg-slate-950 p-1.5 rounded-2xl border border-slate-800 text-xs">
                  <button type="button" id="baRoomLiving" onclick="setBaScene('kitchen')" class="ba-room-btn py-2 px-3 rounded-xl font-black bg-amber-500 text-slate-950 shadow-md transition-all flex items-center gap-1.5">
                    <span>🍳</span>
                    <span>Mutfak</span>
                  </button>
                  <button type="button" id="baRoomBath" onclick="setBaScene('bath')" class="ba-room-btn py-2 px-3 rounded-xl font-bold text-slate-400 hover:text-white hover:bg-slate-900 transition-all flex items-center gap-1.5">
                    <span>🛁</span>
                    <span>Spa Banyo</span>
                  </button>
                  <button type="button" id="baRoomPenthouse" onclick="setBaScene('living')" class="ba-room-btn py-2 px-3 rounded-xl font-bold text-slate-400 hover:text-white hover:bg-slate-900 transition-all flex items-center gap-1.5">
                    <span>🏡</span>
                    <span>Komple Daire</span>
                  </button>
                </div>
              </div>

              <!-- FOTOĞRAFİK KARŞILAŞTIRMA TUVALİ (INTERACTIVE PHOTO SLIDER) -->
              <div class="relative w-full h-[340px] sm:h-[460px] rounded-2xl overflow-hidden select-none border-2 border-slate-800 shadow-2xl group" id="baSliderWrapper">
                
                <!-- 1. SONRASI FOTOĞRAFI (2027 ANAHTAR TESLİM DÖNÜŞÜM) -->
                <img id="baAfterImg" src="images/kitchen-after.jpg" alt="2027 Proje Dönüşümü" class="absolute inset-0 w-full h-full object-cover">
                
                <!-- SONRASI ROZETİ (SAĞ ÜST) -->
                <div class="absolute top-3.5 right-3.5 bg-emerald-600/95 backdrop-blur-md text-white text-[10px] sm:text-xs font-black uppercase tracking-wider px-3.5 py-1.5 rounded-full shadow-xl z-10 flex items-center gap-1.5 border border-emerald-400/40">
                  <span class="w-2 h-2 rounded-full bg-white"></span>
                  <span id="baAfterLabel">2027 AÇIK MUTFAK &amp; ADA DÖNÜŞÜMÜ</span>
                </div>

                <!-- 2. ÖNCESİ FOTOĞRAFI (ESKİ YAPI - MASKELİ KATMAN) -->
                <div id="baBeforeClip" class="absolute inset-0 overflow-hidden pointer-events-none transition-none" style="clip-path: inset(0 50% 0 0);">
                  <img id="baBeforeImg" src="images/kitchen-before.jpg" alt="Mevcut Eski Yapı" class="w-full h-full object-cover">
                  <!-- ÖNCESİ ROZETİ (SOL ÜST) -->
                  <div class="absolute top-3.5 left-3.5 bg-slate-950/90 backdrop-blur-md text-white text-[10px] sm:text-xs font-black uppercase tracking-wider px-3.5 py-1.5 rounded-full shadow-xl z-10 flex items-center gap-1.5 border border-red-500/50">
                    <span class="w-2 h-2 rounded-full bg-red-500"></span>
                    <span>TADİLAT ÖNCESİ (1995 ESKİ YAPI)</span>
                  </div>
                </div>

                <!-- BÖLÜCÜ ÇİZGİ VE TUTAMAK -->
                <div id="baDividerLine" class="absolute top-0 bottom-0 w-1 bg-white shadow-[0_0_16px_rgba(255,255,255,0.95)] pointer-events-none z-20 flex items-center justify-center" style="left: 50%;">
                  <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white text-slate-950 shadow-2xl flex items-center justify-center font-black text-sm border-2 border-slate-300">
                    ⇄
                  </div>
                </div>

                <!-- SÜRÜKLEME RANGE INPUT KATMANI -->
                <input id="baRangeInput" type="range" min="5" max="95" value="50" aria-label="Önce Sonra Karşılaştırıcı" class="absolute inset-0 w-full h-full opacity-0 cursor-ew-resize z-30 m-0 p-0">
              </div>

              <!-- ALT AÇIKLAMA VE YÜZDE GÖSTERGESİ -->
              <div class="flex items-center justify-between text-xs pt-2 text-slate-400 border-t border-slate-800/80">
                <span id="baSceneDesc" class="text-xs text-slate-300 max-w-sm">
                  Eski yıpranmış mutfak ve altyapıdan; akrilik ada tezgahı, ankastre ve gizli LED aydınlatmaya geçiş.
                </span>
                <span id="baSliderPctText" class="font-mono text-amber-400 font-extrabold text-xs whitespace-nowrap bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-500/20">
                  %50 Önce / %50 Sonra
                </span>
              </div>

            </div>
"""

# Replace the entire right side of Step 2 (from <!-- SAĞ 50% to end of right side container)
s2_start = content.find('<div id="sectionStep2"')
s3_start = content.find('<div id="sectionStep3"')

if s2_start != -1 and s3_start != -1:
    s2_block = content[s2_start:s3_start]
    idx_right_col = s2_block.find('<!-- SAĞ 50%')
    if idx_right_col != -1:
        # Find closing div of sectionStep2
        last_divs = s2_block.rfind('</div>\n          </div>')
        new_s2_block = s2_block[:idx_right_col] + real_showcase_html + "\n          </div>\n        </div>\n\n        "
        content = content[:s2_start] + new_s2_block + content[s3_start:]
        print("✅ Step 2 Sağ tarafı tamamen gerçek fotoğraflı öncesi/sonrası motoruna dönüştürüldü.")

# 3. Update JavaScript to drive real images
js_code = """
      // GERÇEK FOTOĞRAFLI ÖNCESİ / SONRASI MİMARİ MOTORU
      const baPhotoScenes = {
        kitchen: {
          before: 'images/kitchen-before.jpg',
          after: 'images/kitchen-after.jpg',
          label: '2027 AÇIK MUTFAK & ADA DÖNÜŞÜMÜ',
          desc: 'Eski yıpranmış mutfak ve altyapıdan; akrilik ada tezgahı, ankastre ve gizli LED aydınlatmaya geçiş.'
        },
        bath: {
          before: 'images/bath-before.jpg',
          after: 'images/bath-after.jpg',
          label: '2027 LÜKS SPA BANYO & 60x120 CALACATTA',
          desc: 'Eski sararmış fayans ve paslı tesisattan; walk-in cam duşakabin, Geberit gömme rezervuar ve LED aynaya geçiş.'
        },
        living: {
          before: 'images/living-before.jpg',
          after: 'images/living-after.jpg',
          label: '2027 MİMARİ PRESTİJ (BALIKSIRTI MEŞE & LED)',
          desc: 'Yıkım/kırım sonrası harabe yapıdan; balıksırtı meşe parke, akustik çıta duvar ve asma tavan aydınlatmalı anahtar teslim salona geçiş.'
        }
      };

      window.setBaScene = function(scKey) {
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
"""

# Replace in script
idx_old_ba = content.find("const scenes = {")
if idx_old_ba != -1:
    idx_end_ba = content.find("if (btnLiving)", idx_old_ba)
    if idx_end_ba != -1:
        # replace block
        content = content[:idx_old_ba] + js_code + "\n      " + content[idx_end_ba + 180:]
        print("✅ JavaScript Before/After motoru gerçek fotoğraflarla güncellendi.")

with open("hesapla.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Tüm işlemler başarıyla tamamlandı.")
