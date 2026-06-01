from browser.browser_manager import BrowserManager

browser = BrowserManager()

browser.start()

browser.goto("https://google.com")

browser.screenshot("google.png")

text = browser.extract_text()

print(text[:500])
input("Press Enter to close...")

browser.stop()