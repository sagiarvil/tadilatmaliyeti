const { test, expect } = require("@playwright/test");
const path = require("path");

test.describe("2027 Tadilat Maliyeti — Gerçek Mimari Fotoğraflar & 7 Motor Testi", () => {
  const fileUrl = "file://" + path.join(process.cwd(), "hesapla.html");

  test("1. Sayfa yükleme ve başlık doğrulaması", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
    await expect(page).toHaveTitle(/2027 Ev Tadilatı Fiyat & Metraj Hesaplama Motoru/);
  });

  test("2. Adım geçişleri ve Kalite Segmenti doğrulaması", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
    
    // Adım 1 görünür
    const step1 = page.locator("#sectionStep1");
    await expect(step1).toBeVisible();

    // Adım 2 sekmesine tıkla
    await page.locator("#stepTab2").click();
    const step2 = page.locator("#sectionStep2");
    await expect(step2).toBeVisible();

    // 3 Tier fotoğrafının varlığını doğrula
    await expect(page.locator("#tierImgEco")).toHaveAttribute("src", "images/tier-eco.jpg");
    await expect(page.locator("#tierImgStd")).toHaveAttribute("src", "images/tier-std.jpg");
    await expect(page.locator("#tierImgLux")).toHaveAttribute("src", "images/tier-lux.jpg");
  });

  test("3. Gerçek Fotoğraflı Öncesi / Sonrası Mekan Değişimi", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
    await page.locator("#stepTab2").click();

    // Başlangıç Mutfak Fotoğrafları
    const afterImg = page.locator("#baAfterImg");
    const beforeImg = page.locator("#baBeforeImg");
    await expect(afterImg).toBeVisible();
    await expect(beforeImg).toBeVisible();
    await expect(afterImg).toHaveAttribute("src", "images/kitchen-after.jpg");
    await expect(beforeImg).toHaveAttribute("src", "images/kitchen-before.jpg");

    // Banyo sekmesine tıkla
    await page.locator("#baRoomBath").click();
    await expect(afterImg).toHaveAttribute("src", "images/bath-after.jpg");
    await expect(beforeImg).toHaveAttribute("src", "images/bath-before.jpg");

    // Komple Daire sekmesine tıkla
    await page.locator("#baRoomPenthouse").click();
    await expect(afterImg).toHaveAttribute("src", "images/living-after.jpg");
    await expect(beforeImg).toHaveAttribute("src", "images/living-before.jpg");
  });

  test("4. Dinamik metraj ve canlı bütçe reaksiyonu", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });

    const sqmInput = page.locator("#sqmInput");
    await sqmInput.fill("140");
    await sqmInput.dispatchEvent("input");

    const badge = page.locator("#topTotalBadge");
    const text = await badge.textContent();
    expect(text).toContain("₺");
  });
});
