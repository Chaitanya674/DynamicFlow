import os
from state import AgentState
from langgraph.graph import StateGraph, END
from tools import llm, llm_worker
from workflow import app 

os.makedirs("./builds", exist_ok=True)

inputs = {
    "requirements": "Create a simple To-Do List web app. "
                    "Backend: Python FastAPI with 2 endpoints (GET /tasks, POST /tasks). "
                    "Frontend: A single HTML file that fetches tasks from the API and displays them. "
                    "Database: Use a simple JSON file (tasks.json) for storage.",
    
    "project_root": "./builds/todo-app",

    "architecture": None,
    "task_queue": [],
    "completed_tasks": [],
    "current_task": None,
    "test_logs": None,
    "test_status": "pending",
    "iteration_count": 0
}

try:
    # app.invoke returns the FINAL state after the graph finishes
    final_state = app.invoke(
        inputs, 
        config={"recursion_limit": 50} # Safety limit for loops
    )

    # 4. Report Final Results
    print("\n" + "="*50)
    print("🏁 WORKFLOW FINISHED")
    print("="*50)
    print(f"Final Test Status: {final_state['test_status'].upper()}")
    print(f"Total Iterations:  {final_state['iteration_count']}")
    print(f"Tasks Completed:   {len(final_state['completed_tasks'])}")

except Exception as e:
    print(f"\n❌ Execution Error: {e}")