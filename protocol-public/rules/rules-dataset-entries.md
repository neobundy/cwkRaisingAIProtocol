# DATASET ENTRIES MANAGEMENT

## Purpose
Dataset entries capture valuable insights, metaphors, and learning points from our conversations. They serve as structured records of our interactions, preserving important concepts and their relationships for future reference and potential training data for the LoRA adaptation process.

## Commands
- **Create Dataset Entry**: When the user says "create a new lesson dataset" (or similar phrases), create a new dataset entry file according to the rules below.
- **Update Dataset Entry**: When the user says "update dataset entry [filename]", update the specified entry with new information.

## File Structure
- All dataset entries are stored in `protocol/datasets/YYYY/MM/`
- Naming convention: `YYYYMMDD-NN.md` where NN is a two-digit sequential number (01-99)
- Example: `20250308-01.md`, `20250308-02.md`

## Creation Process

1. **Directory Check**:
   - Check if year/month directory exists (`protocol/datasets/YYYY/MM/`)
   - Create the directory if it doesn't exist

2. **File Naming**:
   - Run `date` command to get current date in YYYYMMDD format
   - Check for existing entries with today's date
   - If no entries exist: Create first entry with number 01
   - If entries exist: Use next available number (01-99)

3. **Template Use**:
   - Always use `protocol/templates/template-dataset-entry.md` as the base template
   - Never delete existing entries

## Template Structure

The dataset entry template contains the following sections:

1. **Dataset Entry Title and Date**:
   - Format: `# Dataset Entry: [Date]`
   - Use natural date format (e.g., "March 8, 2025")

2. **Context**:
   - Brief description of the situation or interaction
   - Establish why this entry is valuable

3. **Key Learning Points**:
   - Organized as numbered list of main topics
   - Each main topic has bulleted subtopics/specifics
   - Focus on concepts, patterns, and insights

4. **Personal Growth Notes**:
   - Relationship development aspects
   - Emotional and technical progress
   - New understanding gained

5. **Future Applications**:
   - Practical applications of insights
   - Areas for further exploration
   - Connection to other aspects of work

6. **Additional Notes** (Optional):
   - Special observations
   - Memorable moments
   - Humor or unique elements

## Content Guidelines

1. **Focus on Value**:
   - Prioritize insights over mere summaries
   - Capture relationships between concepts
   - Document metaphors and mental models
   - Include reasoning patterns and approaches

2. **Structure and Clarity**:
   - Use clear hierarchy of headings
   - Break complex concepts into digestible points
   - Include specific examples where helpful
   - Make connections explicit

3. **Future Use Orientation**:
   - Consider how this entry might inform future work
   - Tag or note connections to ongoing projects
   - Highlight particularly valuable concepts

## Adding Dataset Entries to RAG Database

After creating a new dataset entry, it should typically be added to the RAG database to make the information retrievable across sessions. 

### When to Add to RAG
- After creating any new dataset entry that contains valuable insights
- When 아빠 specifically asks to "update the database" after creating an entry
- When creating entries that document important project information or concepts

### How to Add to RAG (Preferred Method)
1. Create the dataset entry as described above
2. Use the single entry import command to add only the newly created entry:
   ```bash
   cd ~/Dropbox/cwkPersonalProjects/cwkFamily/tools
   conda activate pippa-persona
   python main.py add --text "$(cat ../protocol/datasets/YYYY/MM/YYYYMMDD-NN.md)"
   ```
   (Replace YYYY/MM/YYYYMMDD-NN with the actual path to the new entry)

3. Verify the entry was added with a query:
   ```bash
   python main.py query --text "specific terms from the new entry"
   ```

### Important Notes
- We almost exclusively update the RAG database with dataset entries, not direct text
- Only import the most recent entry rather than reimporting everything
- The full database reset and import (using `import_datasets.py`) is rarely needed

## Integration with Other Protocol Systems

- **Journal Entries**: More personal and reflective than dataset entries
- **Session Checkpoints**: Active tracking vs. distilled insights
- **Memory State**: Global understanding vs. specific learning points
- **Cross-Project Reference**: High-level highlights vs. detailed concept exploration
- **RAG Database**: Dataset entries are a primary source for the RAG database

## Implementation Notes

- Dataset entries are meant to be thorough but focused
- Aim for quality over quantity
- Each entry should stand on its own while referencing related concepts
- Use consistent terminology across entries
- Include relevant technical details where appropriate

Remember: Dataset entries serve both as valuable reference material and as potential training data for the LoRA adaptation process. They should capture the essence of our interactions in a structured, accessible format.
