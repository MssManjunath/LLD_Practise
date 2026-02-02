"""
TEST FILE: In-Memory File System

Instructions to Candidate:
--------------------------
- Run these tests after implementing FileSystem
- You may add more tests if you feel necessary
"""

from filesystem import FileSystem


def test_basic_file_system_flow():
    """
    Happy path:
    - create directories
    - add a file
    - read it
    - list directories
    """
    fs = FileSystem()

    fs.mkdir("/a")
    fs.mkdir("/a/b")
    fs.add_file("/a/b/file.txt", "hello")

    assert fs.read_file("/a/b/file.txt") == "hello"
    assert fs.ls("/") == ["a"]
    assert fs.ls("/a") == ["b"]
    assert fs.ls("/a/b") == ["file.txt"]
    assert fs.ls("/a/b/file.txt") == ["file.txt"]


def test_error_cases():
    """
    Failure cases:
    - duplicate creation
    - reading directory as file
    """
    fs = FileSystem()

    fs.mkdir("/dir")

    # Duplicate directory
    try:
        fs.mkdir("/dir")
        assert False, "Expected exception for duplicate directory"
    except Exception:
        pass

    # Reading a directory as a file
    try:
        fs.read_file("/dir")
        assert False, "Expected exception when reading directory"
    except Exception:
        pass
