# cli.py

import argparse
from pr_impact_analyzer.git_diff import get_changed_files
from pr_impact_analyzer.dep_graph import build_dependency_graph
from pr_impact_analyzer.impact_mapper import map_impact
from pr_impact_analyzer.utils import print_api_routes, print_impacted_modules

def main():
    parser = argparse.ArgumentParser(description="PR Impact Analyzer CLI")
    parser.add_argument("--base", required=True, help="Base branch")
    parser.add_argument("--pr", required=True, help="PR branch or HEAD")

    args = parser.parse_args()

    changed_files = get_changed_files(args.base, args.pr)
    dep_graph = build_dependency_graph()
    impacted = map_impact(changed_files, dep_graph)

    report_lines = []
    report_lines.append("[*] Analyzing Git diff...")
    report_lines.append(f"[+] Changed files: {changed_files}\n")

    report_lines.append("[*] Building dependency graph...")
    report_lines.append("[*] Mapping impact...")
    report_lines.append("[*] Generating report...\n")

    report_lines.append("### Impacted Modules:\n")
    for module in impacted:
        report_lines.append(f"- {module}")

    try:
        from pr_impact_analyzer.api_mapper import map_fastapi_routes
        import sys
        import os
        from dotenv import load_dotenv

        # Read env vars for FastAPI project
        fastapi_project_path = os.getenv("FASTAPI_PROJECT_PATH")
        dotenv_path = os.getenv("FASTAPI_DOTENV_PATH")

        if fastapi_project_path and dotenv_path:
            load_dotenv(dotenv_path=dotenv_path)
            sys.path.insert(0, fastapi_project_path)
            from app.main import app as fastapi_app

            fastapi_routes = map_fastapi_routes(fastapi_app)
            report_lines.append("\n### API Routes:\n")
            for path, module in fastapi_routes.items():
                report_lines.append(f"{path} → {module}")
        else:
            report_lines.append("\n[!] Skipping API route mapping (FASTAPI_PROJECT_PATH and FASTAPI_DOTENV_PATH not set)\n")

    except Exception as e:
        report_lines.append(f"\n[!] Could not map API routes (FastAPI). Reason: {e}")


    # Output report to file for GitHub Action to post as PR comment
    with open("impact_report.txt", "w") as f:
        for line in report_lines:
            f.write(line + "\n")

    # Also print to console
    for line in report_lines:
        print(line)

if __name__ == "__main__":
    main()
