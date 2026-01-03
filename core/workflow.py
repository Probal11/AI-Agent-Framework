from core.state import StateStore
from core.audit import AuditLogger
class Workflow:
    def __init__(self, name):
        self.name = name
        self.tasks = {}
        self.state = StateStore()
        self.audit = AuditLogger()
    def add_task(self, task_node):
        self.tasks[task_node.task_id] = task_node
    def run(self):
        self.audit.log("WORKFLOW_START", self.name)
        completed = set()
        while len(completed) < len(self.tasks):
            for task_id, task in self.tasks.items():
                if task_id in completed:
                    continue

                if all(dep in completed for dep in task.depends_on):
                    context = self.state.as_text()
                    result = task.agent.execute(task.prompt, context)
                    self.state.set(task_id, result)
                    completed.add(task_id)

        self.audit.log("WORKFLOW_COMPLETE", self.name)
        return self.state._store
