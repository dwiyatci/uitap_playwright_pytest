# uitap_playwright_pytest

🎭🐍 Automate end-to-end tests training against [www.uitestingplayground.com](http://www.uitestingplayground.com/) using [Playwright](https://playwright.dev/) and [pytest](https://docs.pytest.org/en/latest/explanation/fixtures.html), written in Python.

https://user-images.githubusercontent.com/4405796/164913144-bfbc8f54-4bac-4e61-af09-d1c8ac860304.mov

## 🆙 and 🏃🏻

### Prerequisites

- Python 3.7+, preferably installed via [pyenv](https://github.com/pyenv/pyenv).
- pip 21.3+ (usually bundled with Python, when outdated, run: `pip install --upgrade pip`).
- Python essentials (https://docs.python.org/3/tutorial/).

> Playwright requires Python 3.7 or above. The browser binaries for Chromium, Firefox and WebKit work across the 3 platforms (Windows, macOS, Linux).

### Installation and usage

```shell
# Install project dependencies
make install

# Run tests
make test

# Run tests in parallel fashion (⚠️ EXPERIMENTAL!)
make test_parallel
```

## 🏃🏻 inside 🐳

```shell
# Build Docker image
docker build -t uitap-e2e-testing .

# Run Docker container
docker run --rm -it uitap-e2e-testing
```

## Configuration

### Environment Variables

#### `PYTEST_ADDOPTS`

Please see various supported Playwright's [CLI arguments](https://playwright.dev/python/docs/test-runners#cli-arguments) that can be set in this [`PYTEST_ADDOPTS` envvar](https://docs.pytest.org/en/latest/example/simple.html?highlight=addopts).

## Project layout consideration

The heck the project is structured that way and why all those artifacts, you ask? Long story short, the rationale is a curation product after reading various sources. So be my guests:

- https://docs.python-guide.org/writing/structure/
- https://realpython.com/python-application-layouts/
- https://snarky.ca/clarifying-pep-518/
- https://docs.pytest.org/en/latest/explanation/anatomy.html#test-anatomy
- https://docs.pytest.org/en/latest/explanation/fixtures.html
- https://docs.pytest.org/en/latest/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files
- https://docs.pytest.org/en/latest/explanation/goodpractices.html#good-integration-practices

## Formatting

I'm a hardcore fan of having our code uniformly formatted, and I believe [Black](https://github.com/psf/black) has been the de-facto formatter in the Python ecosystem. So I use just that and please do so in the IDE of your choice (ideally, it should be integrated somehow with the IDE, e.g. `.py` file being formatted "On save").

Additionally, having your code formatted automatically means the formatter's parser will help to catch syntax errors earlier for you, even before the code get interpreted/compiled. 🪤
