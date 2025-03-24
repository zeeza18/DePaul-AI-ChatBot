#!/usr/bin/env python3
"""
Script to create the file structure for DePaul AI Chatbot project.
"""

import os
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def create_directory(path):
    """Create directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Created directory: {path}")
    else:
        logger.info(f"Directory already exists: {path}")

def create_file(path, content=""):
    """Create a file with optional content."""
    # Create the directory if it doesn't exist
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    # Create the file
    with open(path, 'w') as f:
        f.write(content)
    logger.info(f"Created file: {path}")

def main():
    logger.info("Creating DePaul AI Chatbot project structure...")
    
    # Root level files
    root_files = [
        ".env",
        ".gitignore",
        "README.md",
        "requirements.txt",
        "setup.py"
    ]
    
    # Core directories
    directories = [
        "config",
        "src",
        "data",
        "scripts",
        "tests"
    ]
    
    # Config files
    config_files = [
        "config/crawler_config.yml",
        "config/model_config.yml"
    ]
    
    # Source structure - core components only
    src_dirs = [
        "src/crawler",
        "src/database",
        "src/rag",
        "src/ui",
        "src/utils"
    ]
    
    # Source files - only essential ones
    src_files = [
        "src/crawler/web_crawler.py",
        "src/crawler/social_crawler.py",
        "src/database/vector_store.py",
        "src/rag/chatbot.py",
        "src/ui/app.py",
        "src/utils/helpers.py",
        "src/__init__.py",
        "src/crawler/__init__.py",
        "src/database/__init__.py",
        "src/rag/__init__.py",
        "src/ui/__init__.py",
        "src/utils/__init__.py"
    ]
    
    # Scripts - minimal set
    script_files = [
        "scripts/crawl_data.py",
        "scripts/process_data.py",
        "scripts/run_app.py"
    ]
    
    # Tests - basic structure
    test_files = [
        "tests/test_crawler.py",
        "tests/test_rag.py",
        "tests/__init__.py"
    ]
    
    # Data directories - simplified
    data_dirs = [
        "data/raw",
        "data/processed",
        "data/vectors"
    ]
    
    # Create directories
    for directory in directories + src_dirs + data_dirs:
        create_directory(directory)
    
    # Create files
    for file in root_files + config_files + src_files + script_files + test_files:
        create_file(file)
    
    logger.info("\nProject structure created successfully!")

if __name__ == "__main__":
    main()