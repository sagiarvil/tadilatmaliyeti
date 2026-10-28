const { test, expect } = require("@playwright/test");
const path = require("path");

test.describe("2027 Tadilat & Maliyet Hesaplama Motoru (Mutfak, Banyo, Komple Daire)", () => {
  const fileUrl = "file://" + path.join(process.cwd(), "hesapla.html");

  test("1. Sayfa yükleme ve başlık doğrulaması", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
    await expect(page).toHaveTitle(/2027 Tadilat & Maliyet Hesaplama Motoru/);
  });

  test("2. 3 Ana Kategori Sekmesi (Mutfak, Banyo, Komple) Geçişleri", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });

    // Başlangıçta Mutfak Paneli aktif
    const pMutfak = page.locator("#panelMutfak");
    await expect(pMutfak).toBeVisible();

    // Banyo sekmesine tıkla
    await page.locator("button[data-target='panelBanyo']").click();
    const pBanyo = page.locator("#panelBanyo");
    await expect(pBanyo).toBeVisible();
    await expect(pMutfak).toBeHidden();

    // Komple Daire sekmesine tıkla
    await page.locator("button[data-target='panelKomple']").click();
    const pKomple = page.locator("#panelKomple");
    await expect(pKomple).toBeVisible();
    await expect(pBanyo).toBeHidden();
  });

  test("3. Mutfak Stepper & Canlı Fiyat Hesaplaması", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });

    // m2 değiştir
    const mInput = page.locator("#m_alan_input");
    await mInput.fill("18");
    await mInput.dispatchEvent("input");

    // Min ve Max göstergeleri kontrol et
    const minText = await page.locator("#m_min_display").textContent();
    const maxText = await page.locator("#m_max_display").textContent();
    expect(minText).toContain("₺");
    expect(maxText).toContain("₺");

    // 2. Adıma geç
    await page.locator(".btn-next-m").first().click({ force: true });
    await expect(page.locator("#m_step_2")).toBeVisible();
  });

  test("4. Komple Daire Metraj ve Canlı Fiyat Reaksiyonu", async ({ page }) => {
    await page.goto(fileUrl, { waitUntil: "domcontentloaded" });

    // Komple paneline geç
    await page.locator("button[data-target='panelKomple']").click();

    // 140 m2 hızlı butonuna tıkla
    await page.locator("button.btn-quick-k-m2[data-val='140']").click();

    const minText = await page.locator("#k_min_display").textContent();
    const maxText = await page.locator("#k_max_display").textContent();
    expect(minText).toContain("₺");
    expect(maxText).toContain("₺");
  });
});
