#!/bin/bash
# Create a new essay with proper HTML structure
# Usage: ./make_essay.sh "Essay Title Here"

if [ -z "$1" ]; then
    echo "Usage: ./make_essay.sh \"Essay Title Here\""
    exit 1
fi

TITLE="$1"

# Create slug from title (lowercase, remove special chars)
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr ' ' '' | cut -c1-20)

if [ -z "$SLUG" ]; then
    echo "Error: Could not generate valid filename from title"
    exit 1
fi

FILENAME="${SLUG}.html"
FILEPATH="essays/${FILENAME}"

# Check if file exists
if [ -f "$FILEPATH" ]; then
    echo "Error: File $FILENAME already exists!"
    exit 1
fi

# Create the HTML file
cat > "$FILEPATH" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-153791322-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-153791322-1');
  </script>
  <!-- endof Global site tag (gtag.js) - Google Analytics -->
  
  
  
  
  <style>
.accordion {
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
}

.active, .accordion:hover {
  background-color: #000; 
}

/* panel css and js at bottom */

li.sick {
  color: rgb(38, 150, 255);
}

li.audited {
  color: rgb(52,168,83);
}
  </style>
  
  
  <link rel="stylesheet" href="/static/style.css">
  <title>${TITLE} · Tanishq Kumar</title>
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
    
<h3>${TITLE}</h3>
<p>
Write your essay here!
</p>

  </div>
  
  
  <script>
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    
    if (panel.style.maxHeight && panel.style.maxHeight !== "0px") {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}
  </script>
  
</body>
</html>
EOF

echo "✓ Created new essay: essays/${FILENAME}"
echo ""
echo "Next steps:"
echo "1. Edit essays/${FILENAME} and add your content"
echo "2. Add '${FILENAME}' to essays_to_keep list in build.py (around line 238)"
echo "3. Add a link in essays.html under the appropriate year"
echo "4. Run: python3 build.py"

