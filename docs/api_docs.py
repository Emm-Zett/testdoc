"""Generate (virtual) API documentation for digiplan."""
from pathlib import Path

import mkdocs_gen_files


docs_dir = Path("docs/api")

PACKAGE_DIR = Path("digiplan/map")
SKIP_MODULES = ["__init__", "__pycache__", "admin", "storage"]

for module in PACKAGE_DIR.iterdir():
    if module.stem in SKIP_MODULES:
        continue
    rel_path = Path("api", module.stem)  # e.g. api/mypackage/module.py
    file_path = rel_path.with_suffix(".md")

    module_path = f"{str(PACKAGE_DIR).replace('/', '.')}.{module.stem}"
    with mkdocs_gen_files.open(file_path, "w") as f:
        f.write(f"# `{module_path}`\n\n")
        f.write(f"::: {module_path}\n")
        f.write(f"    handler: python\n")
        f.write(f"    options:\n")
        f.write(f"      show_submodules: true\n")
        f.write(f"      show_root_toc_entry: true\n")
        f.write(f"      show_root_full_path: true\n")

    mkdocs_gen_files.set_edit_path(file_path, PACKAGE_DIR / module.stem)
