def init_memory(goal: str) -> dict:
    return {
        "goal": goal,
        "steps": [],
        "completed": False
    }

#“Memory will grow later. Today it exists.”