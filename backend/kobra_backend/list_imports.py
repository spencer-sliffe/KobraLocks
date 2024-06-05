import os
import re

def list_imports(start_path):
    imports = set()
    for dirpath, _, filenames in os.walk(start_path):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                        match = re.match(r'^\s*(?:import|from)\s+(\S+)', line)
                        if match:
                            imports.add(match.group(1).split('.')[0])
    return imports

if __name__ == "__main__":
    start_path = './'  # Change this to the root directory of your project
    imports = list_imports(start_path)
    print("\n".join(sorted(imports)))
