import pytest
import os


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {**browser_type_launch_args, "args": ["--disable-dev-shm-usage"]}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1600,
            "height": 900,
        },
        "record_video_size": {
            "width": 1920,
            "height": 1080,
        },
    }


# ref: https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


video_counter = 0


@pytest.fixture(autouse=True)
def save_video_as(request, page):
    global video_counter

    yield

    video_opt = request.config.getoption("video")
    test_result_failed = request.node.rep_call.failed

    if video_opt == "on" or (video_opt == "retain-on-failure" and test_result_failed):
        page.context.close()

        video_counter = video_counter + 1
        custom_path = f"videos/{video_counter:02d}_{request.node.originalname}.webm"
        page.video.save_as(custom_path)
        page.video.delete()
