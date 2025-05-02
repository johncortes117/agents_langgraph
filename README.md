# LangGraph Agent Review

Simple repository to review and test basic concepts of LangGraph agents.

## Setup

### 1. Create Conda Environment

The recommended way to create the Conda environment is using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate agents
```

This ensures you have the correct Python version and Poetry installed within the environment.

### 2. Install Dependencies

Once the conda environment is active and has Poetry, install the project dependencies:

```bash
poetry install
```

## Running the Agent

### LangGraph Development Server

You can run the agent using the LangGraph development server:

```bash
langgraph dev
```

This will start a local server (usually at `http://127.0.0.1:2024`) and provide a link to the LangSmith Studio UI for interacting with the graph.

### FastAPI Application

Alternatively, run the FastAPI application which exposes the agent via an API endpoint:

```bash
uvicorn app.api:app --reload
```

This will start the FastAPI server (usually at `http://127.0.0.1:8000`). You can access the agent's output by visiting `http://127.0.0.1:8000/` in your browser.