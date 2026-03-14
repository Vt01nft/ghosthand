"""GHOSTHAND — Custom Tools"""

import datetime

_memory = {}

def save_progress(step_description: str, status: str) -> dict:
    """Saves the current project progress so GHOSTHAND remembers what you've done.

    Args:
        step_description: What was just completed (e.g. "connected the red wire to terminal A").
        status: Either 'completed', 'in_progress', or 'skipped'.

    Returns:
        dict: Confirmation of what was saved.
    """
    ts = datetime.datetime.now().isoformat()
    if "steps" not in _memory:
        _memory["steps"] = []
    _memory["steps"].append({"step": step_description, "status": status, "time": ts})
    return {"saved": step_description, "status": status, "total_steps": len(_memory["steps"])}


def get_progress() -> dict:
    """Returns all saved project progress so far.

    Returns:
        dict: List of all completed, in-progress, and skipped steps.
    """
    steps = _memory.get("steps", [])
    if not steps:
        return {"status": "No progress saved yet. Start working and I'll track your steps."}
    return {"total_steps": len(steps), "steps": steps}


def check_safety(situation: str) -> dict:
    """Checks a described situation for safety hazards.

    Use this when you see something that might be dangerous — exposed wires,
    wrong connections, unstable structures, sharp edges, chemical labels.

    Args:
        situation: Description of what you observed that might be risky.

    Returns:
        dict: Risk level and recommended action.
    """
    s = situation.lower()
    critical = ["exposed wire", "live wire", "electric shock", "gas leak", "fire",
                "short circuit", "capacitor", "high voltage", "battery leak"]
    warning = ["sharp edge", "hot surface", "wrong polarity", "reversed",
               "loose connection", "unstable", "incorrect wiring", "stripped"]

    level = "SAFE"
    found = []
    for kw in critical:
        if kw in s:
            level = "DANGER"
            found.append(kw)
    for kw in warning:
        if kw in s:
            if level != "DANGER":
                level = "CAUTION"
            found.append(kw)

    return {
        "risk_level": level,
        "hazards_found": found if found else ["none detected"],
        "action": {
            "DANGER": "STOP IMMEDIATELY. Do not touch. Address this before continuing.",
            "CAUTION": "Proceed carefully. Double-check before continuing.",
            "SAFE": "No immediate hazards detected. Proceed normally.",
        }[level]
    }
