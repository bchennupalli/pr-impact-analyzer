# utils.py

def print_api_routes(title, api_routes):
    print(f"\n=== {title} ===")
    if not api_routes:
        print("No API routes detected.")
    else:
        for path, module in sorted(api_routes.items()):
            print(f"{path} → {module}")

def print_impacted_modules(impacted_modules):
    print("\n=== Impacted Modules ===")
    if not impacted_modules:
        print("No impacted modules detected.")
    else:
        for module in sorted(impacted_modules):
            print(f"- {module}")
