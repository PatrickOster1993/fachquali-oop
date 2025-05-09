import os

def create_init_files(project_root):
    """
    Check and create missing __init__.py files in the project structure.
    
    Args:
        project_root (str): Path to the project root directory.
    """
    # Directories that should have __init__.py files
    required_dirs = [
        "",  # Project root
        "controller",
        "model",
        "view",
    ]
    
    # Check each directory and create __init__.py if needed
    for dir_path in required_dirs:
        full_path = os.path.join(project_root, dir_path)
        init_path = os.path.join(full_path, "__init__.py")
        
        # Check if directory exists
        if not os.path.exists(full_path):
            print(f"Creating directory: {full_path}")
            os.makedirs(full_path, exist_ok=True)
        
        # Check if __init__.py exists
        if not os.path.exists(init_path):
            print(f"Creating __init__.py in: {full_path}")
            with open(init_path, 'w') as f:
                f.write("# This file makes the directory a Python package\n")
        else:
            print(f"__init__.py already exists in: {full_path}")

if __name__ == "__main__":
    # Replace with your project path
    project_path = "."  # Current directory
    create_init_files(project_path)