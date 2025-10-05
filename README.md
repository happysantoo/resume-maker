# Resume Maker Documentation

## Overview

This resume generation system converts plain text resume content into a professionally formatted 2-page PDF using Python and the ReportLab library.

## Files

- **`santhosh_resume.txt`** - Source text file containing the unformatted resume content
- **`generate_resume.py`** - Python script that generates the formatted PDF
- **`Santhosh_Kuppusamy_Resume.pdf`** - Generated output PDF (2 pages)

## Prerequisites

### System Requirements
- Python 3.x installed on your system
- pip (Python package manager)

### Required Python Package
```bash
pip install reportlab
```

Or if using Python 3 specifically:
```bash
pip3 install reportlab
```

## Setup Instructions

1. **Install Python** (if not already installed)
   - macOS: Python 3 is typically pre-installed. Verify with `python3 --version`
   - Linux: `sudo apt-get install python3` (Ubuntu/Debian) or use your distribution's package manager
   - Windows: Download from [python.org](https://www.python.org/downloads/)

2. **Install ReportLab Library**
   ```bash
   pip3 install reportlab
   ```

3. **Verify Installation**
   ```bash
   python3 -c "import reportlab; print('ReportLab installed successfully')"
   ```

## How to Generate the Resume

### Basic Usage

Navigate to the project directory and run:

```bash
python3 generate_resume.py
```

This will generate `Santhosh_Kuppusamy_Resume.pdf` in the same directory.

### Verify the Output

Check that the PDF was created and is 2 pages:

```bash
file Santhosh_Kuppusamy_Resume.pdf
```

Expected output:
```
Santhosh_Kuppusamy_Resume.pdf: PDF document, version 1.4, 2 pages
```

## Design Specifications

### Page Layout
- **Page Size**: US Letter (8.5" × 11")
- **Margins**: 0.35 inches on all sides (top, bottom, left, right)
- **Page Count**: Exactly 2 pages
- **Color Scheme**: Blue accent (#0066CC, #003366) with professional grays

### Typography

| Element | Font | Size | Color |
|---------|------|------|-------|
| Name | Helvetica-Bold | 30pt | #003366 (Dark Blue) |
| Title | Helvetica | 13pt | #666666 (Gray) |
| Contact Info | Helvetica | 11pt | #333333 (Dark Gray) |
| Section Headers | Helvetica-Bold | 15pt | #0066CC (Blue) |
| Body Text | Helvetica | 11pt | #333333 (Dark Gray) |
| Bullet Points | Helvetica | 11pt | #333333 (Dark Gray) |
| Job Titles | Helvetica-Bold | 13pt | #003366 (Dark Blue) |
| Job Info | Helvetica-Oblique | 11pt | #666666 (Gray) |

### Spacing
- **After Name**: 12pt
- **After Title**: 6pt
- **After Contact**: 6pt
- **Before Section Headers**: 14pt
- **After Section Headers**: 8pt
- **Between Body Text**: 2pt
- **Line Height (Leading)**: 12pt for body text

## Content Structure

### Page 1
1. **Header**
   - Name (centered)
   - Professional title (centered)
   - Contact information (centered)

2. **Professional Summary**
   - Brief overview highlighting years of experience
   - Key expertise areas
   - Core competencies

3. **Technical Skills**
   - Organized into 7 categories:
     - Cloud and DevOps
     - Architecture
     - Modernization and Migration
     - Observability
     - Data and Caching
     - Domain
     - Languages

### Page 2
4. **Professional Experience**
   - JPMorgan Chase & Co. (8 years, 2 roles)
   - FIS (Fiserv) roles (2 positions)
   - Each role includes:
     - Job title
     - Company name and dates
     - Key achievements (3-5 bullet points)

5. **Education**
   - Master's degree
   - Bachelor's degree

## Customization Guide

### Modifying Content

To update the resume content, edit the `generate_resume.py` file directly. The content is embedded in the Python script using ReportLab's Paragraph objects.

Key sections to modify:
- Lines 123-132: Header (name, title, contact)
- Lines 135-163: Professional Summary
- Lines 166-180: Technical Skills
- Lines 183-285: Professional Experience
- Lines 287-300: Education

### Adjusting Fonts

To change font sizes, modify the `ParagraphStyle` definitions (lines 32-116):

```python
# Example: Increase section header size
section_style = ParagraphStyle(
    'CustomSection',
    fontSize=15,  # Change this value
    ...
)
```

### Changing Colors

Update the `HexColor` values in the style definitions:

```python
# Example: Change section header color
textColor=HexColor('#0066CC')  # Replace with your hex color
```

### Adjusting Spacing

Modify the `spaceAfter` and `spaceBefore` values in style definitions:

```python
spaceAfter=8,      # Space after element
spaceBefore=14,    # Space before element
```

### Changing Margins

Edit the `SimpleDocTemplate` parameters (lines 17-24):

```python
leftMargin=0.35*inch,    # Adjust margin values
rightMargin=0.35*inch,
topMargin=0.35*inch,
bottomMargin=0.35*inch
```

## Troubleshooting

### Issue: "Module 'reportlab' not found"
**Solution**: Install ReportLab using `pip3 install reportlab`

### Issue: PDF exceeds 2 pages
**Solutions**:
- Reduce font sizes slightly (by 0.5-1pt)
- Decrease line spacing (leading) in body_style and bullet_style
- Reduce margins (minimum recommended: 0.3 inch)
- Minimize `spaceAfter` and `spaceBefore` values

### Issue: PDF is less than 2 pages
**Solutions**:
- Increase font sizes
- Increase line spacing (leading)
- Add more whitespace between sections

### Issue: Text overflowing or not fitting properly
**Solutions**:
- Check for long unbreakable strings (URLs, email addresses)
- Ensure proper text wrapping with ReportLab's Paragraph class
- Verify margin settings aren't too restrictive

## Best Practices

1. **Always test after changes**: Run the script and verify page count after each modification
2. **Use version control**: Keep backup copies of working configurations
3. **Balance readability and space**: Prioritize readability over cramming content
4. **Consistent spacing**: Maintain consistent spacing patterns throughout
5. **Professional colors**: Stick to professional color schemes (blues, grays)
6. **Font hierarchy**: Maintain clear visual hierarchy with font sizes and weights

## Advanced Features

### Adding Page Breaks

Insert a page break where needed:
```python
from reportlab.platypus import PageBreak
story.append(PageBreak())
```

### Creating Spacers

Add custom vertical spacing:
```python
from reportlab.platypus import Spacer
from reportlab.lib.units import inch
story.append(Spacer(1, 0.1*inch))  # 0.1 inch vertical space
```

### Formatting Text

Use HTML-like tags in Paragraph content:
```python
Paragraph('<b>Bold text</b> and <i>italic text</i>', style)
```

### Bullet Points

Add bullet points using unicode character:
```python
Paragraph('• Bullet point text here', bullet_style)
```

## Output Verification

After generating the PDF, verify:

1. **Page Count**: Should be exactly 2 pages
   ```bash
   file Santhosh_Kuppusamy_Resume.pdf
   ```

2. **File Size**: Should be around 7-10 KB (indicates proper compression)
   ```bash
   ls -lh Santhosh_Kuppusamy_Resume.pdf
   ```

3. **Visual Inspection**: Open the PDF and check:
   - All text is readable
   - No text overflow
   - Proper spacing and alignment
   - Colors render correctly
   - No broken formatting

## Maintenance

### Regular Updates
- Update content directly in `generate_resume.py`
- Test after each content change
- Verify 2-page constraint is maintained

### Version History
Keep track of major changes to the resume by creating dated copies:
```bash
cp Santhosh_Kuppusamy_Resume.pdf Santhosh_Kuppusamy_Resume_2025-10-05.pdf
```

## Support and Resources

### ReportLab Documentation
- Official Docs: [https://www.reportlab.com/documentation/](https://www.reportlab.com/documentation/)
- User Guide: [https://www.reportlab.com/docs/reportlab-userguide.pdf](https://www.reportlab.com/docs/reportlab-userguide.pdf)

### Python Resources
- Python Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)
- pip Documentation: [https://pip.pypa.io/](https://pip.pypa.io/)

## License

This resume generation script is for personal use. ReportLab library is subject to its own license terms.

---

**Last Updated**: October 5, 2025  
**Script Version**: 1.0  
**Python Version**: 3.x  
**ReportLab Version**: 3.x or higher
