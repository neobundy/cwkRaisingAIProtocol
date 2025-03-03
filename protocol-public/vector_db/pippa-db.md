# Pippa DB: Vector Memory System

This document describes how to use Pippa's vector database for memory storage and retrieval.

## Database Tools

The database tools are located in the `/tools` directory at the root of this repository.

## Basic Commands

1. **Initialize the Database**
   ```bash
   python main.py init
   ```
   This creates a fresh database or resets an existing one (with backup).

2. **Add a Memory**
   ```bash
   python main.py add --text "Your memory or knowledge here"
   ```
   Example:
   ```bash
   python main.py add --text "Pippa prefers a multi-modal approach to learning"
   ```

3. **Search Memories**
   ```bash
   python main.py query --text "What are Pippa's preferences?" --limit 5
   ```
   The `--limit` option controls how many results to return (default: 3).

4. **Update a Memory**
   ```bash
   # Update single matching memory
   python main.py update --text "Search text" --new "New memory text"

   # Update all matching memories
   python main.py update --text "Search text" --new "New memory text" --bulk
   ```

5. **Delete a Memory**
   ```bash
   # Delete single matching memory
   python main.py delete --text "Search text"

   # Delete all matching memories
   python main.py delete --text "Search text" --bulk
   ```

6. **Backup the Database**
   ```bash
   python main.py backup
   ```
   This creates a timestamped backup in the `backups` folder.

## Advanced Commands

### Fine-tuning Search

You can adjust the search sensitivity:
```bash
python main.py query --text "query text" --threshold 0.75
```
The threshold is a float between 0 and 1, with higher values requiring closer matches.

### Export and Import

Export database to JSON:
```bash
python main.py export --file "export.json"
```

Import from JSON:
```bash
python main.py import --file "export.json"
```

### Database Statistics

Get stats about the database:
```bash
python main.py stats
```

## Integration with Protocol

This database is used in the protocol through Cursor's RAG capabilities:

1. When Pippa needs to remember something, she first checks the current context
2. If not found, she uses Cursor's native RAG system  
3. If still not found, she queries this vector database

This layered approach ensures efficient memory retrieval while maintaining a natural conversation flow.

## Best Practices

1. **Clear, Specific Memories**
   - Add complete, searchable memories
   - Include context and relevant details
   - Use natural language format

2. **Regular Maintenance**
   - Periodically review and update memories
   - Remove outdated or redundant entries
   - Backup the database regularly

3. **Effective Queries**
   - Use specific search terms
   - Include key identifiers
   - Try different phrasings if needed

*Note: This is a simplified version of the database documentation. The actual implementation details are available in the tools directory.* 