# Pippa Memory Database Tools

This directory contains tools for managing the vector memory database that enables long-term memory for the Pippa Protocol.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key'
```
Or create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your-api-key
```

## Usage

The main script provides several commands for managing the memory database:

### Initialize Database
```bash
python main.py init
```

### Add Memory
```bash
python main.py add -t "Your memory text here"
```

### Query Memories
```bash
python main.py query -t "Search text" -l 5  # -l sets limit (default: 3)
```

### Update Memory
```bash
# Update single matching memory
python main.py update -t "Search text" -n "New memory text"

# Update all matching memories
python main.py update -t "Search text" -n "New memory text" -b
```

### Delete Memory
```bash
# Delete single matching memory
python main.py delete -t "Search text"

# Delete all matching memories
python main.py delete -t "Search text" -b
```

### Backup Database
```bash
python main.py backup
```

### Run Tests
```bash
python main.py --test
```

## Directory Structure

- `pippa_db.py`: Core database functionality for vector storage
- `main.py`: Command-line interface for database operations
- `import_datasets.py`: Utility to import dataset files into the database
- `vector_db_setup.py`: Legacy setup script
- `tests/`: Test suite with unit tests
- `vector_db/`: Database storage (created on initialization)
- `backups/`: Backup storage (created when running backup command)

Note: The `vector_db/` directory will be empty in the repository but will be populated when you initialize the database. 