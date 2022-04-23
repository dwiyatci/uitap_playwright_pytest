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


video_counter = 0


@pytest.fixture(autouse=True)
def save_video_as(request, page):
    global video_counter

    yield

    video_counter = video_counter + 1
    custom_path = f"videos/{video_counter:02d}_{request.node.originalname}.webm"
    page.context.close()
    page.video.save_as(custom_path)
