import json
import shutil
from pathlib import Path
from loguru import logger

from src.data import DATA_DIR
from src.utils.io import read_json


class OrganizeFiles:
    def __init__(self, directory):
        self.directory = Path(directory)
        



        ext_dirs = read_json(DATA_DIR / "extension.json")
        self.extensions_dest = {}
        for dir_name, ext_list in ext_dirs.items():
           for ext in ext_list:
               self.extensions_dest[ext] = dir_name

    def __call__(self):
        """
            Organizing files in directory by moving them
            to sub directions based on extension
        """
        logger.info(f"Organizing files in {self.directory}...")
        file_extention = []
        for file_path in self.directory.iterdir():
            if file_path.is_dir():
                continue
            file_extention.append(file_path.suffix)
            if file_path.suffix not in self.extensions_dest:

                DEST_DIR = self.directory / "other"
            else:
                DEST_DIR = self.directory / self.extensions_dest[file_path.suffix]
            DEST_DIR.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(DEST_DIR))
            logger.info(f"moving {file_path} to {DEST_DIR}...")


if __name__== "__main__":
    org_files = OrganizeFiles("/mnt/c/Users/Mehrnoosh/Downloads")
    org_files()
    logger.info("Done!")






