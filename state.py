from typing import TypedDict, List, Optional, Annotated
from langgraph.graph import StateGraph, END
import operator

class Task(TypedDict):
    id: str
    description: str
    assigned_agent: str
    status: str

class AgentState(TypedDict):
    """Main state for the entire workflow"""
    project_root: str
    requirements: str
    architecture: Optional[str]
    
    task_queue: List[Task]
    current_task: Optional[Task]
    # Use Annotated with operator.add to allow parallel workers to write concurrently
    completed_tasks: Annotated[List[Task], operator.add]

    test_logs: Optional[str]
    test_status: str
    iteration_count: int
    final_report: Optional[str]  # Synthesized results from all workers


class WorkerState(TypedDict):
    """State for individual worker execution - receives single task"""
    task: Task
    project_root: str
    # Workers write back to this key which merges with main state
    completed_tasks: Annotated[List[Task], operator.add]