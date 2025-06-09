# PR Impact Analyzer

[![CI](https://github.com/bchennupalli/pr-impact-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/bchennupalli/pr-impact-analyzer/actions/workflows/ci.yml)
[![GitHub license](https://img.shields.io/github/license/bchennupalli/pr-impact-analyzer)](https://github.com/bchennupalli/pr-impact-analyzer/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/bchennupalli/pr-impact-analyzer?style=social)](https://github.com/bchennupalli/pr-impact-analyzer/stargazers)

---

**PR Impact Analyzer** is a lightweight CLI tool that helps you understand the impact of your Pull Requests:

✅ Shows which **modules** are impacted  
✅ Shows which **API Routes** (FastAPI / Flask) may be impacted  
✅ Works on large projects → proven on full-stack FastAPI apps  
✅ Easy to integrate with GitHub Actions or CI/CD  

---

## ✨ Features

- Analyze Git diffs between branches
- Build static code dependency graph
- Map changed files → impacted modules
- Map impacted modules → API routes (FastAPI supported)
- CLI output + GitHub PR comment supported
- Easy to integrate into GitHub Actions workflows
- Proven on full-stack FastAPI real-world projects

---

## 🚀 Example Output

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
```

---

## ⚙️ Installation

```bash
git clone https://github.com/bchennupalli/pr-impact-analyzer.git
cd pr-impact-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

---

## 🖥️ Usage (CLI)

```bash
python3 -m pr_impact_analyzer.cli --base main --pr HEAD
```

---

## 🛠️ Usage with FastAPI Apps

To map API Routes:

1️⃣ Create `.env` in your FastAPI project:

```env
PROJECT_NAME=PR Impact Test Project
POSTGRES_SERVER=localhost
POSTGRES_USER=testuser
FIRST_SUPERUSER=admin@example.com
FIRST_SUPERUSER_PASSWORD=password
```

2️⃣ In `cli.py`, update this section:

```python
load_dotenv(dotenv_path="/path/to/your/fastapi-project/backend/.env")
sys.path.insert(0, "/path/to/your/fastapi-project/backend")
from app.main import app as fastapi_app
```

✅ Done → API routes will be mapped and included in the report.

---

## 🔄 GitHub Actions Integration

Example `.github/workflows/ci.yml` included.

On every PR:

✅ Run CLI  
✅ Post PR Impact Report as a GitHub PR comment (via `sticky-pull-request-comment` action)

---

## 📦 Roadmap

✅ Phase 1: CLI tool  
✅ Phase 2: GitHub Action integration  
✅ Phase 3: GitHub PR comment support  
🚀 Phase 4: Impact-aware test selection  
🚀 Phase 5: Multi-language support (JavaScript / Java)  
🚀 Phase 6: Critical path highlighting (auth, payment, infra)

---

## 📄 License

MIT License.

---

## 🤝 Contributions

PRs are welcome!  
If you use this tool → ⭐️ the repo and spread the word 🚀.

---

## Author

Bhaskar Pramod Chennupalli — [https://github.com/bchennupalli](https://github.com/bchennupalli)

---
