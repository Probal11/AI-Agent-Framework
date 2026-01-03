import json
import uuid
from datetime import datetime
class AuditLogger:
    def __init__(self, file_path="audit.log"):
        self.file_path = file_path

    def log(self, event, source, data=None):
        record = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "source": source,
            "data": data or {}
        }
        with open(self.file_path, "a") as f:
            f.write(json.dumps(record) + "\n")
