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
    "PennChopMicrobiomeProgram/CHOP_metadata_checker",
    "Ulthran/conda_env_check",
    "sunbeam-labs/sbx_template",
    "sunbeam_labs/sbx_test_action",
]


def _get_pages(template_fp: Path) -> list[str]:
    return [fp.stem for fp in template_fp.glob("*.html")]


def project_pages() -> list[str]:
    return _get_pages(Path("app/templates/projects"))


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
        "XKCD Quoter",
        "Definitely Human",
        "Automating Processes",
        "Developing Solutions",
    ]
    return random.choice(attrs)
