# api_mapper.py

def map_fastapi_routes(app):
    """
    Extract FastAPI route mappings:
    Returns dict: {path: module_name}
    """
    routes = {}

    for route in app.routes:
        # route.endpoint is the handler function → .__module__ gives module
        if hasattr(route, "endpoint"):
            module_name = route.endpoint.__module__
            routes[route.path] = module_name

    return routes


def map_flask_routes(app):
    """
    Extract Flask route mappings:
    Returns dict: {path: module_name}
    """
    routes = {}

    for rule in app.url_map.iter_rules():
        endpoint = app.view_functions.get(rule.endpoint)
        if endpoint:
            module_name = endpoint.__module__
            routes[str(rule)] = module_name

    return routes
