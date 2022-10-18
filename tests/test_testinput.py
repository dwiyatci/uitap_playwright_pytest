def test_testinput(page):
    page.goto("/textinput")

    page.locator("#newButtonName").fill("MyButton")
    page.locator("'Button That Should Change it's Name Based on Input Value'").click()
    assert page.locator("#updatingButton").text_content() == "xMyButton"
