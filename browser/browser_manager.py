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
        self.page.goto(url)

    # Task 3
    def click(self, selector: str):
        self.page.click(selector)

    # Task 4
    def type(self, selector: str, text: str):
        self.page.fill(selector, text)

    # Task 5
    def screenshot(self, filename="page.png"):
        self.page.screenshot(path=filename)

    # Task 6
    def extract_text(self):
        return self.page.text_content("body")

    def stop(self):
        self.browser.close()
        self.playwright.stop()
    def goto(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def click(self, selector: str):
        self.page.click(selector).click()

    def type(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    