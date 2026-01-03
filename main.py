from dotenv import load_dotenv
load_dotenv()
from core.agent import Agent
from core.task import TaskNode
from core.workflow import Workflow
from ingress.cli import get_user_input
def main():
    topic = get_user_input()
    researcher = Agent(
        "Researcher",
        "Find three factual points about the topic."
    )

    writer = Agent(
        "Writer",
        "Write a short blog post using the facts."
    )

    reviewer = Agent(
        "Reviewer",
        "Review the blog post and suggest one improvement."
    )

    workflow = Workflow("AI Blog Pipeline")

    workflow.add_task(TaskNode(
        "research",
        researcher,
        f"Research the topic: {topic}"
    ))

    workflow.add_task(TaskNode(
        "write",
        writer,
        "Write a blog post.",
        depends_on=["research"]
    ))

    workflow.add_task(TaskNode(
        "review",
        reviewer,
        "Review the blog post.",
        depends_on=["write"]
    ))

    result = workflow.run()

    print("\nFINAL OUTPUT\n")
    for k, v in result.items():
        print(f"{k.upper()}:\n{v}\n")
run=main()
print(run)