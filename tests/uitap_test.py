from playwright.sync_api import expect
import re


def test_dynamicid(page):
    page.goto("/dynamicid")

    page.get_by_role("button", name="Button with Dynamic ID").click()


def test_classattr(page):
    page.goto("/classattr")

    page.locator(".btn-primary").click()


def test_hiddenlayers(page):
    page.goto("/hiddenlayers")

    green_button = page.locator("#greenButton")
    blue_button = page.locator("#blueButton")

    green_button.click()
    blue_button.click()

    expect(green_button).not_to_be_focused()
    expect(blue_button).to_be_focused()


def test_loaddelay(page):
    page.goto("/")

    page.get_by_role("link", name="Load Delay").click()
    page.get_by_role("button", name="Button Appearing After Delay").click()


def test_ajax(page):
    page.goto("/ajax")

    page.get_by_role("button", name="Button Triggering AJAX Request").click()

    label_text = page.get_by_text("Data loaded with AJAX get request.")
    label_text.click()
    expect(label_text).to_be_visible()


def test_clientdelay(page):
    page.goto("/clientdelay")

    page.get_by_role("button", name="Button Triggering Client Side Logic").click()

    label_text = page.get_by_text("Data calculated on the client side.")
    label_text.focus()
    expect(label_text).to_be_visible()


def test_click(page):
    page.goto("/click")

    button = page.get_by_role("button", name="Button That Ignores DOM Click Event")
    button.click()
    button.click()
    expect(button).to_be_focused()


def test_testinput(page):
    page.goto("/textinput")

    page.get_by_role("textbox").fill("MyButton")

    page.get_by_role(
        "button", name="Button That Should Change it's Name Based on Input Value"
    ).click()
    expect(page.get_by_role("button")).to_have_text("MyButton")


def test_scrollbars(page):
    page.goto("/scrollbars")

    button = page.get_by_role("button", name="Hiding Button")
    button.scroll_into_view_if_needed()
    button.click()
    expect(button).to_be_focused()


def test_dynamictable(page):
    page.goto("/dynamictable")

    table = page.get_by_role("table").filter(has_text="Task Manager")

    chrome_row = table.get_by_role("row").filter(has_text="Chrome")

    column_headers = table.get_by_role("columnheader")
    cpu_col_idx = 0
    for idx, column_header in enumerate(column_headers.all()):
        if column_header.text_content() == "CPU":
            break
        cpu_col_idx += 1

    chrome_cpu_cell = chrome_row.get_by_role("cell").nth(cpu_col_idx)

    yellow_label = page.locator(".bg-warning")
    expect(yellow_label).to_have_text(f"Chrome CPU: {chrome_cpu_cell.text_content()}")


def test_verifytext(page):
    page.goto("/verifytext")

    expect(page.locator(".bg-primary").get_by_text("Welcome UserName!")).to_be_visible()


def test_progressbar(page):
    page.goto("/progressbar")

    page.get_by_role("button", name="Start").click()
    #     page.wait_for_selector('#progressBar:has-text("75%")')
    #     page.locator('#progressBar:has-text("75%")').wait_for()
    #     page.get_by_role("progressbar").filter(has_text="75%").wait_for()
    progressbar_selector = "#progressBar"
    page.wait_for_function(
        "selector => document.querySelector(selector).textContent === '75%'",
        arg=progressbar_selector,
    )
    page.get_by_role("button", name="Stop").click()

    expect(page.locator("#result")).to_contain_text(re.compile(r"Result: \d{1}"))


def test_visibility(page):
    page.goto("/visibility")

    hide_button = page.get_by_role("button", name="Hide")
    removed_button = page.get_by_role("button", name="Removed")
    zero_width_button = page.get_by_role("button", name="Zero Width")
    overlapped_button = page.get_by_role("button", name="Overlapped")
    opacity_0_button = page.get_by_role("button", name="Opacity 0")
    visibility_hidden_button = page.get_by_role("button", name="Visibility Hidden")
    display_none_button = page.get_by_role("button", name="Display None")
    offscreen_button = page.get_by_role("button", name="Offscreen")

    hide_button.click()

    expect(hide_button).to_be_visible()
    expect(removed_button).not_to_be_visible()
    expect(zero_width_button).not_to_be_visible()
    expect(overlapped_button).to_be_visible()
    expect(opacity_0_button).to_be_visible()
    expect(visibility_hidden_button).not_to_be_visible()
    expect(display_none_button).not_to_be_visible()
    expect(offscreen_button).to_be_visible()


def test_sampleapp(page):
    page.goto("/sampleapp")

    username_input = page.get_by_placeholder("User Name")
    password_input = page.get_by_placeholder("********")
    login_button = page.get_by_role("button", name="Log In")

    username_input.fill("glenn")
    password_input.fill("pwd")
    login_button.click()

    login_status = page.locator("#loginstatus")
    expect(login_status).to_have_text("Welcome, glenn!")
    logout_button = page.get_by_role("button", name="Log Out")
    logout_button.click()
    expect(login_status).to_have_text("User logged out.")

    username_input.fill("glenn")
    password_input.fill("ania")
    login_button.click()
    expect(login_status).to_have_text("Invalid username/password")


def test_mouseover(page):
    page.goto("/mouseover")

    page.pause()
    click_link = page.get_by_text("Click me")
    click_link.click()
    click_link.click()

    expect(page.locator("#clickCount")).to_have_text("2")


def test_nbsp(page):
    page.goto("/nbsp")

    button = page.get_by_role("button", name="My Button")
    button.click()
    expect(button).to_be_focused()


def test_overlapped(page):
    page.goto("/overlapped")

    name_input = page.get_by_placeholder("Name")
    subject_input = page.get_by_placeholder("Subject")

    subject_input.scroll_into_view_if_needed()
    name_input.fill("glenn")
    expect(name_input).to_have_value("glenn")


def test_shadowdom(page):
    page.goto("/shadowdom")

    page.locator("#buttonGenerate").click()
    page.locator("#buttonCopy").click()

    guid_regex = re.compile(
        r"^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$"
    )

    expect(page.locator("#editField")).to_have_value(guid_regex)
