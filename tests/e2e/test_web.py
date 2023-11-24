import pytest
from . import DEV_URL


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get(DEV_URL)
        assert self.driver.title == "Charlie Bushman"

    def test_title_blog(self):
        self.driver.get(f"{DEV_URL}/certifications")
        print(self.driver.title)
