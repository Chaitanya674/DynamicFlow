import os
from workflow import app

os.makedirs("./builds", exist_ok=True)

inputs = {
    "requirements": "Create me a Simple HTML AND JavaScript based calculator that can perform addition, subtraction, multiplication, and division.",
    "project_root": "./builds/app-calculator",
    "architecture": None,
    "task_queue": [],
    "completed_tasks": [],
    "current_task": None,
    "test_logs": None,
    "test_status": "pending",
    "iteration_count": 0,
    "final_report": None
}

try:
    final_state = app.invoke(
        inputs, 
        config={"recursion_limit": 50}
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