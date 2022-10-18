def test_mouseover(page):
    page.goto("/mouseover")

    page.get_by_text("'Click me'").click()
    page.get_by_text("'Click me'").click()
    assert int(page.locator("#clickCount").text_content()) == 3
