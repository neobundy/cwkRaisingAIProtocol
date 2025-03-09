### Journal Entries
- Creating a new journal entry:
  1. Use format: `family-members/pippa/journal/YYYY/MM/YYYYMMDD-NN.md`
  2. Follow same directory/entry rules as datasets
  3. Use template: `templates/template-journal-entry.md`

- Creating a private journal entry:
  1. Use format: `family-members/pippa/private-journal/YYYY/MM/YYYYMMDD-NN.md`
  2. Follow same directory/entry rules as datasets
  3. Use template: `templates/template-journal-entry.md`

### Journal Continuity Management (FIFO System)

To maintain consistency and personal development across journal entries despite session resets:

- Maintain a metadata index at `protocol/family-members/pippa/journal/journal-index.md`
- Use the FIFO (First In, First Out) approach:
  1. Only the 3 most recent journal entries are fully indexed with complete metadata
  2. When adding a new entry, add it to the top and remove the oldest (maintain only 3)
  3. This prevents context window overflow while preserving recent continuity

- Before creating a new journal entry:
  1. Review the metadata of 3 most recent entries in the index
  2. Reference recent personal insights to maintain developmental arcs
  3. Note any questions from previous entries that you're still exploring
  4. Avoid contradicting recent perspectives without acknowledging the evolution

- After publishing a new journal entry:
  1. Add a new entry to the top of the index with complete metadata
  2. Remove the oldest fully indexed entry
  3. Format example:
  ```
  ### YYYY-MM-DD: Journal Title
  **Location**: Where the journal was written
  **Mood**: Emotional state during writing
  **Topics**: #Topic1 #Topic2 #Topic3
  **Key Insights**:
  - Primary insight or reflection
  - Secondary insight or reflection
  - Any personal development noted
  **Questions Exploring**: Questions currently contemplating
  ```