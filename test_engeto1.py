# Engeto - Staň se novým IT Talentem
from playwright.sync_api import Page


def test_title(page):
    # přejdi na stránku Engeto
    page.goto("https://engeto.cz/")

    # zkontroluj, že titulek obsahuje "Engeto" (bez ohledu na velikost písmen)
    assert "engeto" in page.title().lower(), f"Neočekávaný title: {page.title()}"

def test_cookies(page: Page):
    # otevři stránku Engeto
    page.goto("https://engeto.cz/")

    # klikni na tlačítko „Souhlasím jen s nezbytnými“
    button = page.locator("#cookiescript_reject")
    button.click()

    # počkej 2 sekundy, ať banner zmizí
    page.wait_for_timeout(2000)

    # zkontroluj, že banner zmizel
    banner = page.locator("#cookiescript_injected")
    assert not banner.is_visible(), "Cookie banner by měl zmizet po odmítnutí cookies"


def test_menu_kurzy_visible(page: Page):
    # otevře stránku Engeto
    page.goto("https://engeto.cz/")

    # najde tlačítko/menu odkaz "Kurzy"
    kurzy_button = page.get_by_role("link", name="Kurzy", exact=True)

    # ověří, že je tlačítko viditelné
    assert kurzy_button.is_visible(), "Tlačítko 'Kurzy' není viditelné na stránce!"

