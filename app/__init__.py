import glob
from pathlib import Path


def project_pages():
    templates_fp = Path("app/templates/projects/")
    extensions = []
    for fp_str in glob.iglob(str(templates_fp / "*.html")):
        fp = Path(fp_str.replace(str(templates_fp), ""))
        extensions.append(str(fp).replace(".html", ""))

    return extensions
