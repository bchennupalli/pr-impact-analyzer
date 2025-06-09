# report_generator.py

def generate_report(impacted_modules):
    print("\n=== PR Impact Report ===")
    if not impacted_modules:
        print("No impacted modules detected.")
    else:
        for module in impacted_modules:
            print(f"- {module}")
