def test_dynamicid(page):
    page.goto("/dynamicid")

    page.locator("'Button with Dynamic ID'").click()


def test_classattr(page):
    page.goto("/classattr")

    page.locator(".btn-primary").click()


def test_hiddenlayers(page):
    page.goto("/hiddenlayers")

    page.set_default_timeout(5000)

    buttons_locator = page.locator("'Button'")
    # print(buttons_locator.count())
    buttons_locator.click()

    # print(buttons_locator.count())
    #     for i in range(buttons_locator.count()):
    #         locator = buttons_locator.nth(i)
    #         if locator.is_visible():
    #             print(locator.get_attribute("id"))
    #             locator.click()

    page.locator("#blueButton").click()


def test_loaddelay(page):
    page.goto("/")

    page.locator("'Load Delay'").click()
    page.locator("'Button Appearing After Delay'").click()


def test_ajax(page):
    page.goto("/ajax")

    page.locator("'Button Triggering AJAX Request'").click()
    page.locator("'Data loaded with AJAX get request.'").click()


def test_clientdelay(page):
    page.goto("/clientdelay")

    page.locator("'Button Triggering Client Side Logic'").click()
    page.locator("'Data calculated on the client side.'").click()


def test_click(page):
    page.goto("/click")

    page.locator("'Button That Ignores DOM Click Event'").click()
    page.locator("'Button That Ignores DOM Click Event'").click()


def test_testinput(page):
    page.goto("/textinput")

    page.locator("#newButtonName").fill("MyButton")
    page.locator("'Button That Should Change it's Name Based on Input Value'").click()
    assert page.locator("#updatingButton").text_content() == "MyButton"


def test_scrollbars(page):
    page.goto("/scrollbars")

    page.locator("'Hiding Button'").click()


def test_dynamictable(page):
    page.goto("/dynamictable")

    colheaders_locator = page.locator('[role="table"] [role="columnheader"]')
    target_prop_node_index = colheaders_locator.evaluate_all(
        "nodes => {"
        + "const targetPropNode = Array.from(nodes).find(node => node.textContent === 'CPU');"
        + "return [...targetPropNode.parentElement.childNodes].indexOf(targetPropNode);"
        + "}"
    )

    cells_locator = page.locator('[role="table"] [role="cell"]')
    chrome_cpu_load = cells_locator.evaluate_all(
        "(nodes, targetPropNodeIndex) => {"
        + "const targetBrowserNode = Array.from(nodes).find(node => node.textContent === 'Chrome');"
        + "return targetBrowserNode.parentElement.childNodes[targetPropNodeIndex].textContent;"
        + "}",
        target_prop_node_index,
    )

    assert chrome_cpu_load in page.locator("p.bg-warning").text_content()


def test_verifytext(page):
    page.goto("/verifytext")

    text = page.locator(".bg-primary > .badge-secondary").inner_text()
    assert text == "Welcome UserName!"


def test_progressbar(page):
    page.goto("/progressbar")

    page.locator("#startButton").click()
    page.wait_for_selector("#progressBar:has-text('75%')")
    page.locator("#stopButton").click()
    result = page.locator("#result").text_content()
    assert "Result: 0" in result


def test_visibility(page):
    page.goto("/visibility")

    buttons_locator = page.locator("button")
    page.locator("#hideButton").click()

    visibility = False
    for i in range(buttons_locator.count()):
        locator = buttons_locator.nth(i)
        text = locator.text_content()
        if (
            not (
                text == "Hide"
                or text == "Overlapped"
                or text == "Opacity 0"
                or text == "Offscreen"
            )
            and locator.is_visible()
        ):
            print(f'"{text}" Button is visible (!)')
            visibility = True
            break

    assert visibility == False


def test_sampleapp(page):
    page.goto("/sampleapp")

    page.locator('[name="UserName"]').fill("glenn")
    page.locator('[name="Password"]').fill("pwd")
    page.locator("#login").click()
    assert page.locator("#loginstatus").text_content() == "Welcome, glenn!"
    page.locator("#login").click()
    assert page.locator("#loginstatus").text_content() == "User logged out."

    page.locator('[name="UserName"]').fill("glenn")
    page.locator('[name="Password"]').fill("zsófi")
    page.locator("#login").click()
    assert page.locator("#loginstatus").text_content() == "Invalid username/password"


def test_mouseover(page):
    page.goto("/mouseover")

    page.locator("'Click me'").click()
    page.locator("'Click me'").click()
    assert int(page.locator("#clickCount").text_content()) == 2


def test_nbsp(page):
    page.goto("/nbsp")

    page.locator("'My Button'").click()
