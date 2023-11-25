import glob
from pathlib import Path

DEV_URL = "https://cjg5wanye9.execute-api.us-east-1.amazonaws.com/dev/"


def pages():
    templates_fp = Path("app/templates/")
    extensions = []
    for fp_str in glob.iglob(str(templates_fp / "**/*.html"), recursive=True):
        fp = Path(fp_str.replace(str(templates_fp), ""))
        if fp.stem == "base":
            continue
        elif fp.stem == "index":
            extensions.append("")
        else:
            extensions.append(str(fp).replace(".html", ""))

    return extensions
