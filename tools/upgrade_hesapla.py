import re
import os

print("Starting hesapla.html engine integration...")

with open("hesapla.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. GSAP 3 and Designlang Tokens & Transitions-dev CSS in <head>
gsap_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>'
if "gsap.min.js" not in content:
    content = content.replace("</head>", f"  {gsap_script}\n</head>")
    print("✅ GSAP 3 script CDN eklendi.")

# Design tokens & micro-interactions style
tokens_style = """
  <!-- 7-MOTOR TASARIM & GEÇİŞ MOTORLARI (DESIGNLANG, TRANSITIONS.DEV, REACT-BITS) -->
  <style>
    :root {
      --color-primary: #d97706;
      --color-primary-hover: #b45309;
      --color-surface-dark: #090d16;
      --color-surface-card: #0f172a;
      --color-border: #1e293b;
      --font-sans: 'Plus Jakarta Sans', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }
    /* transitions.dev View Transitions Engine */
    ::view-transition-old(root),
    ::view-transition-new(root) {
      animation-duration: 0.32s;
      animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
    }
    /* React-Bits Spotlight Card Component */
    .spotlight-card {
      position: relative;
      overflow: hidden;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .spotlight-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(650px circle at var(--mouse-x, -999px) var(--mouse-y, -999px), rgba(245, 158, 11, 0.10), transparent 50%);
      pointer-events: none;
      z-index: 1;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .spotlight-card:hover::before {
      opacity: 1;
    }
    /* Taste-Skill Clean Typography & Border Normalization */
    .clean-border {
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .scene-3d-svg {
      transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
  </style>
"""

if "7-MOTOR TASARIM & GEÇİŞ MOTORLARI" not in content:
    content = content.replace("</head>", f"{tokens_style}\n</head>")
    print("✅ Design tokens ve transitions.dev stilleri eklendi.")

# 2. Check and Replace the 3D Studio container with the 3 Dedicated Scenes & Switcher
studio_replacement = """
          <!-- ======================================================= -->
          <!-- 1. BÜYÜTÜLMÜŞ SİNEMATİK 3D MİMARİ HACİM & YÜZEY STÜDYOSU -->
          <!-- ======================================================= -->
          <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-slate-950 text-white rounded-3xl p-5 sm:p-7 border border-slate-800 shadow-2xl space-y-4 spotlight-card">
            
            <!-- STÜDYO ÜST BAŞLIK & AYDINLATMA ROZETİ -->
            <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-3.5">
              <div>
                <span class="text-[11px] font-extrabold uppercase tracking-widest text-amber-400 flex items-center gap-1.5">
                  <span class="w-2 h-2 rounded-full bg-amber-400"></span> Real-Time 3D Mimari Hacim Simülatörü
                </span>
                <h3 class="text-base sm:text-lg font-black text-white mt-0.5">3D Mekan, Malzeme &amp; Aydınlatma Stüdyosu</h3>
              </div>
              <div class="flex items-center gap-2">
                <span id="lightingModeBadge" class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">
                  3000K Sıcak Gizli LED
                </span>
              </div>
            </div>

            <!-- KONUYA GÖRE DİNAMİK 3D SAHNE SEÇİCİ SEKMELER (TRANSITIONS.DEV TABS-SLIDING) -->
            <div class="grid grid-cols-3 gap-1.5 p-1.5 bg-slate-950 rounded-2xl border border-slate-800 text-xs">
              <button type="button" id="tab3dKitchen" onclick="switch3dScene('kitchen')" class="scene-tab-btn py-2.5 px-3 rounded-xl font-bold transition-all flex items-center justify-center gap-1.5 bg-amber-500 text-slate-950 font-black shadow-md">
                <span>🍳</span>
                <span class="hidden sm:inline">Mutfak Yenileme</span>
                <span class="sm:hidden">Mutfak</span>
              </button>
              <button type="button" id="tab3dBathroom" onclick="switch3dScene('bathroom')" class="scene-tab-btn py-2.5 px-3 rounded-xl font-bold transition-all flex items-center justify-center gap-1.5 text-slate-400 hover:text-white hover:bg-slate-900">
                <span>🛁</span>
                <span class="hidden sm:inline">Banyo Tadilatı</span>
                <span class="sm:hidden">Banyo</span>
              </button>
              <button type="button" id="tab3dLiving" onclick="switch3dScene('living')" class="scene-tab-btn py-2.5 px-3 rounded-xl font-bold transition-all flex items-center justify-center gap-1.5 text-slate-400 hover:text-white hover:bg-slate-900">
                <span>🏡</span>
                <span class="hidden sm:inline">Komple Ev / Salon</span>
                <span class="sm:hidden">Salon</span>
              </button>
            </div>

            <!-- 3 BOYUTLU MİMARİ TUVAL (EXPANDED VIEWPORT) -->
            <div class="relative w-full rounded-2xl overflow-hidden border-2 border-slate-800 bg-slate-950 shadow-inner group min-h-[340px] sm:min-h-[440px] flex items-center justify-center">
              
              <!-- 1. SAHNE: MUTFAK YENİLEME -->
              <svg id="svgSceneKitchen" viewBox="0 0 800 440" class="scene-3d-svg w-full h-[320px] sm:h-[440px] block">
                <defs>
                  <linearGradient id="kLedGlowCove" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.95"/>
                    <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.05"/>
                  </linearGradient>
                  <linearGradient id="kIslandTopGrad" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#ffffff"/>
                    <stop offset="100%" stop-color="#e2e8f0"/>
                  </linearGradient>
                </defs>
                <polygon id="svg3dBackWall" points="150,70 650,70 650,310 150,310" fill="#e7e2d8"/>
                <polygon id="svg3dLeftWall" points="0,0 150,70 150,310 0,440" fill="#dcd6ca"/>
                <polygon id="svg3dRightWall" points="650,70 800,0 800,440 650,310" fill="#cfc8ba"/>
                <polygon points="0,0 800,0 650,70 150,70" fill="#f8fafc"/>
                <polygon id="svg3dLedGlow" points="120,55 680,55 650,70 150,70" fill="url(#kLedGlowCove)" opacity="0.75"/>
                <polygon id="svg3dFloor" points="150,310 650,310 800,440 0,440" fill="#b88655"/>
                <g stroke="rgba(0,0,0,0.18)" stroke-width="1.2">
                  <line x1="230" y1="310" x2="110" y2="440"/>
                  <line x1="320" y1="310" x2="270" y2="440"/>
                  <line x1="400" y1="310" x2="400" y2="440"/>
                  <line x1="480" y1="310" x2="530" y2="440"/>
                  <line x1="570" y1="310" x2="690" y2="440"/>
                </g>
                <polygon id="svg3dWindow" points="25,55 125,90 125,270 25,335" fill="#bae6fd" stroke="#1e293b" stroke-width="3"/>
                <rect id="svg3dCabinetUpper" x="200" y="95" width="310" height="75" rx="3" fill="#1e293b" stroke="#0f172a" stroke-width="1.5"/>
                <line x1="303" y1="95" x2="303" y2="170" stroke="#0f172a" stroke-width="1.5"/>
                <line x1="406" y1="95" x2="406" y2="170" stroke="#0f172a" stroke-width="1.5"/>
                <rect id="svg3dBacksplash" x="200" y="170" width="310" height="45" fill="#f8fafc"/>
                <line x1="200" y1="170" x2="510" y2="170" stroke="#fde047" stroke-width="2.5" opacity="0.9"/>
                <rect id="svg3dCabinetLower" x="200" y="215" width="310" height="85" rx="3" fill="#1e293b" stroke="#0f172a" stroke-width="1.5"/>
                <line x1="303" y1="215" x2="303" y2="300" stroke="#0f172a" stroke-width="1.5"/>
                <line x1="406" y1="215" x2="406" y2="300" stroke="#0f172a" stroke-width="1.5"/>
                <polygon id="svg3dIslandBody" points="260,265 580,265 610,380 230,380" fill="#1e293b"/>
                <polygon id="svg3dIslandTop" points="250,255 590,255 615,270 225,270" fill="url(#kIslandTopGrad)" stroke="#cbd5e1" stroke-width="1.5"/>
                <polygon points="225,270 250,255 230,380 205,380" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
                <line x1="350" y1="35" x2="350" y2="140" stroke="#475569" stroke-width="2"/>
                <circle cx="350" cy="148" r="14" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
                <line x1="490" y1="35" x2="490" y2="140" stroke="#475569" stroke-width="2"/>
                <circle cx="490" cy="148" r="14" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
                <rect id="svg3dAmbientOverlay" x="0" y="0" width="800" height="440" fill="#0f172a" opacity="0.08" pointer-events="none"/>
              </svg>

              <!-- 2. SAHNE: BANYO TADİLATI (60x120 CALACATTA PORSELEN, CAM DUŞAKABİN, ASMA KLOZET, OVAL LED AYNA) -->
              <svg id="svgSceneBathroom" viewBox="0 0 800 440" class="scene-3d-svg w-full h-[320px] sm:h-[440px] hidden">
                <defs>
                  <linearGradient id="bLedGlowCove" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.9"/>
                    <stop offset="100%" stop-color="#0284c7" stop-opacity="0.05"/>
                  </linearGradient>
                  <linearGradient id="bMirrorHalo" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#fde68a" stop-opacity="0.95"/>
                    <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.3"/>
                  </linearGradient>
                  <linearGradient id="bGlassGrad" x1="0" y1="0" x2="1" y2="0">
                    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.18"/>
                    <stop offset="100%" stop-color="#0284c7" stop-opacity="0.06"/>
                  </linearGradient>
                </defs>
                <polygon id="bBackWall" points="150,70 650,70 650,310 150,310" fill="#f1f5f9"/>
                <g stroke="#cbd5e1" stroke-width="1" opacity="0.7">
                  <line x1="150" y1="150" x2="650" y2="150"/>
                  <line x1="150" y1="230" x2="650" y2="230"/>
                  <line x1="280" y1="70" x2="280" y2="310" stroke-dasharray="6 6"/>
                  <line x1="420" y1="70" x2="420" y2="310" stroke-dasharray="6 6"/>
                  <line x1="540" y1="70" x2="540" y2="310" stroke-dasharray="6 6"/>
                </g>
                <polygon id="bLeftWall" points="0,0 150,70 150,310 0,440" fill="#e2e8f0"/>
                <polygon id="bRightWall" points="650,70 800,0 800,440 650,310" fill="#cbd5e1"/>
                <polygon points="0,0 800,0 650,70 150,70" fill="#ffffff"/>
                <polygon id="bLedGlow" points="120,55 680,55 650,70 150,70" fill="url(#bLedGlowCove)" opacity="0.7"/>
                <polygon id="bFloor" points="150,310 650,310 800,440 0,440" fill="#334155"/>
                <g stroke="rgba(255,255,255,0.2)" stroke-width="1.2">
                  <line x1="230" y1="310" x2="110" y2="440"/>
                  <line x1="350" y1="310" x2="310" y2="440"/>
                  <line x1="470" y1="310" x2="510" y2="440"/>
                  <line x1="570" y1="310" x2="700" y2="440"/>
                </g>
                <!-- WALK-IN CAM DUŞAKABİN -->
                <polygon points="170,100 290,100 290,340 170,360" fill="url(#bGlassGrad)" stroke="#0f172a" stroke-width="2.5"/>
                <line x1="200" y1="85" x2="235" y2="85" stroke="#0f172a" stroke-width="3.5"/>
                <ellipse cx="235" cy="90" rx="16" ry="6" fill="#0f172a"/>
                <line x1="200" y1="85" x2="200" y2="220" stroke="#0f172a" stroke-width="3"/>
                <rect x="220" y="160" width="50" height="45" rx="2" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                <rect x="222" y="162" width="46" height="4" fill="#fde047" opacity="0.9"/>
                <!-- ASMA HİLTON BANYO DOLABI & ÇANAK LAVABO -->
                <rect id="bVanity" x="330" y="210" width="170" height="65" rx="4" fill="#1e293b" stroke="#0f172a" stroke-width="1.5"/>
                <line x1="330" y1="242" x2="500" y2="242" stroke="#0f172a" stroke-width="1.5"/>
                <rect x="326" y="204" width="178" height="8" rx="2" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
                <ellipse cx="415" cy="200" rx="34" ry="9" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
                <path d="M415,195 L415,170 Q415,160 422,160 L425,160" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
                <!-- ARKADAN AYDINLATMALI OVAL LED AYNA -->
                <ellipse cx="415" cy="135" rx="42" ry="52" fill="url(#bMirrorHalo)"/>
                <ellipse cx="415" cy="135" rx="38" ry="48" fill="#e0f2fe" stroke="#0f172a" stroke-width="2"/>
                <!-- GEBERİT ASMA KLOZET & KUMANDA PANELİ -->
                <rect x="540" y="160" width="80" height="150" rx="2" fill="#cbd5e1" opacity="0.3" stroke="#94a3b8" stroke-width="1"/>
                <rect x="565" y="180" width="30" height="18" rx="2" fill="#0f172a"/>
                <path d="M555,250 C555,275 605,275 605,250 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
                <!-- MAT SİYAH HAVLUPAN -->
                <g stroke="#0f172a" stroke-width="2.5">
                  <line x1="670" y1="110" x2="670" y2="260"/>
                  <line x1="710" y1="110" x2="710" y2="260"/>
                  <line x1="670" y1="140" x2="710" y2="140"/>
                  <line x1="670" y1="180" x2="710" y2="180"/>
                  <line x1="670" y1="220" x2="710" y2="220"/>
                </g>
                <rect id="bAmbient" x="0" y="0" width="800" height="440" fill="#0f172a" opacity="0.05" pointer-events="none"/>
              </svg>

              <!-- 3. SAHNE: KOMPLE EV / SALON (BALIKSIRTI MEŞE PARKE, AHŞAP ÇITA AKUSTİK PANEL, OLED TV KONSOLU, AVİZE) -->
              <svg id="svgSceneLiving" viewBox="0 0 800 440" class="scene-3d-svg w-full h-[320px] sm:h-[440px] hidden">
                <defs>
                  <linearGradient id="lLedGlowCove" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.95"/>
                    <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.05"/>
                  </linearGradient>
                  <linearGradient id="lChandelierGlow" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#fde68a"/>
                    <stop offset="100%" stop-color="#f59e0b"/>
                  </linearGradient>
                  <linearGradient id="lSofaGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#475569"/>
                    <stop offset="100%" stop-color="#334155"/>
                  </linearGradient>
                </defs>
                <polygon id="lBackWall" points="150,70 650,70 650,310 150,310" fill="#e7e2d8"/>
                <!-- AKUSTİK AHŞAP ÇITA DUVAR PANELİ -->
                <g id="lSlatWall" stroke="#854d0e" stroke-width="2.5" opacity="0.85">
                  <line x1="430" y1="70" x2="430" y2="250"/>
                  <line x1="446" y1="70" x2="446" y2="250"/>
                  <line x1="462" y1="70" x2="462" y2="250"/>
                  <line x1="478" y1="70" x2="478" y2="250"/>
                  <line x1="494" y1="70" x2="494" y2="250"/>
                  <line x1="510" y1="70" x2="510" y2="250"/>
                  <line x1="526" y1="70" x2="526" y2="250"/>
                  <line x1="542" y1="70" x2="542" y2="250"/>
                  <line x1="558" y1="70" x2="558" y2="250"/>
                  <line x1="574" y1="70" x2="574" y2="250"/>
                  <line x1="590" y1="70" x2="590" y2="250"/>
                  <line x1="606" y1="70" x2="606" y2="250"/>
                  <line x1="622" y1="70" x2="622" y2="250"/>
                </g>
                <polygon id="lLeftWall" points="0,0 150,70 150,310 0,440" fill="#dcd6ca"/>
                <polygon points="20,40 135,90 135,290 20,380" fill="#38bdf8" opacity="0.25" stroke="#0f172a" stroke-width="2"/>
                <polygon id="lRightWall" points="650,70 800,0 800,440 650,310" fill="#cfc8ba"/>
                <polygon points="0,0 800,0 650,70 150,70" fill="#f8fafc"/>
                <polygon id="lLedGlow" points="120,55 680,55 650,70 150,70" fill="url(#lLedGlowCove)" opacity="0.8"/>
                <!-- BALIKSIRTI MEŞE PARKE -->
                <polygon id="lFloor" points="150,310 650,310 800,440 0,440" fill="#b88655"/>
                <g stroke="rgba(0,0,0,0.16)" stroke-width="1.2">
                  <line x1="230" y1="310" x2="110" y2="440"/>
                  <line x1="320" y1="310" x2="260" y2="440"/>
                  <line x1="410" y1="310" x2="410" y2="440"/>
                  <line x1="500" y1="310" x2="560" y2="440"/>
                  <line x1="590" y1="310" x2="710" y2="440"/>
                  <line x1="180" y1="340" x2="250" y2="370"/>
                  <line x1="280" y1="340" x2="350" y2="370"/>
                  <line x1="380" y1="340" x2="450" y2="370"/>
                  <line x1="480" y1="340" x2="550" y2="370"/>
                </g>
                <!-- ASMA TV & MEDYA KONSOLU -->
                <rect x="440" y="100" width="170" height="95" rx="2" fill="#020617" stroke="#334155" stroke-width="1.5"/>
                <polygon id="lConsole" points="420,210 630,210 645,245 405,245" fill="#1e293b" stroke="#0f172a" stroke-width="1.5"/>
                <rect x="405" y="245" width="240" height="30" rx="2" fill="#0f172a"/>
                <!-- MODERN KÖŞE SOFA / KANEPE -->
                <polygon points="170,260 380,260 410,360 140,360" fill="url(#lSofaGrad)" stroke="#1e293b" stroke-width="1.5"/>
                <rect x="175" y="230" width="95" height="32" rx="6" fill="#64748b" stroke="#334155" stroke-width="1"/>
                <rect x="275" y="230" width="95" height="32" rx="6" fill="#64748b" stroke="#334155" stroke-width="1"/>
                <ellipse cx="360" cy="365" rx="35" ry="16" fill="#1e293b" stroke="#d97706" stroke-width="1.5"/>
                <ellipse cx="415" cy="380" rx="28" ry="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
                <!-- TASARIM HALKA AVİZE -->
                <line x1="380" y1="20" x2="380" y2="90" stroke="#475569" stroke-width="1.5"/>
                <ellipse cx="380" cy="95" rx="55" ry="16" fill="none" stroke="url(#lChandelierGlow)" stroke-width="3"/>
                <rect id="lAmbient" x="0" y="0" width="800" height="440" fill="#0f172a" opacity="0.08" pointer-events="none"/>
              </svg>

              <!-- ALT BİLGİ ROZETİ -->
              <div class="absolute bottom-3 left-3 bg-slate-900/90 backdrop-blur-md px-3.5 py-1.5 rounded-xl border border-slate-700/80 text-[11px] text-slate-300 flex items-center gap-2 z-10 shadow-lg">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span>Seçilen mekana göre GSAP 60fps mimari geçiş ve anlık malzeme önizlemesi.</span>
              </div>
            </div>

            <!-- CANLI MALZEME VE YÜZEY SEÇİCİ DOCK -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs pt-1">
              <div class="bg-slate-950/80 p-3 rounded-xl border border-slate-800">
                <label for="simWallSelect" class="text-[10px] text-slate-400 font-extrabold uppercase tracking-wider block mb-1.5">1. Duvar / Seramik Tonu</label>
                <select id="simWallSelect" class="w-full px-3 py-2 rounded-lg bg-slate-900 border border-slate-700 text-white font-bold text-xs focus:ring-2 focus:ring-amber-500 outline-none">
                  <option value="sand">Jotun Space (Kum Beji)</option>
                  <option value="white">Calacatta Mermer Beyazı</option>
                  <option value="sage">Adaçayı Yeşili (Pale Green)</option>
                  <option value="anthracite">Modern Antrasit &amp; Gri</option>
                </select>
              </div>

              <div class="bg-slate-950/80 p-3 rounded-xl border border-slate-800">
                <label for="simFloorSelect" class="text-[10px] text-slate-400 font-extrabold uppercase tracking-wider block mb-1.5">2. Zemin / Parke &amp; Mermer</label>
                <select id="simFloorSelect" class="w-full px-3 py-2 rounded-lg bg-slate-900 border border-slate-700 text-white font-bold text-xs focus:ring-2 focus:ring-amber-500 outline-none">
                  <option value="oak">Balıksırtı Doğal Meşe</option>
                  <option value="marble">Calacatta Porselen Zemin</option>
                  <option value="nordic">İskandinav Açık Kayın</option>
                  <option value="walnut">Koyu Amerikan Ceviz</option>
                </select>
              </div>

              <div class="bg-slate-950/80 p-3 rounded-xl border border-slate-800">
                <label for="simCabinetSelect" class="text-[10px] text-slate-400 font-extrabold uppercase tracking-wider block mb-1.5">3. Dolap / Lake &amp; Panel</label>
                <select id="simCabinetSelect" class="w-full px-3 py-2 rounded-lg bg-slate-900 border border-slate-700 text-white font-bold text-xs focus:ring-2 focus:ring-amber-500 outline-none">
                  <option value="anthracite">Mat Antrasit Lake</option>
                  <option value="cashmere">Kaşmir &amp; Kum Beji</option>
                  <option value="walnut">Doğal Ceviz &amp; Siyah</option>
                  <option value="emerald">Zümrüt Yeşil &amp; Altın</option>
                </select>
              </div>

              <div class="bg-slate-950/80 p-3 rounded-xl border border-slate-800">
                <label for="simLightSelect" class="text-[10px] text-slate-400 font-extrabold uppercase tracking-wider block mb-1.5">4. Aydınlatma Atmosferi</label>
                <select id="simLightSelect" class="w-full px-3 py-2 rounded-lg bg-slate-900 border border-slate-700 text-white font-bold text-xs focus:ring-2 focus:ring-amber-500 outline-none">
                  <option value="warm">3000K Sıcak Gizli LED</option>
                  <option value="daylight">6500K Doğal Gün Işığı</option>
                  <option value="cinema">Gece Lounge &amp; Sinema</option>
                </select>
              </div>
            </div>

          </div>
"""

# Replace between the old studio section
old_studio_pattern = re.compile(r'<!-- SAĞ 50%: CANLI 3D MİMARİ HACİM & YÜZEY SİMÜLATÖRÜ -->[\s\S]*?<!-- CANLI MALZEME VE YÜZEY SEÇİCİ \(HORIZONTAL DOCK\) -->[\s\S]*?</div>\s*</div>\s*</div>', re.MULTILINE)

match = old_studio_pattern.search(content)
if match:
    content = content[:match.start()] + "<!-- SAĞ 50%: CANLI 3D MİMARİ HACİM & YÜZEY SİMÜLATÖRÜ -->\n" + studio_replacement + "\n</div>" + content[match.end():]
    print("✅ 3D Mimari Stüdyo 3 dinamik sahne ve geçiş dock'u ile değiştirildi.")
else:
    # Try finding by sectionStep2
    print("⚠️ regex eşleşmedi, doğrudan svg arayarak değiştirilecek.")
    idx_svg = content.find('<svg id="room3dSvg"')
    if idx_svg != -1:
        start_idx = content.rfind('<div class="bg-gradient-to-br from-slate-900', 0, idx_svg)
        end_idx = content.find('<!-- 2. İNTERAKTİF ÖNCESİ / SONRASI SLIDER', idx_svg)
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + studio_replacement + "\n\n            " + content[end_idx:]
            print("✅ 3D Stüdyo bloğu cerrahi olarak başarıyla yenilendi.")

# 3. Update JavaScript logic with GSAP 3 transitions and React-Bits mouse tracking
js_enhancements = """
    // ============================================================
    // 7-MOTOR ETKİLEŞİM & GSAP 3 GEÇİŞ KODLARI
    // ============================================================
    let current3dScene = 'kitchen';

    window.switch3dScene = function(scene) {
      if (current3dScene === scene) return;
      const scenes = { kitchen: 'svgSceneKitchen', bathroom: 'svgSceneBathroom', living: 'svgSceneLiving' };
      const currentEl = document.getElementById(scenes[current3dScene]);
      const targetEl = document.getElementById(scenes[scene]);

      // Sekme Butonlarının Durumu
      const tabs = { kitchen: 'tab3dKitchen', bathroom: 'tab3dBathroom', living: 'tab3dLiving' };
      Object.entries(tabs).forEach(([k, id]) => {
        const btn = document.getElementById(id);
        if (btn) {
          if (k === scene) {
            btn.className = 'scene-tab-btn py-2.5 px-3 rounded-xl font-bold transition-all flex items-center justify-center gap-1.5 bg-amber-500 text-slate-950 font-black shadow-md';
          } else {
            btn.className = 'scene-tab-btn py-2.5 px-3 rounded-xl font-bold transition-all flex items-center justify-center gap-1.5 text-slate-400 hover:text-white hover:bg-slate-900';
          }
        }
      });

      // GSAP 3 60fps Sinematik Geçiş Zaman Çizelgesi
      if (typeof gsap !== 'undefined' && currentEl && targetEl) {
        gsap.timeline()
          .to(currentEl, {
            opacity: 0,
            scale: 0.97,
            duration: 0.22,
            ease: 'power2.in',
            onComplete: () => {
              currentEl.classList.add('hidden');
              targetEl.classList.remove('hidden');
              current3dScene = scene;
              gsap.fromTo(targetEl, 
                { opacity: 0, scale: 1.02 }, 
                { opacity: 1, scale: 1, duration: 0.35, ease: 'power2.out' }
              );
              update3dStudio();
            }
          });
      } else if (currentEl && targetEl) {
        currentEl.classList.add('hidden');
        targetEl.classList.remove('hidden');
        current3dScene = scene;
        update3dStudio();
      }
    };

    // React-Bits: Spotlight Mouse Takipçisi
    document.addEventListener('mousemove', (e) => {
      document.querySelectorAll('.spotlight-card').forEach(card => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
      });
    });

    // 3D Stüdyo Renk ve Işık Güncellemesi (Tüm 3 Sahne İçin)
    function update3dStudio() {
      const wall = document.getElementById('simWallSelect')?.value || 'sand';
      const floor = document.getElementById('simFloorSelect')?.value || 'oak';
      const cab = document.getElementById('simCabinetSelect')?.value || 'anthracite';
      const light = document.getElementById('simLightSelect')?.value || 'warm';

      const wallPalettes = {
        sand: ['#e7e2d8', '#dcd6ca', '#cfc8ba'],
        white: ['#f8fafc', '#f1f5f9', '#e2e8f0'],
        sage: ['#d6e0d6', '#c5d3c5', '#b4c5b4'],
        anthracite: ['#94a3b8', '#64748b', '#475569']
      };
      const floorPalettes = {
        oak: '#b88655',
        marble: '#e2e8f0',
        nordic: '#dcc3a1',
        walnut: '#5c3a21'
      };
      const cabPalettes = {
        anthracite: ['#334155', '#1e293b'],
        cashmere: ['#d6cfc2', '#bfb6a6'],
        walnut: ['#6b4423', '#27272a'],
        emerald: ['#064e3b', '#022c22']
      };

      const wp = wallPalettes[wall] || wallPalettes.sand;
      const fp = floorPalettes[floor] || '#b88655';
      const cp = cabPalettes[cab] || cabPalettes.anthracite;

      // GSAP ile Renkleri Pürüzsüz Değiştirme
      if (typeof gsap !== 'undefined') {
        // Mutfak Sahnesi
        const kw1 = document.getElementById('svg3dBackWall');
        if (kw1) gsap.to(kw1, { fill: wp[0], duration: 0.3 });
        const kfl = document.getElementById('svg3dFloor');
        if (kfl) gsap.to(kfl, { fill: fp, duration: 0.3 });
        const kcab = document.getElementById('svg3dCabinetUpper');
        if (kcab) gsap.to(kcab, { fill: cp[0], duration: 0.3 });
        const kis = document.getElementById('svg3dIslandBody');
        if (kis) gsap.to(kis, { fill: cp[1], duration: 0.3 });

        // Banyo Sahnesi
        const bw = document.getElementById('bBackWall');
        if (bw) gsap.to(bw, { fill: wp[1], duration: 0.3 });
        const bfl = document.getElementById('bFloor');
        if (bfl) gsap.to(bfl, { fill: fp === '#e2e8f0' ? '#ffffff' : (fp === '#5c3a21' ? '#1e293b' : '#334155'), duration: 0.3 });
        const bvan = document.getElementById('bVanity');
        if (bvan) gsap.to(bvan, { fill: cp[1], duration: 0.3 });

        // Salon Sahnesi
        const lw = document.getElementById('lBackWall');
        if (lw) gsap.to(lw, { fill: wp[0], duration: 0.3 });
        const lfl = document.getElementById('lFloor');
        if (lfl) gsap.to(lfl, { fill: fp, duration: 0.3 });
        const lcon = document.getElementById('lConsole');
        if (lcon) gsap.to(lcon, { fill: cp[1], duration: 0.3 });
      }

      // Aydınlatma Modu
      const badge = document.getElementById('lightingModeBadge');
      const ledGlows = [document.getElementById('svg3dLedGlow'), document.getElementById('bLedGlow'), document.getElementById('lLedGlow')];
      const ambients = [document.getElementById('svg3dAmbientOverlay'), document.getElementById('bAmbient'), document.getElementById('lAmbient')];

      let glowOp = 0.70;
      let glowFill = '#fbbf24';
      let ambOp = 0.08;
      let badgeText = '3000K Sıcak Gizli LED';

      if (light === 'daylight') {
        glowOp = 0.20;
        glowFill = '#38bdf8';
        ambOp = 0.00;
        badgeText = '6500K Doğal Gün Işığı';
      } else if (light === 'cinema') {
        glowOp = 0.90;
        glowFill = '#38bdf8';
        ambOp = 0.38;
        badgeText = 'Gece Lounge & Sinema';
      }

      if (badge) badge.textContent = badgeText;
      ledGlows.forEach(el => {
        if (el) {
          el.setAttribute('opacity', glowOp);
          el.setAttribute('fill', glowFill);
        }
      });
      ambients.forEach(el => {
        if (el) el.setAttribute('opacity', ambOp);
      });
    }
"""

# Replace old update3dStudio
if "function update3dStudio()" in content:
    idx_old_func = content.find("function update3dStudio()")
    idx_end_func = content.find("['simWallSelect', 'simFloorSelect'", idx_old_func)
    if idx_old_func != -1 and idx_end_func != -1:
        content = content[:idx_old_func] + js_enhancements + "\n\n      " + content[idx_end_func:]
        print("✅ update3dStudio fonksiyonu GSAP 3 ve çoklu sahne desteğiyle güncellendi.")

with open("hesapla.html", "w", encoding="utf-8") as f:
    f.write(content)

print("hesapla.html başarıyla güncellendi.")
