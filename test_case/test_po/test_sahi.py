from time import sleep

from page.page_sahi import PageSahi


class TestSahi:
    def test_sahi1(self, driver1):
        page = PageSahi(driver1)
        page.get_url('http://sahitest.com/demo/dragDropMooTools.htm')
        page.drag_and_drop(page.start, page.end)
        sleep(3)

    def test_sahi2(self, driver1):
        page = PageSahi(driver1)
        page.get_url('https://sahitest.com/demo/selectTest.htm')
        page.select_by_index(page.select,2)
        sleep(3)

    def test_sahi3(self, driver1):
        page = PageSahi(driver1)
        page.get_url('https://sahitest.com/demo/selectTest.htm')
        page.select_by_value(page.select, "48")
        sleep(3)

    def test_sahi4(self, driver1):
        page = PageSahi(driver1)
        page.get_url('https://sahitest.com/demo/selectTest.htm')
        page.select_by_visible_text(page.select, "Home Phone")
        sleep(3)