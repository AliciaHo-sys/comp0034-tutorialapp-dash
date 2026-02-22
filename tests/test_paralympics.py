# Imports from Playwright
from playwright.sync_api import Page, expect


# The Page fixture and app_server fixture are parameters for the method
def test_page_has_body(page: Page, app_server):
    """
    GIVEN a server URL (app_server fixture yields the URL)
    WHEN the 'home' page is requested
    THEN the home page body should be displayed
    """
    # Use the page to go to the URL, in this case the app_server fixture yield the URL
    page.goto(dash_app_server)
    expect(page.locator("body")).to_be_visible()
    # For Streamlit use: expect(page.locator("body")).to_be_attached() or expect(page).to_have_title("Paralympics Dashboard") 