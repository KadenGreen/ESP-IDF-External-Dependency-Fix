# ESP-IDF-External-Dependency-Fix
Script to make non-ESP-IDF libraries compatible with ESP-IDF’s Component Manager.
First build will fail because it does the check for managed status right after cloning, delete the build folder, build again, and it'll handle it.