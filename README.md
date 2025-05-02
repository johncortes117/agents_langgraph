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

### FastAPI Application

Alternatively, run the FastAPI application which exposes the agent via an API endpoint:

```bash
fastapi dev app/api.py
```