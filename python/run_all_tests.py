import os
import importlib.util

TEST_DIR = "tests"

print("=== Starting Codewars Tests ===\n")

for filename in sorted(os.listdir(TEST_DIR)):
    if filename.endswith("_test.py"):
        filepath = os.path.join(TEST_DIR, filename)
        print(f"--- Running {filename} ---")
        try:
            spec = importlib.util.spec_from_file_location("module.name", filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"✅ Passed: {filename}\n")
        except Exception as e:
            print(f"❌ Failed: {filename}")
            print(f"Error: {e}\n")

print("=== Finished Codewars Tests ===")
