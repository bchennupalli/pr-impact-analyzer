# PR Impact Analyzer

**PR Impact Analyzer** is a lightweight CLI tool that helps you understand the impact of your Pull Requests:

✅ Shows which **modules** are impacted  
✅ Shows which **API Routes** (FastAPI / Flask) may be impacted  
✅ Works on large projects → proven on full-stack FastAPI apps  
✅ Easy to integrate with GitHub Actions or CI/CD  

---

## Features

- Analyze Git diffs between branches
- Build static code dependency graph
- Map changed files → impacted modules
- Map impacted modules → API routes (FastAPI supported)
- CLI output + easy HTML report integration possible

---

## Example Output

```plaintext
[*] Analyzing Git diff...
[+] Changed files: ['pr_impact_analyzer/cli.py']
[*] Building dependency graph...
[*] Mapping impact...
[*] Generating report...

=== Impacted Modules ===
- app.main
- argparse
- ast
- dotenv
- networkx
- os
- pr_impact_analyzer.api_mapper
- pr_impact_analyzer.cli
- pr_impact_analyzer.dep_graph
- pr_impact_analyzer.git_diff
- pr_impact_analyzer.impact_mapper
- pr_impact_analyzer.utils
- subprocess
- sys

=== API Routes (FastAPI) ===
/api/v1/items/ → app.api.routes.items
/api/v1/items/{id} → app.api.routes.items
/api/v1/login/access-token → app.api.routes.login
/api/v1/users → app.api.routes.users
...
![CI](https://github.com/yourusername/pr-impact-analyzer/actions/workflows/ci.yml/badge.svg)
