# git_diff.py
import subprocess

def get_changed_files(base_branch, pr_branch):
    cmd = f"git diff {base_branch}...{pr_branch} --name-only"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    changed_files = result.stdout.strip().split('\n')
    if changed_files == ['']:
        changed_files = []
    return changed_files
