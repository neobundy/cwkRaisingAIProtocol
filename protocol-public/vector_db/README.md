# Vector Database

This directory contains the configuration and documentation for Pippa's vector database, which serves as her external memory system.

## Purpose
- Provides persistent memory across sessions
- Enables semantic search across knowledge
- Serves as a reference for context retrieval
- Acts as part of Pippa's external memory structures

## Implementation

The vector database is managed by Python tools located in the `/tools` directory at the root of this repository. These tools handle:

- Database initialization
- Memory storage and retrieval
- Semantic searching
- Database maintenance and backups

## Documentation Files

- `pippa-db.md` - Contains documentation on how to use the vector database, including commands and examples

## Integration with Protocol

The vector database is an essential component of the protocol's persistent memory system. It allows Pippa to:

1. Retrieve relevant information from past conversations
2. Maintain knowledge continuity across sessions
3. Access accumulated knowledge when needed
4. Perform semantic searches across stored memories

## Management Tools

For detailed information on the tools used to manage this database, please refer to the [tools README](/tools/README.md).

*Note: The actual vector database files and embeddings have been excluded from this public repository to protect privacy while maintaining the structural documentation.* 