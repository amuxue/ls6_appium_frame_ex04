from frame.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.run_steps("../page/search_page.yaml", "search")
        return True