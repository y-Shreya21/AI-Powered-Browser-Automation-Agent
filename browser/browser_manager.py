# browser/browser_manager.py

from playwright.sync_api import sync_playwright


class BrowserManager:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

    # Task 2
    def goto(self, url: str):
        if self.page:
            self.page.goto(url)
        else:
            raise Exception("Browser not started")

    # Task 3
    def click(self, selector: str):
        if self.page:
            self.page.click(selector)
        else:
            raise Exception("Browser not started")

    # Task 4
    def type(self, selector: str, text: str):
        if self.page:
            self.page.fill(selector, text)
        else:
            raise Exception("Browser not started")

    # Task 5
    def screenshot(self, filename="page.png"):
        if self.page:
            self.page.screenshot(path=filename)
        else:
            raise Exception("Browser not started")

    # Task 6
    def extract_text(self):
        if self.page:
            return self.page.text_content("body")
        else:
            raise Exception("Browser not started")

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        if self.playwright:
            self.playwright.stop()