# LangGraph Agent Review

Simple repository to review and test basic concepts of LangGraph agents.

## Setup

### 1. Create Conda Environment

Follow these steps if you don't have the environment set up:

```bash
conda create -n agents python=3.12
conda activate agents
conda install -c conda-forge poetry
# Optional: Export environment history (already done in environment.yml)
# conda env export --from-history > environment.yml
```

If you already have the `environment.yml` file, you can create the environment with:

```bash
conda env create -f environment.yml
conda activate agents
```

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