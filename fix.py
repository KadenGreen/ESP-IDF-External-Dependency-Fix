#!/usr/bin/env python3
"""
ESP-IDF Component Manager Helper Script

Generates a minimal CMakeLists.txt for non-ESP-IDF libraries,
keeping glob to scan for source files. Print messages only
appear when run manually.
"""

import os
import sys
from glob import glob

def create_cmake(component_path: str, src_dir: str = "src", include_dir: str = "inc", verbose: bool = False):
    """
    Creates a minimal CMakeLists.txt in the component folder.

    Args:
        component_path: Path to the library folder (managed_components/<lib>)
        src_dir: Subdirectory containing source files (default 'src')
        include_dir: Subdirectory containing headers (default 'inc')
        verbose: If True, prints status messages
    """
    cmake_file = os.path.join(component_path, "CMakeLists.txt")

    if not os.path.exists(component_path):
        if verbose:
            print(f"Component path '{component_path}' does not exist. Skipping.")
        return

    if os.path.exists(cmake_file):
        if verbose:
            print(f"CMakeLists.txt already exists for '{component_path}'. Skipping.")
        return

    # Always write wildcard
    c_files_line = f'    SRCS "{src_dir}/*.c"\n'

    # Write CMakeLists.txt
    with open(cmake_file, "w") as f:
        f.write("idf_component_register(\n")
        f.write(c_files_line)
        f.write(f'    INCLUDE_DIRS "{include_dir}"\n')
        f.write(")\n")

    if verbose:
        print(f"Created CMakeLists.txt for '{component_path}'")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_cmake.py <component_path> [src_dir] [include_dir]")
        sys.exit(1)

    create_cmake(sys.argv[1],
                 sys.argv[2] if len(sys.argv) > 2 else "src",
                 sys.argv[3] if len(sys.argv) > 3 else "inc",
                 verbose=True)