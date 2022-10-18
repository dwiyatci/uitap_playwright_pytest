def test_verifytext(page):
    page.goto("/verifytext")

    text = page.locator(".bg-primary > .badge-secondary").inner_text()
    assert text == "xWelcome UserName!"
