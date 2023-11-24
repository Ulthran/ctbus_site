from . import DEV_URL


def test_title(setup):
    for name, driver in setup.items():
        driver.get(DEV_URL)
        assert driver.title == "Charlie Bushman", f"{name} failed"


def test_title(setup):
    for name, driver in setup.items():
        driver.get(f"{DEV_URL}/certifications")
        assert driver.title == "Charlie Bushman", f"{name} failed"
