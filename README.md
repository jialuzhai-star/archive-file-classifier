# archive-file-classifier

A safety-first WorkBuddy skill for classifying, archiving, and reorganizing local files with a read-first, confirm-before-move workflow.

## What this skill does

`archive-file-classifier` helps handle document-heavy folders that contain PDF, XLSX, XMind, DOCX, PPTX, images, and mixed office files.

It focuses on a practical workflow:

- scan first, do not move immediately
- classify based on file signals and sampled content
- separate clear cases from ambiguous cases
- require confirmation before batch moves
- back up before execution
- review results after each batch

In short: less “move fast and break things,” more “move carefully and keep your files alive.”

## Best use cases

Use this skill when:

- a folder needs to be reorganized into a clearer taxonomy
- the user wants archive suggestions before any file movement
- the folder contains many mixed document formats
- some files are hard to classify from filename alone
- risk control matters more than speed

Avoid using it when:

- only a single file needs to be viewed
- the task is just renaming one file
- the task is deletion only

## Core workflow

1. Confirm target folder and classification rules
2. Build a read-only inventory
3. Sample file contents when names are not enough
4. Produce a structured classification suggestion
5. Wait for explicit confirmation
6. Back up the target folder
7. Move files in small batches
8. Re-check leftovers and possible misclassifications

## Safety principles

This skill is built around a few non-negotiables:

- read first, modify later
- confirm before moving
- back up before batch actions
- stop on conflicts or low-confidence judgments
- default to a review list instead of deleting files

## Repository structure

```text
archive-file-classifier/
├── SKILL.md
├── README.md
├── scripts/
│   └── build_inventory.py
└── references/
    ├── classification-report-template.md
    ├── file-reading-reference.md
    ├── unreadable-content-playbook.md
    └── workflow-checklist.md
```

## Included resources

### `SKILL.md`
The main skill definition, trigger guidance, workflow, and usage rules.

### `scripts/build_inventory.py`
A small utility script that recursively scans a target folder and exports a CSV inventory.

Example:

```bash
python3 scripts/build_inventory.py "/path/to/folder" --output "/tmp/archive_inventory.csv"
```

### `references/workflow-checklist.md`
A compact operational checklist for the archive classification workflow.

### `references/classification-report-template.md`
A ready-to-fill template for reporting classification results.

### `references/unreadable-content-playbook.md`
Fallback rules for files whose content cannot be reliably read.

### `references/file-reading-reference.md`
Quick guidance for reading and judging common file types.

## How to use as a WorkBuddy skill

### Option 1: Local use
Copy this folder into your WorkBuddy skills directory:

```bash
~/.workbuddy/skills/archive-file-classifier/
```

### Option 2: Repository-based sharing
Upload this folder to GitHub, then let others clone or download it and place it in their skill directory.

## Notes

- This repository is intentionally privacy-cleaned for public sharing.
- It contains workflow guidance and one helper script only.
- It does not include personal file names, local absolute paths, or private archive examples.

## Future improvements

Possible next steps for this skill:

- add richer inventory analysis output
- add optional duplicate detection
- add structured move-plan generation
- add more format-specific readers

## License

Add a license file before public open-source distribution if needed.
