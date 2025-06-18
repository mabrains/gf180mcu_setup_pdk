# =========================================================================================
# Copyright 2025 Mabrains Company
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================================

"""
setup_klayout.py — GF180MCU KLayout PDK Installer

Usage:
  setup_klayout.py (--tech_path=<tech_path>) (--klayout_home=<klayout_home>) (--python_env=<python_env>)

Options:
  -h, --help                         Show help text.
  -v, --version                      Show version.
  --tech_path=<tech_path>           Path to gf180mcu KLayout PDK (required).
  --klayout_home=<klayout_home>     Path to install KLayout symlink.
  --python_env=<python_env>         Path to Python virtual environment used for this tech.
"""

import os
import logging
from glob import glob
from pathlib import Path
from docopt import docopt

SHELL_TYPES = {
    "bash": ".bashrc",
    "zsh": ".zshrc",
    "fish": ".config/fish/config.fish",
    "csh": ".cshrc",
    "tcsh": ".tcshrc",
}


def detect_shell():
    shell = os.getenv("SHELL", "")
    for shell_type, rc_file in SHELL_TYPES.items():
        if shell.endswith(shell_type):
            return shell_type, os.path.expanduser(f"~/{rc_file}")
    return None, None


def add_line_to_rc(line: str):
    shell_type, rc_path = detect_shell()
    if shell_type and rc_path:
        with open(rc_path, "a") as f:
            f.write(f"\n{line}\n")
        logging.info(f"Added alias to {rc_path}")
    else:
        logging.error("Could not detect shell. Supported shells are:")
        logging.error(", ".join(SHELL_TYPES.keys()))
        exit(1)


def klayout_env_setup(klayout_home: str, python_env: str):
    env_dir = os.path.abspath(os.path.expanduser(python_env))
    python_path = os.path.join(env_dir, "lib", "python*", "site-packages")
    python_libs = glob(python_path)

    if not python_libs or not os.path.isdir(python_libs[0]):
        logging.error(f"Python lib path {python_path} not found.")
        exit(1)

    python_lib = python_libs[0]

    alias = (
        f"alias klayout_gf180mcu='KLAYOUT_PATH={klayout_home}:{klayout_home}/tech "
        f"KLAYOUT_PYTHONPATH={python_lib} klayout -e'"
    )
    add_line_to_rc(alias)


def check_klayout_version():
    try:
        version_str = os.popen("klayout -b -v").read().strip().split()[-1]
        major, minor, patch = (int(x) for x in version_str.split("."))
    except Exception:
        logging.error("Failed to parse KLayout version.")
        exit(1)

    if (major, minor, patch) < (0, 29, 11):
        logging.error("KLayout >= 0.29.11 is required.")
        logging.error(f"Detected version: {version_str}")
        exit(1)

    logging.info(f"KLayout version OK: {version_str}")


def make_link(src: str, dest: str):
    src_path = Path(src)
    dest_path = Path(dest)

    if not src_path.exists():
        logging.error(f"Tech path does not exist: {src_path}")
        exit(1)

    if dest_path.exists() or dest_path.is_symlink():
        logging.info(f"Removing existing path: {dest_path}")
        os.remove(dest_path)

    try:
        os.symlink(src_path, dest_path, target_is_directory=True)
        logging.info(f"Symlink created:\nFrom: {src_path}\nTo:   {dest_path}")
    except OSError as err:
        logging.error(f"Failed to create symlink: {err}")
        exit(1)


def main(tech_path: str, klayout_home: str, python_env: str):
    check_klayout_version()

    tech_path_abs = os.path.abspath(os.path.expanduser(tech_path))
    klayout_home_abs = os.path.abspath(os.path.expanduser(klayout_home))
    Path(klayout_home_abs).parent.mkdir(parents=True, exist_ok=True)

    make_link(src=tech_path_abs, dest=klayout_home_abs)
    klayout_env_setup(klayout_home=klayout_home_abs, python_env=python_env)

    logging.info("✅ KLayout-GF180MCU tech installed successfully.")

# ================================================================
# -------------------------- MAIN --------------------------------
# ================================================================


if __name__ == "__main__":
    arguments = docopt(__doc__, version="setup_klayout.py 1.0")

    tech_path = arguments["--tech_path"]
    klayout_home = arguments["--klayout_home"]
    python_env = arguments["--python_env"]

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%d-%b-%Y %H:%M:%S",
    )

    main(tech_path, klayout_home, python_env)
