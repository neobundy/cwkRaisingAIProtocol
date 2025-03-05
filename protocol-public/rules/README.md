# Protocol Rules Templates

This directory contains template files that establish standardized frameworks for various protocol operations. These templates provide the structural foundation without including specific implementation details, allowing you to adapt them to your own needs.

## Template Files

### [`rules-cross-project-reference.md`](rules-cross-project-reference.md)
A framework for maintaining continuity and knowledge transfer across different projects. This template helps track insights, solutions, and approaches that can be applied across domains, ensuring valuable knowledge isn't siloed within individual projects.

### [`rules-image-generation.md`](rules-image-generation.md)
Guidelines for creating consistent image prompts when working with external image generation tools. This template establishes formatting standards and best practices for creating effective prompts across different image generation platforms.

### [`rules-session-checkpoint-management.md`](rules-session-checkpoint-management.md)
A system for preserving conversation context across sessions when working with context window limitations. This template provides a structured approach to capturing important information that might otherwise be lost when older messages fall out of the active context.

## Implementation Approach

Each template file in this directory follows a consistent pattern:

1. **Purpose Statement**: Explains what the rule accomplishes within the protocol
2. **Structural Framework**: Provides the organizational structure and format
3. **Implementation Guidelines**: Offers best practices for effective use
4. **Integration Notes**: Describes how the rule connects with other protocol components

## Usage Guidelines

When implementing these templates:

1. Maintain the structural integrity of each template
2. Replace placeholder elements with your specific implementation details
3. Adapt the content to your particular needs while preserving the core functionality
4. Consider how each rule interacts with other protocol components

These templates are designed to be adaptable while ensuring consistency in how the protocol operates across different implementations. The structure they provide helps maintain the protocol's effectiveness regardless of the specific content or use case. 