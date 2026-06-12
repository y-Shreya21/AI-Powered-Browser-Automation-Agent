from browser.browser_manager import BrowserManager

browser = BrowserManager()

browser.start()

browser.goto("https://google.com")

browser.screenshot("google.png")

text = browser.extract_text()

if text:
    print(text[:500])
else:
    print("No text found")

input("Press Enter to close...")

browser.stop()