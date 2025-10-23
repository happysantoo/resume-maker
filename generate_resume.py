#!/usr/bin/env python3
"""
Resume PDF Generator for Santhosh Kuppusamy
Creates a professionally formatted 2-page resume PDF from text file
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
import re

def parse_resume_txt(filepath='santhosh_resume.txt'):
    """Parse the resume text file and extract structured data"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    resume_data = {
        'name': '',
        'title': '',
        'contact': '',
        'location': '',
        'summary': [],
        'skills': {},
        'experience': [],
        'education': []
    }
    
    lines = content.split('\n')
    current_section = None
    current_job = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Parse name (first non-empty line)
        if not resume_data['name'] and line:
            resume_data['name'] = line
            continue
        
        # Parse title (second line with |)
        if not resume_data['title'] and '|' in line and 'Principal' in line:
            resume_data['title'] = line
            continue
        
        # Parse contact info
        if 'Phone:' in line or 'Email:' in line:
            resume_data['contact'] = line
            continue
        
        # Parse location
        if 'Location:' in line:
            resume_data['location'] = line.replace('Location:', '').strip()
            continue
        
        # Identify sections
        if line == 'PROFESSIONAL SUMMARY':
            current_section = 'summary'
            continue
        elif line == 'TECHNICAL SKILLS':
            current_section = 'skills'
            continue
        elif line == 'PROFESSIONAL EXPERIENCE':
            current_section = 'experience'
            continue
        elif line == 'EDUCATION':
            current_section = 'education'
            continue
        
        # Parse summary
        if current_section == 'summary' and line and line != 'PROFESSIONAL SUMMARY':
            if line.startswith('Deep Expertise:') or line.startswith('Modern Stack:') or line.startswith('Leadership and Governance:'):
                resume_data['summary'].append(line)
            elif not any(x in line for x in ['TECHNICAL SKILLS', 'Cloud and DevOps']):
                if resume_data['summary'] and not resume_data['summary'][-1].endswith('.'):
                    resume_data['summary'][-1] += ' ' + line
                elif line:
                    resume_data['summary'].append(line)
        
        # Parse skills
        elif current_section == 'skills' and line:
            if not any(x in line for x in ['PROFESSIONAL EXPERIENCE', 'JPMORGAN']):
                # Check if this line is already a skill value (contains commas or is descriptive)
                if ',' in line or any(keyword in line.lower() for keyword in ['kafka', 'kubernetes', 'postgresql', 'payment']):
                    continue  # Skip lines that are skill values, not categories
                # Check if it's a category or skill list
                if i + 1 < len(lines) and lines[i + 1].strip() and not lines[i + 1].strip().isupper():
                    category = line
                    skills = lines[i + 1].strip()
                    if category and skills and category not in resume_data['skills']:
                        resume_data['skills'][category] = skills
        
        # Parse experience
        elif current_section == 'experience':
            # Check for company name - but not if it's part of an achievement text
            is_company_line = (line.isupper() or 'CHASE' in line) or \
                            (('FIS' in line or 'Fidelity' in line) and line.startswith('FIS'))
            
            if line and is_company_line:
                if current_job:
                    resume_data['experience'].append(current_job)
                current_job = {
                    'company': line,
                    'title': '',
                    'location': '',
                    'dates': '',
                    'achievements': []
                }
            elif current_job:
                if not current_job['title'] and ('Vice President' in line or 'Senior IT Architect' in line or 'Engineer/Architect' in line):
                    current_job['title'] = line
                elif not current_job['location'] and ('Florida' in line or 'Wisconsin' in line) and 'Targeting' not in line:
                    current_job['location'] = line
                elif not current_job['dates'] and ('to' in line.lower() or '–' in line) and any(month in line for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']):
                    current_job['dates'] = line
                elif line and not line.isupper() and line != 'EDUCATION':
                    # Check if it's a new achievement (contains a colon in the first part)
                    if ':' in line[:50]:  # Colon in first 50 chars indicates achievement title
                        current_job['achievements'].append(line)
                    elif current_job['achievements']:
                        # Continuation of previous achievement
                        current_job['achievements'][-1] += ' ' + line
        
        # Parse education
        elif current_section == 'education' and line:
            if 'Master' in line or 'Bachelor' in line:
                resume_data['education'].append({'degree': line, 'details': ''})
            elif resume_data['education'] and not resume_data['education'][-1]['details']:
                resume_data['education'][-1]['details'] = line
    
    # Add last job if exists
    if current_job:
        resume_data['experience'].append(current_job)
    
    # Debug output
    print(f"   ✓ Parsed content: {len(resume_data['summary'])} summary items, {len(resume_data['skills'])} skill categories, {len(resume_data['experience'])} jobs")
    
    return resume_data

def create_resume_pdf(filename='Santhosh_Kuppusamy_Resume.pdf', target_location='San Francisco Bay Area', source_file='santhosh_resume.txt', internal_format=False):
    """Create a formatted resume PDF from text file
    
    Args:
        filename: Output PDF filename
        target_location: Target job location (e.g., 'San Francisco Bay Area', 'New York City')
        source_file: Source text file containing resume content
        internal_format: If True, modifies title for internal use
    """
    
    # Parse the resume text file
    print(f"📖 Reading resume content from {source_file}...")
    resume_data = parse_resume_txt(source_file)
    
    # For internal format, override JPMC experience with internal content
    if internal_format:
        internal_jpmc_achievements = [
            "Cloud-Native Funds Control Platform: Provided technical leadership for a cloud-neutral, multi-region resilient funds control platform, targeting reduced inter-region latency and establishing a new 99.99% availability standard.",
            "Mainframe Modernization Initiative: Led the strategic modernization of mainframe-hosted legacy payment systems to modern cloud-native architecture. Architected and executed the incremental migration of COBOL-based batch processing systems to containerized Spring Boot microservices on AWS, enabling real-time transaction capabilities. Implemented dual-run validation strategies to ensure zero data loss during the transition.",
            "Legacy System Modernization: Drove the technical roadmap for core legacy system migration, orchestrating the transition from monolith to microservices, enabling faster feature release cycles and reducing technical debt.",
            "FinOps and Automation: Championed Infrastructure as Code (IaC) best practices (Terraform/CloudFormation) and FinOps principles, optimizing cloud resource consumption to achieve significant reduction in infrastructure costs.",
            "Enterprise Security Governance: Drove the adoption of standardized security frameworks using IDAnywhere across 15+ applications, connecting to various applications and backends (databases/messaging systems).",
            "AMPS/Graphite Foundation Activities: Led the Banking AMPS team infrastructure, enabling enhanced security and reconciliation mechanisms supporting the FTPS stack integration for multiple CIB payment systems.",
            "CCMP/FTPS: Led the Reference Data team and Invoice/Payments Capture team from architecture to implementation. This represents one of the earliest microservices applications targeted for internal cloud deployment.",
            "Observability: Integrated enterprise observability solutions using OpenTelemetry, Prometheus, and Grafana to reduce mean-time-to-resolution (MTTR) and minimize production incidents.",
            "Generative AI: Developed AI-powered Java static analyzer used firm-wide for detecting concurrency issues and performance anti-patterns with async batch processing and intelligent caching."
        ]
        
        # Replace JPMC achievements in resume data
        for job in resume_data['experience']:
            if 'JPMORGAN' in job['company'] or 'CHASE' in job['company']:
                job['achievements'] = internal_jpmc_achievements
                break
    
    # Create the PDF document
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=0.35*inch,
        rightMargin=0.35*inch,
        topMargin=0.35*inch,
        bottomMargin=0.35*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Header style (name)
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Heading1'],
        fontSize=26,
        textColor=HexColor('#003366'),
        alignment=TA_CENTER,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style (title)
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#666666'),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    
    # Contact style
    contact_style = ParagraphStyle(
        'CustomContact',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#333333'),
        alignment=TA_CENTER,
        spaceAfter=6,
        fontName='Helvetica'
    )
    
    # Section heading style
    section_style = ParagraphStyle(
        'CustomSection',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=HexColor('#0066CC'),
        spaceAfter=4,
        spaceBefore=8,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=HexColor('#0066CC'),
        borderPadding=2,
        borderRadius=None
    )
    
    # Body text style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#333333'),
        spaceAfter=1,
        leading=11
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#333333'),
        leftIndent=20,
        spaceAfter=1,
        leading=11
    )
    
    # Job title style
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#003366'),
        fontName='Helvetica-Bold',
        spaceAfter=1
    )
    
    # Job info style
    job_info_style = ParagraphStyle(
        'JobInfo',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#666666'),
        spaceAfter=1,
        fontName='Helvetica-Oblique'
    )
    
    # ===== PAGE 1: Header, Summary, and Technical Skills =====
    
    # Header
    story.append(Paragraph(resume_data['name'], header_style))
    
    # Modify title for internal format
    title_text = resume_data['title']
    if internal_format:
        title_text = title_text.replace('Principal/Lead Software Engineer', 'Senior Lead Software Engineer')
        title_text = title_text.replace(' | VP of Engineering | Cloud Architect', '')
        title_text = title_text.replace(' | VP of Engineering', '')
        title_text = title_text.replace(' | Cloud Architect', '')
    
    story.append(Paragraph(title_text, subtitle_style))
    
    # Extract contact info and update location
    contact_line = resume_data['contact'].replace('Phone:', '').replace('Email:', '')
    contact_parts = [part.strip() for part in contact_line.split('|')]
    if len(contact_parts) >= 2:
        if target_location == 'No Location Preference':
            contact_info = f'{contact_parts[0]} | {contact_parts[1]} | Tampa, Florida Area'
        else:
            contact_info = f'{contact_parts[0]} | {contact_parts[1]} | {target_location} (Targeting Relocation)'
    else:
        if target_location == 'No Location Preference':
            contact_info = f'{contact_line} | Tampa, Florida Area'
        else:
            contact_info = f'{contact_line} | {target_location} (Targeting Relocation)'
    
    story.append(Paragraph(contact_info, contact_style))
    
    # Professional Summary
    story.append(Paragraph('<b>PROFESSIONAL SUMMARY</b>', section_style))
    
    for summary_para in resume_data['summary']:
        story.append(Paragraph(summary_para, body_style))
    
    # Technical Skills
    story.append(Paragraph('<b>TECHNICAL SKILLS</b>', section_style))
    
    for category, skills_list in resume_data['skills'].items():
        story.append(Paragraph(f'• <b>{category}</b> {skills_list}', bullet_style))
    
    # Professional Experience (Start on Page 1)
    story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE</b>', section_style))
    
    # Add all jobs from parsed data
    page_break_added = False
    for idx, job in enumerate(resume_data['experience']):
        # Add page break after first job (JPMC) to start page 2
        if idx == 1 and not page_break_added:
            story.append(PageBreak())
            story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE (Continued)</b>', section_style))
            page_break_added = True
        elif idx > 1:
            story.append(Spacer(1, 0.02*inch))
        
        # Company name
        story.append(Paragraph(f'<b>{job["company"]}</b>', job_title_style))
        
        # Job title
        if job['title']:
            story.append(Paragraph(f'{job["title"]}', job_info_style))
        
        # Location and dates on one line - customize for JPMC
        if 'JPMORGAN' in job['company'] or 'CHASE' in job['company']:
            if target_location == 'No Location Preference':
                location_msg = 'Tampa, Florida Area'
            else:
                location_msg = f'Tampa, Florida Area (Targeting {target_location} Relocation)'
        else:
            location_msg = job['location']
        
        # Combine dates and location on one line (dates first)
        dates_location_line = []
        if job['dates']:
            dates_location_line.append(job['dates'])
        if location_msg:
            dates_location_line.append(location_msg)
        
        if dates_location_line:
            story.append(Paragraph(' | '.join(dates_location_line), job_info_style))
        
        # Achievements
        for achievement in job['achievements']:
            story.append(Paragraph(f'• {achievement}', bullet_style))
    
    # Education
    story.append(Paragraph('<b>EDUCATION</b>', section_style))
    
    for idx, edu in enumerate(resume_data['education']):
        story.append(Paragraph(f'<b>{edu["degree"]}</b>', job_title_style))
        if edu['details']:
            story.append(Paragraph(edu['details'], job_info_style))
        if idx < len(resume_data['education']) - 1:
            story.append(Spacer(1, 0.01*inch))
    
    # Build the PDF
    doc.build(story)
    print(f"✅ Resume PDF created successfully: {filename}")

if __name__ == '__main__':
    # Generate San Francisco Bay Area version
    print("\n📄 Generating San Francisco Bay Area resume...")
    create_resume_pdf(
        filename='Santhosh_Kuppusamy_Resume_SF_Bay_Area.pdf',
        target_location='San Francisco Bay Area'
    )
    
    # Generate New York City version
    print("\n📄 Generating New York City resume...")
    create_resume_pdf(
        filename='Santhosh_Kuppusamy_Resume_NYC.pdf',
        target_location='New York City'
    )
    
    # Generate No Location Preference version
    print("\n📄 Generating No Location Preference resume...")
    create_resume_pdf(
        filename='Santhosh_Kuppusamy_Resume_General.pdf',
        target_location='No Location Preference'
    )
    
    # Generate Internal Format version
    print("\n📄 Generating Internal Format resume...")
    create_resume_pdf(
        filename='Santhosh_Kuppusamy_Resume_Internal.pdf',
        target_location='No Location Preference',
        internal_format=True
    )
    
    print("\n✨ All four resume versions have been generated successfully!")
