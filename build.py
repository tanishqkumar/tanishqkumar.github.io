#!/usr/bin/env python3
"""
Build script to generate HTML files from Jinja2 templates.
Preserves the existing aesthetic while improving code organization.
"""

import os
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Setup Jinja2 environment
template_dir = Path(__file__).parent / 'templates'
env = Environment(loader=FileSystemLoader(template_dir))

# Base directory
base_dir = Path(__file__).parent

def extract_content_between_tags(html_content, start_tag, end_tag):
    """Extract content between two HTML tags, handling nested tags."""
    start_idx = html_content.find(start_tag)
    if start_idx == -1:
        return ""
    
    start_idx += len(start_tag)
    
    # For div tags, we need to count nested divs
    if start_tag == '<div id="content">':
        depth = 1
        current_idx = start_idx
        
        while depth > 0 and current_idx < len(html_content):
            next_open = html_content.find('<div', current_idx)
            next_close = html_content.find('</div>', current_idx)
            
            if next_close == -1:
                break
            
            if next_open != -1 and next_open < next_close:
                depth += 1
                current_idx = next_open + 4
            else:
                depth -= 1
                if depth == 0:
                    return html_content[start_idx:next_close].strip()
                current_idx = next_close + 6
        
        return ""
    else:
        end_idx = html_content.find(end_tag, start_idx)
        if end_idx == -1:
            return ""
        return html_content[start_idx:end_idx].strip()

