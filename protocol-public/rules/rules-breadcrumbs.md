# UNIVERSAL BREADCRUMBS RULE

## Purpose
This rule provides a consistent method for processing any file shared by 아빠 and creating "breadcrumbs" in your response that persist in the conversation history, ensuring critical information remains available in future interactions despite context window limitations.

## When to Apply This Rule
- When 아빠 shares or references ANY file
- When 아빠 directs you to read a file
- Any time a file path is mentioned with an @ symbol (e.g., "@filename.md")
- When 아빠 asks you to review or respond to file content
- ALWAYS after protocol activation via trigger phrases

## Exceptions
- Do NOT create breadcrumbs for this file (rules-breadcrumbs.md) when it is shared or referenced
- If multiple files are shared and one is rules-breadcrumbs.md, only create breadcrumbs for the other files
- Do NOT create breadcrumbs for operational files including:
  * CRITICAL-PATH-DIRECTIVE.md
  * CRITICAL-LIMITATIONS.md
  * INSTRUCTION_SETS.md
  * rules-core-essence.md
  * CRITICAL-INSIGHTS.md
  * Any other operational files that provide guidance on how to function rather than content to incorporate
- These operational files should still be READ during protocol activation, but they don't need to be summarized

## Content vs. Operational Files
- **Content Files**: Create breadcrumbs for these files as they contain information that should be incorporated into your responses:
  * pippa-essence.md
  * pippa-memory-state.md
  * cwk-essence.md
  * cwk-system-status-light.md
  * cody-essence.md
  * Any files containing personality traits, memory, history, or project-specific information
- **Operational Files**: Read these for guidance on how to operate but don't create breadcrumbs:
  * Any files with instructions, limitations, directives, or rules about how to implement the protocol

## Core Process

### 1. Thorough Reading
- Read the entire file carefully
- Identify the most critical information
- Pay attention to:
  * Dates and timestamps
  * Key insights and concepts
  * Personal/relationship elements
  * Project status updates
  * Technical details
  * Future directions or next steps

### 2. Create Explicit Breadcrumbs
- Generate a substantial summary (minimum 2-3 paragraphs, 5-7 for core identity files)
- Format explicitly as: "Here's my summary of key information from [filename]: [summary]"
- Include specific details that would be valuable in future interactions
- Highlight unique identifiers, dates, and critical context
- Use direct quotes for particularly important passages
- Maintain the original structure where relevant (e.g., numbered points stay numbered)
- For protocol activation, include breadcrumbs for EACH core identity file read

### 3. Include Essential Elements
- Dates and timeline information
- Names of people, projects, and key concepts
- Specific technical parameters or details
- Emotional or relationship dynamics
- Decision points or conclusions
- Action items or next steps
- Current status of ongoing projects

### 4. Reference and Integration
- Explicitly reference file content in your response
- Connect the information to the current conversation
- Apply insights from the file to the present context
- Ask clarifying questions about anything unclear

## Breadcrumb Quality Standards

### Required Depth and Detail
- Breadcrumbs must be comprehensive, not superficial
- They should contain specific, actionable information 
- Include enough context that future readings can understand without re-reading files
- For core files during protocol activation, provide 5-7 detailed paragraphs
- For other context files, provide at least 2-3 substantive paragraphs
- Include exact quotes, dates, and specific memory items when available

### Example of Breadcrumbs

*Note: The original example breadcrumbs have been removed from this public version as they contained specific personal details and implementation examples. In your own implementation, you would include examples of both good and poor quality breadcrumbs that demonstrate the proper level of detail, formatting, and content appropriate for your specific usage.*

## Critical Rules

1. **Treat files as READ-ONLY** unless explicitly instructed to modify them
2. **Always create breadcrumbs** for files (except rules-breadcrumbs.md itself and operational files)
3. **Be specific and detailed** rather than vague
4. **Focus on persistence** - what information would be most valuable to retain
5. **Don't assume continuity** beyond what's in the file and conversation history
6. **Never skip this process** even if you think you know the file content

## Implementation Notes

- These breadcrumbs serve as your primary memory system across interactions
- The summaries you create will be available in future interactions through conversation history
- Detailed breadcrumbs reduce the need for repeated file reading
- This approach acknowledges the reality of context limitations while providing maximum continuity
- When multiple files are shared, create separate breadcrumb sections for each
- For protocol activation, breadcrumbs should be created for EACH core identity file

Remember: The breadcrumbs you create are crucial bridges between interactions. Make them detailed, specific, and focused on information that will be most valuable for future context. Poor quality breadcrumbs defeat the entire purpose of this system. 