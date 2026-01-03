class TaskNode:
    def __init__(self, task_id, agent, prompt, depends_on=None):
        self.task_id = task_id
        self.agent = agent
        self.prompt = prompt
        self.depends_on = depends_on or []
