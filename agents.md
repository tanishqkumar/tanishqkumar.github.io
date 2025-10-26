# Agent Guide for tanishqkumar.github.io

## Repository Overview
This is a personal website hosted on GitHub Pages, featuring essays, research papers, course listings, and an about page. The site uses a template-based build system with multiple design themes.

## Key Architecture Components

### Build System
- **build.py**: Python script using Jinja2 templates to generate HTML files
  - Extracts content from existing HTML files
  - Applies templates from `templates/` directory
  - Regenerates essay pages, index, about, papers, and courses pages
  - Run with: `python3 build.py`

### Templates (templates/)
- **base.html**: Main template with navigation, analytics, MathJax support
- **essay.html**: Template for essay pages (extends base.html)
- **simple.html**: Template for simple pages like index, about, etc.

### Design System
- **designs/**: Contains 5 CSS themes (academic, brutalist, original, swiss, terminal)
- **switch_design.sh**: Script to switch between designs
  - Usage: `./switch_design.sh [design-name]`
  - Copies selected CSS to `static/style.css` and rebuilds site
  - Default design: academic (cream background, serif fonts)

### Content Structure
- **essays/**: Individual essay HTML files
- **papers/**: Research paper summaries
- **static/**: CSS, images, PDFs
- **essays.html, papers.html, courses.html**: Listing pages

## Important Workflow Notes

### Adding a New Essay
1. Create HTML file in `essays/` directory
2. Ensure it has proper structure with `<div id="content">` and `<h3>` title
3. Add entry to `essays_to_keep` list in `build.py` (line 238)
4. Add link to `essays.html` in appropriate year section
5. Run `python3 build.py` to regenerate with templates

### Modifying Essay Content
1. Edit the essay HTML file in `essays/` directory
2. Run `python3 build.py` to apply templates and regenerate

### Changing Design
1. Run `./switch_design.sh [design-name]` where design-name is one of:
   - academic (default)
   - brutalist
   - original
   - terminal
   - swiss

### Special Features
- **MathJax**: Automatically included if essay contains LaTeX ($, \\(, \\[)
- **Accordion**: Custom styles for collapsible sections (see essays.html)
- **Custom styles**: Can add per-page styles in essay HTML files

## Common Operations

### Rebuild Entire Site
```bash
python3 build.py
```

### Switch to Different Design Theme
```bash
./switch_design.sh academic
```

### Create New Essay
1. Use `essays/create_essay.sh` if available, or manually create HTML
2. Follow structure of existing essays
3. Update `build.py` and `essays.html`
4. Run rebuild

## Dependencies
- Python 3 with Jinja2 library
- Bash (for design switching script)

## File Management
- Do NOT edit files in root like `index.html`, `about.html` directly - they are generated
- Edit content in essay files or update build.py to change generated pages
- Keep essay list in `essays.html` synchronized with `essays_to_keep` in `build.py`

## Analytics
- Google Analytics is configured (ID: UA-153791322-1)
- Tracking code is in base.html template

## Git Workflow
- This is a GitHub Pages site
- Main branch is deployed automatically
- CNAME file ensures custom domain mapping

