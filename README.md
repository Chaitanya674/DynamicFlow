# DynamicFlow

A modular, fully automated multi-agent development pipeline that transforms plain-text app descriptions into complete, working software applications with integrated backend, frontend, and optional database layers.

**DynamicFlow** orchestrates multiple AI agents, tool functions, and structured prompts to handle the entire development lifecycle—from architecture design to code generation, testing, and debugging—enabling rapid prototyping and full-stack application development without manual coding.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER INPUT (App Idea)                           │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
        ┌────────────────────────────────────────────┐
        │      System Architect Agent                │
        │  • Interprets requirements                 │
        │  • Designs high-level architecture         │
        │  • Recommends frameworks & tools           │
        │  • Plans directory structure               │
        └────────┬─────────────────────────────────────┘
                 │
                 ▼
        ┌────────────────────────────────────────────┐
        │      Planner Agent                         │
        │  • Converts architecture to tasks          │
        │  • Creates ordered task list               │
        │  • Assigns backend/frontend tasks          │
        └────────┬─────────────────────────────────────┘
                 │
                 ▼
        ┌────────────────────────────────────────────┐
        │      Orchestrator Agent                    │
        │  • Manages execution pipeline              │
        │  • Ensures task ordering                   │
        │  • Maintains workflow consistency          │
        └────────┬─────────────────────────────────────┘
                 │
         ┌───────┴──────────┐
         │                  │
         ▼                  ▼
    ┌─────────────┐   ┌──────────────────┐
    │  Backend    │   │  Frontend        │
    │  Developer  │   │  Developer       │
    │  Agent      │   │  Agent           │
    │             │   │                  │
    │ • Generates │   │ • Generates UI   │
    │   server    │   │ • Creates        │
    │   code      │   │   components     │
    │ • Creates   │   │ • Builds styling │
    │   APIs      │   │ • Implements     │
    │ • Sets up   │   │   logic          │
    │   database  │   │                  │
    └──────┬──────┘   └────────┬─────────┘
           │                   │
           └────────┬──────────┘
                    │
                    ▼
        ┌────────────────────────────────────────────┐
        │      QA Tester Agent                       │
        │  • Runs the application                    │
        │  • Captures logs & errors                  │
        │  • Validates functionality                 │
        └────────┬─────────────────────────────────────┘
                 │
           ┌─────┴──────┐
           │            │
        Success      Error
           │            │
           │            ▼
           │   ┌────────────────────────────────┐
           │   │  Debugger/Resolver Agent       │
           │   │  • Analyzes errors             │
           │   │  • Creates repair tasks        │
           │   │  • Feeds back to pipeline      │
           │   └─────────┬──────────────────────┘
           │             │
           │             └──────┐
           │                    │
           └────────┬───────────┘
                    │
                    ▼
        ┌────────────────────────────────────────────┐
        │    WORKING APPLICATION                     │
        │    📁 builds/<app-name>/                   │
        │    ├── backend/                            │
        │    ├── frontend/                           │
        │    └── README.md                           │
        └────────────────────────────────────────────┘
```

---

## 🚀 Overview

DynamicFlow operates through a chain of specialized agents that collaborate to produce a complete application:

1. **System Architect**
   Interprets the user’s app idea and produces a high-level architecture, recommended tools, frameworks, directory structure, and design reasoning.

2. **Planner Agent**
   Converts architecture into actionable tasks, assigns the appropriate agent (backend or frontend), and outputs a full ordered task list.

3. **Orchestrator Agent**
   Oversees the task execution pipeline, ensures ordering, assigns responsibilities, and maintains workflow consistency.

4. **Backend Developer Agent**
   Generates backend code using the enforced `write_file` tool.

5. **Frontend Developer Agent**
   Generates frontend/UI code using the same tool.

6. **QA Tester**
   Runs the application using `run_shell_command`, captures logs, and passes results to the debugger.

7. **Debugger/Resolver**
   Analyzes errors and produces a repair task for the pipeline.

Each agent operates under strict JSON outputs, tool restrictions, and directory constraints.

---

## 🧩 Key Features

### **1. Multi-Agent Collaboration**

Each agent has a well-defined role with enforced constraints to prevent cross-contamination of responsibilities or accidental code drops in chat.

### **2. Strict Tooling Enforcement**

DynamicFlow uses custom tools such as:

* `write_file`
* `run_shell_command`

Files are written only inside `./builds/<app-name>/` and missing directories are auto-created.

### **3. Full Project Generation**

From a simple description like:

> "Build a todo app with login and dark mode."

The system will automatically:

* Plan folder structure
* Generate backend framework setup
* Generate frontend interface
* Set up database schema (if needed)
* Create all files
* Test the output
* Debug errors
* Produce a working application

### **4. Robust Task Planning and Execution**

Planner tasks are deterministic, ordered, and assigned to `backend` or `frontend`.

### **5. Self-Healing Pipeline**

If code fails:

1. Tester captures logs
2. Debugger creates a fix task
3. System resumes execution

---

## 📁 Directory Structure

DynamicFlow stores all generated apps inside:

```
./builds/<app-name>/
```

Files generated by agents always follow this constraint.

Example:

```
builds/
  todo-app/
    backend/
    frontend/
    README.md
```

---

## 🔧 Core Tools

### **`write_file(file_path, content)`**

Writes files inside the `./builds` directory.
Automatically creates missing folders, ensures path safety, and saves content exactly as given.

### **`run_shell_command(command)`**

Executes terminal commands for testing and validation.

---

## 🧠 Agent Prompt Templates

DynamicFlow uses a suite of structured prompts:

* **architect_prompt**
* **planner_prompt**
* **orchestrator_prompt**
* **backend_prompt_template**
* **frontend_prompt_template**
* **tester_prompt_template**
* **debugger_prompt**

These enforce consistent behavior, validate outputs, and ensure strict JSON responses.

---

## 🏗 How DynamicFlow Works Internally

1. **Input:** User describes an application.
2. **Architect:** Creates system architecture.
3. **Planner:** Generates ordered tasks.
4. **Orchestrator:** Assigns each task.
5. **Developers:** Create code using `write_file`.
6. **Tester:** Runs the app.
7. **Debugger:** Fixes errors.
8. **Loop:** Continues until successful.
9. **Output:** A complete, runnable project.

---

## 🛠 Extending DynamicFlow

DynamicFlow is modular; you can add:

* New agents
* Custom tool functions
* New frameworks (React, FastAPI, NodeJS, etc.)
* Additional build steps
* Custom testing routines

---

## ⚠️ Safety & Constraints

* All generated files must stay inside `./builds/`.
* Agents must not output raw code in chat.
* All agent-to-tool communication is strictly validated.
* Output must remain deterministic and in JSON.
