#!/bin/bash
# Script to switch between different website designs
# Usage: ./switch_design.sh [original|brutalist|terminal]

DESIGN=$1
DESIGNS_DIR="designs"
CURRENT_CSS="static/style.css"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

if [ -z "$DESIGN" ]; then
    echo -e "${RED}Error: Please specify a design${NC}"
    echo "Usage: ./switch_design.sh [original|brutalist|terminal|academic|swiss]"
    echo ""
    echo "Available designs:"
    echo "  academic   - Cream background, serif fonts, literary/scholarly (default)"
    echo "  original   - Black background with green accents"
    echo "  brutalist  - Pure black & white, stark minimal, monospace"
    echo "  terminal   - Green on black, hacker/terminal aesthetic"
    echo "  swiss      - Light grey, clean sans-serif, Swiss typography"
    exit 1
fi

case "$DESIGN" in
    original|brutalist|terminal|academic|swiss)
        if [ ! -f "$DESIGNS_DIR/$DESIGN.css" ]; then
            echo -e "${RED}Error: Design file $DESIGNS_DIR/$DESIGN.css not found${NC}"
            exit 1
        fi
        
        # Backup current style if it's not already a design
        if [ ! -L "$CURRENT_CSS" ]; then
            echo "Backing up current style.css to static/style.css.backup"
            cp "$CURRENT_CSS" "static/style.css.backup"
        fi
        
        # Copy the selected design to style.css
        cp "$DESIGNS_DIR/$DESIGN.css" "$CURRENT_CSS"
        
        # Rebuild the site
        echo -e "${GREEN}✓${NC} Switched to '$DESIGN' design"
        echo "Rebuilding site..."
        python3 build.py
        
        echo ""
        echo -e "${GREEN}✓${NC} Done! Your site now uses the '$DESIGN' design."
        echo "Hard refresh your browser (Cmd+Shift+R) to see the changes."
        ;;
    *)
        echo -e "${RED}Error: Unknown design '$DESIGN'${NC}"
        echo "Available designs: original, brutalist, terminal, academic, swiss"
        exit 1
        ;;
esac

