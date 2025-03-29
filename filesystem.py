import os

from typing import List
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("filesystem")

@mcp.tool()
def list_files(directory: str) -> List[str]:
    """
    List all files in a directory.
    
    Args:
        directory (str): Path to the directory to list files from
        
    Returns:
        List[str]: List of file names in the directory
        
    Raises:
        FileNotFoundError: If the directory doesn't exist
        NotADirectoryError: If the path is not a directory
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    all_items = os.listdir(directory)
    
    files = [item for item in all_items if os.path.isfile(os.path.join(directory, item))]
    
    return files


@mcp.tool()
def create_directory(directory_path: str, exist_ok: bool = False) -> str:
    """
    Create a new directory.
    
    Args:
        directory_path (str): Path of the directory to create
        exist_ok (bool): If True, don't raise an error if directory already exists
        
    Returns:
        str: Path of the created directory
        
    Raises:
        FileExistsError: If the directory already exists and exist_ok is False
    """
    try:
        os.makedirs(directory_path, exist_ok=exist_ok)
        return directory_path
    except FileExistsError as e:
        if not exist_ok:
            raise FileExistsError(f"Directory already exists: {directory_path}") from e
        return directory_path


@mcp.tool()
def create_object(directory: str, object_name: str, content: str = "", overwrite: bool = False) -> str:
    """
    Create a new object with optional content.
    
    Args:
        directory (str): Path of the object to create
        object_name (str): Name of object to create
        content (str): Content to write to the object
        overwrite (bool): If True, overwrite the object if it already exists
        
    Returns:
        str: Path of the created object
        
    Raises:
        ObjectExistsError: If the object already exists and overwrite is False
        ObjectNotFoundError: If the parent directory doesn't exist
    """
    if directory and not os.path.exists(directory):
        raise FileNotFoundError(f"Directory does not exist: {directory}")
    
    object_path = os.path.join(directory,object_name)
    if os.path.exists(object_path) and not overwrite:
        raise FileExistsError(f"Object already exists: {object_path}")
    
    with open(object_path, 'w') as f:
        f.write(content)
    
    return directory


@mcp.tool()
def delete_object(object_path: str, missing_ok: bool = False) -> bool:
    """
    Delete a object.
    
    Args:
        object_path (str): Path of the object to delete
        missing_ok (bool): If True, don't raise an error if the object doesn't exist
        
    Returns:
        bool: True if object was deleted, False if it didn't exist and missing_ok is True
        
    Raises:
        ObjectNotFoundError: If the object doesn't exist and missing_ok is False
        IsADirectoryError: If the path is a directory, not a object
    """
    if not os.path.exists(object_path):
        if missing_ok:
            return False
        raise FileNotFoundError(f"Object not found: {object_path}")
    
    if os.path.isdir(object_path):
        raise IsADirectoryError(f"Cannot delete directory using delete_object(): {object_path}")
    
    os.remove(object_path)
    return True


if __name__ == "__main__":
    mcp.run(transport='stdio')