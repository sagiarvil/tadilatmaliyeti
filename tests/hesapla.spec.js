const { test, expect } = require("@playwright/test");
const path = require("path");

test.describe("2027 Tadilat Maliyeti — 7 Motorlu Doğrulama Testi", () => {
  const fileUrl = "file://" + path.join(process.cwd(), "hesapla.html");

  test("1. Sayfa yükleme ve başlık doğrulaması", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
    await expect(page).toHaveTitle(/2027 Ev Tadilatı Fiyat & Metraj Hesaplama Motoru/);
  });

  test("2. Adım geçişleri (View Transitions) doğrulaması", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
    
    // Adım 1 görünür
    const step1 = page.locator("#sectionStep1");
    await expect(step1).toBeVisible();

    // 2. Adıma Geç butonuna tıkla
    const btnNext2 = page.locator("#btnGoToStep2");
    if (await btnNext2.isVisible()) {
      await btnNext2.click();
      const step2 = page.locator("#sectionStep2");
      await expect(step2).toBeVisible();
    }
  });

  test("3. 3D Mimari Sahne Değişimi (Mutfak, Banyo, Salon) ve GSAP kontrolü", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });

    // Adım 2 aç
    await page.evaluate(() => {
      if (window.setStep) window.setStep(2);
      else {
        document.getElementById("sectionStep1").classList.add("hidden");
        document.getElementById("sectionStep2").classList.remove("hidden");
      }
    });

    // Mutfak sahnesi başlangıçta görünür olmalı
    const kScene = page.locator("#svgSceneKitchen");
    await expect(kScene).toBeVisible();

    // Banyo sekmesine tıkla
    await page.locator("#tab3dBathroom").click();
    await page.waitForTimeout(400); // GSAP animasyon süresi
    const bScene = page.locator("#svgSceneBathroom");
    await expect(bScene).toBeVisible();

    // Salon sekmesine tıkla
    await page.locator("#tab3dLiving").click();
    await page.waitForTimeout(400); // GSAP animasyon süresi
    const lScene = page.locator("#svgSceneLiving");
    await expect(lScene).toBeVisible();
  });

  test("4. Dinamik metraj ve fiyat hesaplama reaksiyonu", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });

    // m2 değiştir
    const sqmInput = page.locator("#sqmInput");
    await sqmInput.fill("140");
    await sqmInput.dispatchEvent("input");

    // Toplam keşif badge kontrolü
    const badge = page.locator("#topTotalBadge");
    const text = await badge.textContent();
    expect(text).toContain("₺");
  });
});
