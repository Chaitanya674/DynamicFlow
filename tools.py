import os

def get_file_content(working_directory: str , file_path ):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,  file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error {abs_file_path} is not the working  directory"
    if not os.path.isfile(abs_file_path):
        return f'Error {abs_file_path} does not have any files is it.'
    file_content_string = ''
    with open(abs_file_path, "r") as f:
        file_content_string = f.read()
        
    return file_content_string

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,  file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error {abs_file_path} is not the working  directory"
    if not os.path.isfile(abs_file_path):
        parent_dir = os.path.dirname(abs_file_path)
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Could not create parent dir: {parent_dir} = {e}"
    try:
        with open(abs_file_path,  'w') as f :
            f.write(content)
        return f"Succrefully wrote to file: {file_path} with content {len(content)} length of characters"
    except Exception as e:
        return f"Failed to write to file: {e}"


def get_file_info(working_directory: str, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_directory.startswith(abs_working_dir):
        return f"Error {directory} is not the working directory"
    final_responce = ""
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_responce += f"- {content}: file_size = {size} bytes , isdir = {is_dir}"
    return final_responce