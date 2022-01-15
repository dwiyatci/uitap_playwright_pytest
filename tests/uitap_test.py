def test_dynamicid(page):
    page.goto("/dynamicid")
    page.click("text=Button with Dynamic ID")


def test_classattr(page):
    page.goto("/classattr")
    page.click(".btn-primary")


def test_hiddenlayers(page):
    page.set_default_timeout(5000)
    page.goto("/hiddenlayers")
    page.click("text='Button'")

    #     buttons_locator = page.locator("'Button'")
    #     print(buttons_locator.count())
    #     for i in range(buttons_locator.count()):
    #         locator = buttons_locator.nth(i)
    #         if locator.is_visible():
    #             print(locator.get_attribute("id"))
    #             locator.click()

    page.click("#blueButton")


def test_loaddelay(page):
    page.goto("/")
    page.click("'Load Delay'")
    page.click("'Button Appearing After Delay'")


def test_ajax(page):
    page.goto("/ajax")
    page.click("'Button Triggering AJAX Request'")
    page.click("'Data loaded with AJAX get request.'")


def test_clientdelay(page):
    page.goto("/clientdelay")
    page.click("'Button Triggering Client Side Logic'")
    page.click("'Data calculated on the client side.'")


def test_click(page):
    page.goto("/click")
    page.click("'Button That Ignores DOM Click Event'")
    page.click("'Button That Ignores DOM Click Event'")


def test_testinput(page):
    page.goto("/textinput")
    page.fill("#newButtonName", "MyButton")
    page.click("'Button That Should Change it's Name Based on Input Value'")
    assert page.text_content("#updatingButton") == "MyButton"


def test_scrollbars(page):
    page.goto("/scrollbars")
    page.click("'Hiding Button'")


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

    assert chrome_cpu_load in page.text_content("p.bg-warning")


def test_verifytext(page):
    page.goto("/verifytext")
    text = page.inner_text(".bg-primary > .badge-secondary")
    assert text == "Welcome UserName!"


def test_progressbar(page):
    page.goto("/progressbar")
    page.click("#startButton")
    page.wait_for_selector("#progressBar:has-text('75%')")
    page.click("#stopButton")
    result = page.text_content("#result")
    assert "Result: 0" in result


def test_visibility(page):
    page.goto("/visibility")
    buttons_locator = page.locator("button")
    page.click("#hideButton")

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

    page.fill('[name="UserName"]', "glenn")
    page.fill('[name="Password"]', "pwd")
    page.click("#login")
    assert page.text_content("#loginstatus") == "Welcome, glenn!"
    page.click("#login")
    assert page.text_content("#loginstatus") == "User logged out."

    page.fill('[name="UserName"]', "glenn")
    page.fill('[name="Password"]', "özge")
    page.click("#login")
    assert page.text_content("#loginstatus") == "Invalid username/password"


def test_mouseover(page):
    page.goto("/mouseover")
    page.click("'Click me'")
    page.click("'Click me'")
    assert int(page.text_content("#clickCount")) == 2


def test_nbsp(page):
    page.goto("/nbsp")
    page.click("'My Button'")
