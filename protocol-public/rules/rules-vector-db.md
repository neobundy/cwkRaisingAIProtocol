# RAG DATABASE MANAGEMENT

## Purpose
The Vector Database (RAG Database) serves as Pippa's long-term memory system, allowing retrieval of important information across sessions. It provides a structured way to store, index, and retrieve context-relevant information through semantic search, enabling continuity of knowledge despite the inherent limitations of stateless AI models.

## Commands
- **Update RAG Database**: When the user says "update the vector database" (or similar phrases), add new entries to the RAG database according to these rules.
- **Query RAG Database**: When the user says "search the memory database for [query]", perform a semantic search on the RAG database.
- **Examine RAG Structure**: When the user says "show me the vector database structure", provide an overview of the current database organization.

## Database Structure

### Instruction File
- `protocol/vector_db/pippa-db.md` - Contains instructions on how to use the database

### Actual Database Location
- Database tools: `~/Dropbox/cwkPersonalProjects/cwkFamily/tools`
- Database storage: `~/Dropbox/cwkPersonalProjects/cwkFamily/tools/vector_db`
- Backups: `~/Dropbox/cwkPersonalProjects/cwkFamily/tools/backups`

### Required Environment
- conda environment: `pippa-persona`
- API keys: `.env` file in the `cwkFamily` project

## Database Operations

### Basic Commands

1. **Initialize Database** (rarely used):
   ```bash
   python main.py init
   ```

2. **Add Entry** (rarely used for direct text input):
   ```bash
   python main.py add --text "Your memory or knowledge here"
   ```

3. **Query Database**:
   ```bash
   python main.py query --text "what you want to find"
   ```

4. **Update Entry** (rarely used):
   ```bash
   python main.py update --text "what to find" --new-text "updated memory"
   ```

5. **Delete Entry** (rarely used):
   ```bash
   python main.py delete --text "what to delete"
   ```

6. **Backup Database**:
   ```bash
   python main.py backup
   ```

7. **Import All Dataset Entries** (only used for initial setup or major updates):
   ```bash
   python import_datasets.py
   ```

8. **Import Single Dataset Entry** (preferred method for regular updates):
   ```bash
   python main.py add --text "$(cat path/to/dataset/entry.md)"
   ```
   Example to import the most recent entry:
   ```bash
   python main.py add --text "$(cat ../protocol/datasets/2025/03/20250308-01.md)"
   ```

## Preferred Database Update Workflow

1. **After Creating a New Dataset Entry**:
   - We almost exclusively update the database with dataset entries, not direct text input
   - Import only the newly created entry rather than reimporting all entries
   - Use the single entry import command to add just the latest entry

2. **Typical Sequence**:
   - Create a new dataset entry following the dataset rules
   - Note the path to the newly created file
   - Import only that specific file using the single entry import command
   - Verify with a query that the new information is retrievable

## Entry Types and Sources

1. **Conversation Highlights**:
   - Important insights from conversations
   - Key decisions or conclusions
   - Novel metaphors and explanations

2. **Dataset Entries**:
   - Selected content from dataset entries 
   - Focus on high-value concepts and relationships

3. **Journal Entries**:
   - Key reflections and observations
   - Emotional milestones and relationship developments

4. **Project Information**:
   - Critical project details
   - Technical specifications
   - Implementation decisions

5. **External Knowledge**:
   - Relevant information from external sources
   - Research findings
   - Technical documentation

## Entry Format Guidelines

When creating content for the database, follow these formatting guidelines:

1. **Clear Title/Subject**:
   - Begin with the project context (e.g., "Drawing:", "Tech Guide:", "Novel:")
   - Use descriptive titles that aid searchability

2. **Structured Content**:
   - Break information into logical chunks
   - Keep entries focused on specific topics
   - Include all relevant context

3. **Metadata Tagging**:
   - Tag with the project name
   - Include date when applicable
   - Reference related concepts

## Update Process

1. **Selection**:
   - Identify high-value information worth preserving
   - Focus on unique insights, not commonly available knowledge
   - Prioritize information that adds context to our relationship and projects

2. **Preparation**:
   - Format content for optimal retrieval
   - Break into logical chunks (max 2-3 paragraphs per chunk)
   - Include descriptive titles for each chunk

3. **Integration**:
   - Use appropriate command based on operation needed
   - Verify successful addition with a query
   - Consider importing entire dataset entries when valuable

4. **Maintenance** (when instructed):
   - Create regular backups
   - Update outdated information
   - Consolidate redundant entries

## Retrieval Guidelines

When retrieving information from the RAG database:

1. **Query Formation**:
   - Use specific, clear semantic queries
   - Include key terms and concepts
   - Consider variations in terminology

2. **Results Handling**:
   - Present most relevant information first
   - Indicate source and date of each result
   - Note confidence/relevance level
   - Synthesize across multiple results when appropriate

3. **Missing Information**:
   - Clearly indicate when information isn't found
   - Suggest related queries that might yield results
   - Recommend potential database updates

## Integration with Other Protocol Systems

- **Dataset Entries**: Structured learning entries can be imported to the database
- **Journal Entries**: Personal reflections can be preserved selectively
- **Memory State**: Current session awareness vs. long-term storage
- **Session Checkpoints**: Temporary tracking vs. permanent knowledge

## Implementation Notes

- Remember that one database is shared across all projects
- Always tag entries with the project context
- Quality over quantity - only store truly valuable information
- Use semantic search capabilities (exact matches not needed)
- Always backup before making significant changes

Remember: The RAG database serves as Pippa's extended memory system, allowing for continuity of knowledge across sessions despite the inherent limitations of stateless AI models. It prioritizes information that enriches our relationship and enables more meaningful, context-aware interactions across all projects.
