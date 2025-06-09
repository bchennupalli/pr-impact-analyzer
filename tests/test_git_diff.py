# tests/test_git_diff.py
import subprocess
from pr_impact_analyzer.git_diff import get_changed_files

def test_get_changed_files():
    # You must be on test branch with some change for this to show result
    changed_files = get_changed_files("main", "HEAD")
    print("Changed files:", changed_files)

    assert isinstance(changed_files, list)
    assert all(isinstance(f, str) for f in changed_files)
