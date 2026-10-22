import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.secure_model_handling import (
    validate_model_path,
    get_api_key,
    MAX_MODEL_SIZE,
)


class TestSecureModelHandling(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.model_dir = Path(self.temp_dir.name).resolve()

        # Redirect the approved model directory to a temporary test directory.
        self.patcher = patch(
            "src.secure_model_handling.MODEL_DIR",
            self.model_dir,
        )
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_valid_model_path(self):
        model = self.model_dir / "model.keras"
        model.write_bytes(b"test model")
        self.assertEqual(validate_model_path("model.keras"), model)

    def test_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            validate_model_path("../outside.keras")

    def test_missing_model_rejected(self):
        with self.assertRaises(FileNotFoundError):
            validate_model_path("missing.keras")

    def test_oversized_model_rejected(self):
        model = self.model_dir / "large.keras"
        with model.open("wb") as f:
            f.truncate(MAX_MODEL_SIZE + 1)

        with self.assertRaises(ValueError):
            validate_model_path("large.keras")

    def test_missing_api_key_rejected(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(RuntimeError):
                get_api_key()

    def test_api_key_read_from_environment(self):
        with patch.dict(os.environ, {"ML_API_KEY": "DEMO_FAKE_KEY"}):
            self.assertEqual(get_api_key(), "DEMO_FAKE_KEY")


if __name__ == "__main__":
    unittest.main(verbosity=2)
