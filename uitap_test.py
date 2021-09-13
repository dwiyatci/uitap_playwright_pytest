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

    #     locator = page.locator("'Button'")
    #     print(locator.count())
    #     for handle in locator.element_handles():
    #         if handle.is_visible():
    #             print(handle.get_attribute("id"))
    #             handle.click()

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
    header_handles = page.query_selector_all('[role="table"] [role="columnheader"]')

    target_header_handle = next(
        (x for x in header_handles if x.evaluate("node => node.textContent") == "CPU"),
        None,
    )
    target_index = target_header_handle.evaluate(
        "node => [...node.parentElement.childNodes].indexOf(node)"
    )

    cell_handles = page.query_selector_all('[role="table"] [role="cell"]')
    chrome_cpu_load = None

    for handle in cell_handles:
        if handle.evaluate("node => node.textContent") == "Chrome":
            chrome_cpu_load = handle.evaluate(
                f"node => node.parentElement.childNodes[{target_index}].textContent"
            )
            break

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
    locator = page.locator("button")
    page.click("#hideButton")

    visibility = False
    for handle in locator.element_handles():
        text = handle.text_content()
        if (
            not (
                text == "Hide"
                or text == "Overlapped"
                or text == "Opacity 0"
                or text == "Offscreen"
            )
            and handle.is_visible()
        ):
            print(handle.text_content())
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
