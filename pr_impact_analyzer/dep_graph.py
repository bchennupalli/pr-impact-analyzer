# dep_graph.py
import os
import ast
import networkx as nx

def build_dependency_graph(project_root=".", skip_venv=True):
    G = nx.DiGraph()

    for root, dirs, files in os.walk(project_root):
        # Optionally skip venv folder
        if skip_venv and 'venv' in root:
            continue

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                module_name = get_module_name(file_path, project_root)
                
                imports = get_imports(file_path)
                for imported_module in imports:
                    G.add_edge(module_name, imported_module)

    return G

def get_module_name(file_path, project_root):
    rel_path = os.path.relpath(file_path, project_root)
    module_name = rel_path.replace(os.sep, ".").replace(".py", "")
    return module_name


def get_imports(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            # Skip files that cannot be parsed
            return []

    imports = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)

    # Clean up names → only keep first part (to match module names)
    clean_imports = set()
    for name in imports:
        parts = name.split(".")
        if parts:
            clean_imports.add(name)

    return clean_imports
