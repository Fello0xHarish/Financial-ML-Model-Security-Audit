"""Example of safer ML model handling."""

import os
from pathlib import Path

MODEL_DIR = Path("models").resolve()
MAX_MODEL_SIZE = 100 * 1024 * 1024  # 100 MB


def validate_model_path(filename: str) -> Path:
    """Allow only a simple filename inside the approved model directory."""
    name = Path(filename)

    if name.name != filename or filename in {"", ".", ".."}:
        raise ValueError("Invalid model filename")

    model_path = (MODEL_DIR / filename).resolve()

    if model_path.parent != MODEL_DIR:
        raise ValueError("Model must be stored in the approved directory")

    if not model_path.is_file():
        raise FileNotFoundError("Model file was not found")

    if model_path.stat().st_size > MAX_MODEL_SIZE:
        raise ValueError("Model file exceeds the size limit")

    return model_path


def get_api_key() -> str:
    """Read a secret from the environment instead of hardcoding it."""
    api_key = os.environ.get("ML_API_KEY")

    if not api_key:
        raise RuntimeError("ML_API_KEY environment variable is not set")

    return api_key


if __name__ == "__main__":
    print("Secure model-handling example ready.")
    print("Configure ML_API_KEY through your environment.")
