import os

def copy_self_to_directory(target_directory, number_of_copies):
    # Get the absolute path of the current script
    current_script_path = os.path.abspath(__file__)

    # Read the content of the current script
    with open(current_script_path, 'r') as script_file:
        script_content = script_file.read()

    # Create the specified number of copies
    for i in range(number_of_copies):
        copy_path = os.path.join(target_directory, f'copy_{i+1}.py')
        with open(copy_path, 'w') as copy_file:
            copy_file.write(script_content)

if __name__ == "__main__":
    # Define the target directory
    target_directory = "./copies"
    
    # Define the number of copies to create
    number_of_copies = 5

    # Ensure the target directory exists, create if not
    os.makedirs(target_directory, exist_ok=True)
    
    # Call the function to copy the script
    copy_self_to_directory(target_directory, number_of_copies)
