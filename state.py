from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, END

class Task(TypedDict):
    id: str
    description: str
    assigned_agent: str
    status: str

class AgentState(TypedDict):
    project_root: str
    requirements: str
    architecture: Optional[str]
    
    task_queue: List[Task]
    current_task: Optional[Task]
    completed_tasks: List[Task]

    test_logs: Optional[str]
    test_status: str
    iteration_count: int