# PR Impact Analyzer

PR Impact Analyzer helps you understand **which APIs, modules, and system parts are impacted by a Pull Request**, not just which files changed.

✅ Builds a full code dependency graph  
✅ Maps changes to API endpoints / modules  
✅ Reports **impact radius** of a PR  
✅ Works as CLI tool, GitHub bot, and Web dashboard

## Example Output

<img src="example_report.png" alt="Example Impact Report" width="600"/>

## Features

- Analyze PR diffs
- Build code dependency graph
- Map changes to system impact (APIs, modules)
- CLI report / HTML / GitHub bot comments

## Roadmap

- Python support (initial)
- JavaScript/TypeScript support (next)
- Java support (later)
- Test impact suggestion
- Infra impact suggestion
- Web dashboard

## Getting Started

```bash
pip install pr-impact-analyzer
pr-impact-analyzer --base main --pr feature-branch
