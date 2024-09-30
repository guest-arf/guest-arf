from playwright.sync_api import sync_playwright

 

def run(playwright):

    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://sigmathird.my.canva.site/sigmathird")

    print(page.title())  # Print the title of the page

    browser.close()

 

with sync_playwright() as playwright:

    run(playwright)