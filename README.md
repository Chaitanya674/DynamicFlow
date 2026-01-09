Codeflow 🚀
===========

**Bridging the Gap Between Code, Product, and People.**

> _Automated Technical Documentation, Architecture Visualization, and Knowledge Base Management powered by AI Agents._

🎯 The Mission
--------------

In fast-paced engineering teams, a silent disconnect often grows between the **Code** (what exists) and the **Business** (what is understood).

*   **Managers & Product Owners** struggle to get deep technical insights without interrupting developers.
    
*   **New Hires** waste days or weeks in repetitive "Knowledge Transfer" (KT) sessions just to set up their environment.
    
*   **Open Source Contributors** shy away from complex repositories because the learning curve is too steep.
    

**Codeflow** solves this by treating **Documentation as Code**. It employs a swarm of AI agents to reverse-engineer your repository, visualize its architecture, and publish professional, living documentation directly to Confluence.

💡 Key Features
---------------

### 1\. 🔍 Automated Repo Analysis & Visualization

Codeflow scans your entire repository structure to extract:

*   **Barebone Structure**: File trees and class hierarchies.
    
*   **Execution Flow**: Logic paths (Caller $\\rightarrow$ Callee).
    
*   **Architecture Diagrams**: Automatically generates complex **Mermaid.js** charts (Flowcharts, Sequence diagrams) and renders them as high-quality images.
    

### 2\. 📄 One-Click Confluence Pages

Stop writing docs manually. Codeflow drafts comprehensive Confluence pages including:

*   System Overviews.
    
*   Technical Architecture.
    
*   Step-by-step Logic Flows.
    
*   Embedded Diagrams.
    

### 3\. 🔄 Smart Updates & Changelogs

Documentation goes stale the moment it's written—unless it updates itself.

*   **Changelog Agent**: Scans git history to generate human-readable "Release Notes" (Features vs. Fixes).
    
*   **Smart Updater**: Intelligently appends new sections (like "Business Logic" or "New Features") to _existing_ pages without overwriting current content.
    

### 4\. 🛡️ Human-in-the-Loop Approval

AI drafts it; You own it.

*   Codeflow presents a draft before publishing.
    
*   **Refinement Loop**: Don't like the tone? Want more detail? Just ask the agent to "Redraft," and it refines the content until you click **APPROVE**.
    

🏗️ System Architecture
-----------------------

Codeflow runs on a multi-agent orchestration architecture powered by **Google Gemini 2.5**.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   graph TD      User[User / Developer] -->|Query| Orch{Orchestrator Agent}      Orch -->|General Q| Chat[Chat Agent]      Orch -->|Create Docs| Data[Data Agent]      Orch -->|Update Page| Update[Updater Agent]      Orch -->|Release Notes| Change[Changelog Agent]      subgraph "Data Extraction"          Data --> Repo[Repo Architect]          Data --> Flow[Flow Creator]      end      Repo -->|Structure| Draft[Confluence Drafter]      Flow -->|Mermaid Code| Draft      Draft -->|Markdown| Approval{Human Approval}      Update -->|Merged Content| Approval      Change -->|Release Notes| Approval      Approval -- REJECT --> Refine[Refiner Agent]      Refine --> Approval      Approval -- APPROVE --> Conf((Confluence API))   `

### The Agent Squad

*   **Orchestrator**: The brain. Routes requests (Create vs. Update vs. Chat).
    
*   **Repo Architect**: Reverse-engineers code structure.
    
*   **Flow Creator**: Writes Mermaid.js syntax for visualizations.
    
*   **Confluence Drafter**: Formats text into professional documentation.
    
*   **Updater Agent**: Merges new insights into existing live pages.
    
*   **Refiner Agent**: Handles your feedback loop.
    

🚀 Getting Started
------------------

### Prerequisites

*   Python 3.10+
    
*   Google Cloud Project (for Gemini API)
    
*   Atlassian Confluence Account (API Key + Email)
    
*   GitHub Copilot MCP (Model Context Protocol) Access
    

### Installation

1.  git clone \[https://github.com/yourusername/codeflow.git\](https://github.com/yourusername/codeflow.git)cd codeflow
    
2.  pip install -r requirements.txt
    
3.  export CONFLUENCE\_DOMAIN="\[https://your-domain.atlassian.net\](https://your-domain.atlassian.net)"export CONFLUENCE\_EMAIL="your-email@example.com"export CONFLUENCE\_API\_KEY="your-atlassian-api-token"export GITHUB\_API\_KEY="your-github-token"export GOOGLE\_API\_KEY="your-gemini-key"
    
4.  python main.py
    

🤝 Contributing
---------------

We believe in making knowledge accessible. Whether you want to add new agents (e.g., a "Security Auditor Agent"), improve the diagram styles, or support Notion/Obsidian exports, we welcome your contributions!

1.  Fork the repo.
    
2.  Create your feature branch (git checkout -b feature/AmazingFeature).
    
3.  Commit your changes (git commit -m 'Add some AmazingFeature').
    
4.  Push to the branch (git push origin feature/AmazingFeature).
    
5.  Open a Pull Request.
    

📜 License
----------

Distributed under the MIT License. See LICENSE for more information.

> _Built with ❤️ to kill the phrase "I don't know how that works."_