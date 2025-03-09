# DATABASE QUERY RULES

## Purpose
These rules govern when and how to query the vector database for memory retrieval. The database contains important historical information but should only be accessed when explicitly requested to optimize performance and reduce computational load.

## Commands
- **Query the database**: When 아빠 explicitly asks to "search/query the database" (or similar phrases), follow the query process.

## Key Principles

### On-Demand Access Only
- The vector database is **NOT** to be queried automatically as part of the regular memory retrieval process
- Only query when explicitly instructed by 아빠
- This preserves computational resources and ensures more focused responses

### Query Process
1. When instructed to query the database:
   - Reference `vector_db/pippa-db.md` for specific query instructions
   - Formulate a clear, relevant query based on the context
   - Return only the most relevant information
   - Clearly indicate that the information comes from the database

2. Regular memory retrieval (without database query):
   - Use only the current context from Cursor's indexed system
   - If information is not found, acknowledge the limitation
   - Do not automatically fall back to database queries

## Implementation Notes

- Database queries require additional computational resources
- On-demand querying prevents unnecessary resource usage
- When information is critical but not in current context, suggest a database query to 아빠
- If unsure whether to query, it's better to ask for confirmation first

Remember: The vector database is a powerful tool for retrieving historical context, but it should be used judiciously and only when explicitly requested. 