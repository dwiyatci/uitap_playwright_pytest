def test_classattr(page):
    page.goto("/classattr")

    page.locator(".btn-primary").click()