def extract_essay_content(essay_path):
    """Extract the main content from an essay HTML file."""
    with open(essay_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<title>(.*?)·', content)
    title = title_match.group(1).strip() if title_match else ""
    
    # Extract the h3 title
    h3_match = re.search(r'<h3>(.*?)</h3>', content)
    essay_title = h3_match.group(1).strip() if h3_match else title
    
    # Extract content between <div id="content"> and </div>
    main_content = extract_content_between_tags(content, '<div id="content">', '</div>')
    
    # Remove the first h3 tag from content since we'll add it via template
    main_content = re.sub(r'^\s*<h3>.*?</h3>\s*', '', main_content, count=1, flags=re.DOTALL)
    
    # Check if MathJax is needed (either explicitly included or LaTeX expressions present)
    include_mathjax = ('MathJax' in content or 
                      '$' in main_content or 
                      '\\(' in main_content or 
                      '\\[' in main_content)
    
    return {
        'title': title,
        'essay_title': essay_title,
        'content': main_content,
        'include_mathjax': include_mathjax
    }

def generate_simple_page(page_name, title, content_html, output_path):
    """Generate a simple page from template."""
    template = env.get_template('simple.html')
    
    html = template.render(
        title=title,
        content=content_html
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated {output_path}")

def generate_essay_page(essay_name, output_path):
    """Generate an essay page from template."""
    essay_path = base_dir / 'essays' / essay_name
    
    if not essay_path.exists():
        print(f"Warning: Essay {essay_name} not found")
        return
    
    essay_data = extract_essay_content(essay_path)
    
    template = env.get_template('essay.html')
    
    # Check if this essay needs accordion styles
    with open(essay_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    include_accordion = 'accordion' in original_content.lower()
    
    # Check if custom styles are needed
    custom_styles = None
    if '<style>' in original_content:
        style_start = original_content.find('<style>') + 7
        style_end = original_content.find('</style>', style_start)
        if style_end > style_start:
            custom_styles = original_content[style_start:style_end].strip()
    
    html = template.render(
        title=essay_data['title'] or essay_data['essay_title'],
        essay_title=essay_data['essay_title'],
        content=essay_data['content'],
        include_mathjax=essay_data['include_mathjax'],
        include_accordion=include_accordion,
        custom_styles=custom_styles
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated {output_path}")

def generate_essays_page():
    """Generate the essays listing page."""
    essays_path = base_dir / 'essays.html'
    with open(essays_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract content
    main_content = extract_content_between_tags(content, '<div id="content">', '</div>')
    
    # Check for custom styles
    custom_styles = None
    if '<style>' in content:
        style_start = content.find('<style>') + 7
        style_end = content.find('</style>', style_start)
        if style_end > style_start:
            custom_styles = content[style_start:style_end].strip()
    
    template = env.get_template('simple.html')
    
    html = template.render(
        title='Writing',
        content=main_content,
        include_accordion=True,
        custom_styles=custom_styles
    )
    
    with open(base_dir / 'essays.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated essays.html")

def generate_papers_page():
    """Generate the research/papers page."""
    papers_path = base_dir / 'papers.html'
    with open(papers_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract content
    main_content = extract_content_between_tags(content, '<div id="content">', '</div>')
    
    # Check for custom styles
    custom_styles = None
    if '<style>' in content:
        style_start = content.find('<style>') + 7
        style_end = content.find('</style>', style_start)
        if style_end > style_start:
            custom_styles = content[style_start:style_end].strip()
    
    template = env.get_template('simple.html')
    
    html = template.render(
        title='Papers',
        content=main_content,
        include_accordion=True,
        custom_styles=custom_styles
    )
    
    with open(base_dir / 'papers.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated papers.html")

def generate_courses_page():
    """Generate the courses page."""
    courses_path = base_dir / 'courses.html'
    with open(courses_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract content
    main_content = extract_content_between_tags(content, '<div id="content">', '</div>')
    
    # Check for custom styles
    custom_styles = None
    if '<style>' in content:
        style_start = content.find('<style>') + 7
        style_end = content.find('</style>', style_start)
        if style_end > style_start:
            custom_styles = content[style_start:style_end].strip()
    
    template = env.get_template('simple.html')
    
    html = template.render(
        title='Courses',
        content=main_content,
        custom_styles=custom_styles
    )
    
    with open(base_dir / 'courses.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated courses.html")

def main():
    """Main build function."""
    print("Starting build process...")
    
    # List of essays to keep (based on essays.html)
    essays_to_keep = [
        'rfr.html',
        'ancients.html',
        'cheap.html',
        'changemind.html',
        'lessons.html',
        'orwell.html',
        'abe.html',
        'befriend.html',
        'tocq.html',
        'bnbs.html',
        'ctm.html',
        'hesitations1.html',
        'hesitations2.html',
        'welcome2f.html',
        'pednprof.html',
        'unl.html',
        'clusters.html',
        'cityscapes.html',
        'warnbusiness.html',
        'gyl2.html',
        'gyl1.html',
    ]
    
    # Generate index page
    index_content = """<p>
        I'm a CS PhD student at Stanford working on the science of deep learning. <br>
        I recently graduated from Harvard College, where I studied math. 
           <p>
        <a href="mailto:tanishq@stanford.edu">Email</a> · 
        <a href="https://github.com/tanishqkumar">GitHub</a> · 
        <a href="https://x.com/tanishqkumar07">Twitter</a> ·
        <a href="https://scholar.google.com/citations?user=6wRuU3cAAAAJ&hl=en&oi=sra">Scholar</a>
      </p>"""
    
    generate_simple_page('index', 'About', index_content, base_dir / 'index.html')
    
    # Generate about page
    about_content = """<p>
        I'm a CS PhD student at Stanford working on the science of deep learning. <br>
        I recently graduated from Harvard College, where I studied math. 

        <br><br>

        My youth was spent in transit. I was fortunate to pass childhood years watching skyscrapers
        emerge from sand dunes in Abu Dhabi, shuffling to and fro between
         cafes and cathedrals while at boarding school in London,
        and learning to think clearly as an undergrad in the snowy town of 
        Cambridge, Massachusetts.
        
        <br><br>
        My research spans language models, scaling laws, and more besides. 
        
        
      </p>

      <p>
        <a href="mailto:tanishq@stanford.edu">Email</a> · 
        <a href="https://github.com/tanishqkumar">GitHub</a> · 
        <a href="https://x.com/tanishqkumar07">Twitter</a> ·
        <a href="https://scholar.google.com/citations?user=G5VwdO0AAAAJ&hl=en">Scholar</a>
      </p>"""
    
    generate_simple_page('about', 'About', about_content, base_dir / 'about.html')
    
    # Generate essays listing page
    generate_essays_page()
    
    # Generate papers page
    generate_papers_page()
    
    # Generate courses page
    generate_courses_page()
    
    # Generate individual essay pages
    for essay_name in essays_to_keep:
        output_path = base_dir / 'essays' / essay_name
        generate_essay_page(essay_name, output_path)
    
    print("\nBuild complete!")
    print(f"Generated {len(essays_to_keep)} essay pages")

if __name__ == '__main__':
    main()

