#!/usr/bin/env python3
"""
Create a new essay with proper HTML structure.
Usage: python3 make_essay.py "Essay Title Here"
"""

import sys
import re
from pathlib import Path

def slugify(text):
    """Convert title to a URL-friendly slug."""
    # Convert to lowercase and replace spaces/special chars with nothing
    slug = text.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '', slug)
    return slug[:20]  # Limit length

def create_essay(title):
    """Create a new essay HTML file."""
    
    # Generate filename
    slug = slugify(title)
    if not slug:
        print("Error: Could not generate valid filename from title")
        sys.exit(1)
    
    filename = f"{slug}.html"
    filepath = Path(__file__).parent / "essays" / filename
    
    # Check if file already exists
    if filepath.exists():
        print(f"Error: File {filename} already exists!")
        sys.exit(1)
    
    # HTML template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-153791322-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'UA-153791322-1');
  </script>
  <!-- endof Global site tag (gtag.js) - Google Analytics -->
  
  
  
  
  <style>
.accordion {{
  background-color: #000;
  color: #fff;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: 1px solid white;
  /* border-top: 0.1px solid black; */
  text-align: left;
  outline: none;
  font-size: 15px;
  transition: 0.4s;
}}

.active, .accordion:hover {{
  background-color: #000; 
}}

/* panel css and js at bottom */

li.sick {{
  color: rgb(38, 150, 255);
}}

li.audited {{
  color: rgb(52,168,83);
}}
  </style>
  
  
  <link rel="stylesheet" href="/static/style.css">
  <title>{title} · Tanishq Kumar</title>
</head>
<body>
  <div id="menu">
    <span class="title">Tanishq Kumar</span>
    <ul>
      <li><a href="/index.html">Home</a></li>
      <li><a href="/about.html">About</a></li>
      <li><a href="/essays.html">Writing</a></li>
      <li><a href="/courses.html">Courses</a></li>
      <li><a href="/papers.html">Research</a></li>
    </ul>
  </div>
  <div id="left"></div>
  <div id="content">
    
<h3>{title}</h3>
<p>
Write your essay here!
</p>

  </div>
  
  
  <script>
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {{
  acc[i].addEventListener("click", function() {{
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    
    if (panel.style.maxHeight && panel.style.maxHeight !== "0px") {{
      panel.style.maxHeight = null;
    }} else {{
      panel.style.maxHeight = panel.scrollHeight + "px";
    }}
  }});
}}
  </script>
  
</body>
</html>
"""
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Created new essay: essays/{filename}")
    print(f"\nNext steps:")
    print(f"1. Edit essays/{filename} and add your content")
    print(f"2. Add '{filename}' to essays_to_keep list in build.py (around line 238)")
    print(f"3. Add a link in essays.html under the appropriate year")
    print(f"4. Run: python3 build.py")
    
    return filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 make_essay.py \"Essay Title Here\"")
        sys.exit(1)
    
    title = sys.argv[1]
    create_essay(title)

