class DocumentProcessor:
    def process(self, state):
        # In our current flow, documents are already processed during upload
        # So we'll just pass through the state
        # In a more complex version, this could handle additional processing
        return state