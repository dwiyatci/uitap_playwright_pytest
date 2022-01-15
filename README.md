# uitap_playwright_pytest

🎭🐍 Automate end-to-end tests training against [www.uitestingplayground.com](http://www.uitestingplayground.com/) using [Playwright](https://playwright.dev/) and [pytest](https://docs.pytest.org/en/6.2.x/fixture.html#what-fixtures-are), written in Python.

## 🆙 and 🏃🏻

> Playwright requires Python 3.7 or above. The browser binaries for Chromium, Firefox and WebKit work across the 3 platforms (Windows, macOS, Linux).

```shell
# Install project dependencies
make install

# Run tests
make test
```

## 🏃🏻 inside 🐳

```shell
# Build Docker image
docker build -t uitap-e2e-testing .

# Run Docker container
docker run --rm -it uitap-e2e-testing
```
