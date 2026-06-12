# browser/service.py

from browser.browser_manager import BrowserManager

class BrowserService:

    def visit(self, url):

        browser = BrowserManager()

        browser.start()

        browser.goto(url)

        browser.screenshot()

        browser.stop()

        return {
            "success": True
        }