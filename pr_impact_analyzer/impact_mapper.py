# impact_mapper.py

def map_impact(changed_files, dep_graph):
    impacted = set()

    for file in changed_files:
        # Convert file path to module name style (ex: api/user_api.py → api.user_api)
        module_name = file.replace("/", ".").replace(".py", "")
        
        if module_name in dep_graph:
            impacted.add(module_name)
            
            # Propagate through graph (BFS)
            stack = [module_name]
            while stack:
                current = stack.pop()
                for neighbor in dep_graph.successors(current):
                    if neighbor not in impacted:
                        impacted.add(neighbor)
                        stack.append(neighbor)
    return impacted
