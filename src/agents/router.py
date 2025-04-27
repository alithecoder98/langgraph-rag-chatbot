class Router:
    def route(self, state):
        # Simple router that just passes to the next node
        # In a more complex version, this could decide different paths
        return "domain_selector"