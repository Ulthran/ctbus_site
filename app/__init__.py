import glob
import random
from pathlib import Path
from typing import List


def project_pages() -> List:
    templates_fp = Path("app/templates/projects/")
    extensions = []
    for fp_str in glob.iglob(str(templates_fp / "*.html")):
        fp = Path(fp_str.replace(str(templates_fp), ""))
        extensions.append(str(fp).replace(".html", ""))

    return extensions


def random_third_attribute() -> str:
    attrs = [
        "Plant Dad",
        "Evil Twin",
        "Always Learning",
        "Rock Collector",
        "Piano Man",
        "Crocs Wearer",
        "And a Third Thing",
        "Trapped in a Docker Container",
        "Finding New Music",
        "XKCD Quoter",
        "Definitely Human",
    ]
    return random.choice(attrs)
