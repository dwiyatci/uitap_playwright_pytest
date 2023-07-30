import pytest
import os
from typing import Dict
from pytest import StashKey, CollectReport


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


# ref: https://docs.pytest.org/en/7.4.x/example/simple.html#making-test-result-information-available-in-fixtures
phase_report_key = StashKey[Dict[str, CollectReport]]()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep


def pytest_collection_modifyitems(session, config, items):
    for i, item in enumerate(items):
        setattr(item, "number", i + 1)


@pytest.fixture(autouse=True)
def save_video_as(request, page):
    yield

    video_opt = request.config.getoption("video")

    # request.node is an "item" because we use the default
    # "function" scope
    item = request.node
    report = item.stash[phase_report_key]
    test_result_failed = ("call" in report) and report["call"].failed

    if video_opt == "on" or (video_opt == "retain-on-failure" and test_result_failed):
        page.context.close()

        custom_path = f"videos/{item.number:02d}_{item.originalname}.webm"
        page.video.save_as(custom_path)
        page.video.delete()
