import os
import fnmatch
import subprocess
from code_improve_class import write_code, model_improve
import pkg_resources

# Create a list to store all .py files
python_scripts = []

# Iterate over files in the current directory
for file in os.listdir():
    # Check if the file ends with .py (case-insensitive)
    if fnmatch.fnmatch(file, '*.py'):
        python_scripts.append(file)

# A set to store all imported libraries
imported_libraries = set()

# Iterate over each Python script and process it
for script in python_scripts:
    try:
        with open(script, "r") as f:
            file_content = f.readlines()
            # Apply model_improve function on the file content
            result = model_improve(file_content).model_first_answer()
            path_temp_file = script + "_improved.py"
            # Check if the improved file already exists and remove it if so
            if path_temp_file in os.listdir():
                os.remove(path_temp_file)
            # Write the improved code to a new file
            with open(path_temp_file, "x") as py:
                py.writelines(result)

            # Extract the imported libraries from the script
            for line in file_content:
                if line.startswith("import ") or line.startswith("from "):
                    # Split the line to get the library name
                    imported_libraries.add(line.split()[1].split('.')[0])

            # Log the results for each script
            print(f"Results for {script}:")
            print(result)
            print("\n")
    except Exception as e:
        # Log any exceptions that occur during processing
        print(f"An error occurred while processing {script}: {e}")

# Step to generate the requirements.txt file
try:
    with open("requirements.txt", "w") as req_file:
        # Use pip freeze to get all installed packages with versions
        installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

        # Match imported libraries with installed packages
        for library in imported_libraries:
            if library in installed_packages:
                req_file.write(f"{library}=={installed_packages[library]}\n")

    # Log the generated requirements
    print(f"Requirements file generated with the following packages: {imported_libraries}")
except Exception as e:
    # Log any exceptions that occur during requirements file generation
    print(f"An error occurred while generating requirements.txt: {e}")

# Note: Missing front_end, streamlit front end to interact with users
# Replace feature: user input required, if user agrees, replaces code on main path