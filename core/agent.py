import os
import time
import google.generativeai as genai
from core.audit import AuditLogger
class Agent:
    def __init__(
        self,
        name,
        role,
        model="gemini-2.5-flash",
        retries=3,
        timeout=15
    ):
        self.name = name
        self.role = role
        self.retries = retries
        self.timeout = timeout

        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.client = genai.GenerativeModel(model)
        self.audit = AuditLogger()

    def execute(self, task, context):
        self.audit.log("TASK_START", self.name, {"task": task})

        prompt = f"""
You are acting as: {self.role}

Context:
{context}

Task:
{task}

Return only the final result.
"""

        for attempt in range(1, self.retries + 1):
            try:
                start = time.time()
                response = self.client.generate_content(prompt)
                latency = time.time() - start

                if latency > self.timeout:
                    raise TimeoutError("LLM timeout")

                output = response.text.strip()
                if not output:
                    raise ValueError("Empty response")

                self.audit.log(
                    "TASK_SUCCESS",
                    self.name,
                    {"latency": latency}
                )
                return output

            except Exception as e:
                self.audit.log(
                    "TASK_RETRY",
                    self.name,
                    {"attempt": attempt, "error": str(e)}
                )

        raise RuntimeError(f"{self.name} failed after retries")
