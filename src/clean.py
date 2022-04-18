import json
import shutil
import sys
from pathlib import Path
from typing import Union

from loguru import logger

from src.data import DATA_DIR
from src.utils.io import read_json


class OrganizeFiles:
    def __init__(self):
        ext_dirs = read_json(DATA_DIR / "extension.json")
        self.extensions_dest = {}
        for dir_name, ext_list in ext_dirs.items():
           for ext in ext_list:
               self.extensions_dest[ext] = dir_name

    def __call__(self, directory: Union[str, Path]):
        """
            Organizing files in directory by moving them
            to sub directions based on extension
        """
        directory = Path(directory)
        if not directory.exists():
            raise FileNotFoundError(f"{directory} dosnoot exist!")
        logger.info(f"Organizing files in {directory}...")
        file_extention = []
        for file_path in directory.iterdir():
            if file_path.is_dir():
                continue
            if file_path.name.startswith('.'):
                continue
            file_extention.append(file_path.suffix)
            if file_path.suffix not in self.extensions_dest:

                DEST_DIR = directory / "other"
            else:
                DEST_DIR = directory / self.extensions_dest[file_path.suffix]
            DEST_DIR.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(DEST_DIR))
            logger.info(f"moving {file_path} to {DEST_DIR}...")


if __name__== "__main__":
    org_files = OrganizeFiles()
    org_files(sys.argv[1])
    logger.info("Done!")






