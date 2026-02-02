"""
INTERVIEW QUESTION: DESIGN A SIMPLE IN-MEMORY FILE SYSTEM

Time Limit:
-----------
40 minutes total
- 25 minutes: implement core logic
- 15 minutes: write tests + discuss design trade-offs

Problem Description:
--------------------
Design an in-memory file system that supports basic file and directory operations.

The file system:
- Uses UNIX-style absolute paths
- Has a single root directory "/"
- Supports directories and files
- Entire system runs in memory (no disk persistence)

You must implement the FileSystem class below.

Supported Operations:
---------------------
1. mkdir(path)        -> create a directory
2. add_file(path, content) -> create a file with content
3. read_file(path)   -> return file content
4. ls(path)           -> list directory contents OR file name

Rules & Constraints:
--------------------
1. All paths are absolute (start with "/")
2. Directory names and file names are non-empty strings
3. Creating a directory or file that already exists should raise an exception
4. Reading a directory as a file should raise an exception
5. ls():
   - If path is a file -> return [file_name]
   - If path is a directory -> return sorted list of child names
6. Root directory "/" always exists

Performance Expectations:
-------------------------
- mkdir      → O(L)
- add_file   → O(L)
- read_file  → O(L)
- ls         → O(L + K)

Where:
- L = number of components in the path
- K = number of entries in a directory

Example Usage:
--------------
# fs = FileSystem()
#
# fs.mkdir("/a")
# fs.mkdir("/a/b")
# fs.add_file("/a/b/file.txt", "hello")
#
# fs.read_file("/a/b/file.txt")      # returns "hello"
# fs.ls("/")                         # returns ["a"]
# fs.ls("/a")                        # returns ["b"]
# fs.ls("/a/b/file.txt")             # returns ["file.txt"]
#
# fs.add_file("/a/b/file.txt", "x")  # ERROR (already exists)

What We Are Evaluating:
----------------------
- Tree-based modeling of directories and files
- Clean traversal logic
- Correct edge-case handling
- Test-driven thinking
- Ability to explain complexity & extensibility
"""

class FileSystem:
    def __init__(self):
        pass

    def mkdir(self, path: str) -> None:
        """
        Creates a directory at the given path.
        """
        pass

    def add_file(self, path: str, content: str) -> None:
        """
        Creates a file with the given content.
        """
        pass

    def read_file(self, path: str) -> str:
        """
        Returns file content.
        """
        pass

    def ls(self, path: str) -> list[str]:
        """
        Lists directory contents or returns file name.
        """
        pass
