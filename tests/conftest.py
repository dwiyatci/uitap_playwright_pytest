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
