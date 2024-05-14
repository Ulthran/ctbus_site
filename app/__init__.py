import glob
import random
from pathlib import Path


PCMP_REPOS = [
    "sunbeam-labs/sunbeam",
    "sunbeam-labs/sbx_assembly",
    "sunbeam-labs/sbx_coassembly",
    "sunbeam-labs/sbx_kraken",
    "sunbeam-labs/sbx_mapping",
    "sunbeam-labs/sbx_demic",
    "sunbeam-labs/sbx_gene_clusters",
    "sunbeam-labs/sbx_virus_id",
    "sunbeam-labs/sbx_genome_assembly",
    "Ulthran/sbx_marker_magu",
    "Ulthran/sbx_mgv",
    "Ulthran/sbx_seeker",
    "Ulthran/sbx_genomad",
    "Ulthran/sbx_phold",
    "Ulthran/demic",
    "PennChopMicrobiomeProgram/unassigner",
    "PennChopMicrobiomeProgram/ZIBR",
    "lakerwsl/DAFOT",
    "Ulthran/ShotgunUnifrac",
    "Ulthran/pycov3",
    "PennChopMicrobiomeProgram/primertrim",
    "PennChopMicrobiomeProgram/dnabc",
    "kylebittinger/heyfastq",
    "PennChopMicrobiomeProgram/SampleRegistry",
    "Ulthran/conda_env_check",
    "sunbeam-labs/sbx_template",
    "sunbeam_labs/sbx_test_action",
]


def project_pages() -> list[str]:
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
