#!/usr/bin/env python3
"""
Resume PDF Generator for Santhosh Kuppusamy
Creates a professionally formatted 2-page resume PDF
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor

def create_resume_pdf(filename='Santhosh_Kuppusamy_Resume.pdf'):
    """Create a formatted resume PDF"""
    
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
        fontSize=30,
        textColor=HexColor('#003366'),
        alignment=TA_CENTER,
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style (title)
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=13,
        textColor=HexColor('#666666'),
        alignment=TA_CENTER,
        spaceAfter=6
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
        fontSize=15,
        textColor=HexColor('#0066CC'),
        spaceAfter=8,
        spaceBefore=14,
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
        fontSize=11,
        textColor=HexColor('#333333'),
        spaceAfter=2,
        leading=12
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#333333'),
        leftIndent=20,
        spaceAfter=2,
        leading=12
    )
    
    # Job title style
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=13,
        textColor=HexColor('#003366'),
        fontName='Helvetica-Bold',
        spaceAfter=2
    )
    
    # Job info style
    job_info_style = ParagraphStyle(
        'JobInfo',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#666666'),
        spaceAfter=2,
        fontName='Helvetica-Oblique'
    )
    
    # ===== PAGE 1: Header, Summary, and Technical Skills =====
    
    # Header
    story.append(Paragraph('SANTHOSH KUPPUSAMY', header_style))
    story.append(Paragraph('Principal/Lead Software Engineer (Fintech/Payments) | VP of Engineering | Cloud Architect', subtitle_style))
    story.append(Paragraph(
        '(727) 512-2116 | Santhosh.Kuppuswamy@gmail.com | San Francisco Bay Area (Targeting Relocation)',
        contact_style
    ))
    
    # Professional Summary
    story.append(Paragraph('<b>PROFESSIONAL SUMMARY</b>', section_style))
    
    summary_text = """
    Highly adaptive and innovative Principal/VP-level Engineer with <b>20+ years</b> of progressive 
    experience in the <b>Electronic Payments Industry</b>, specializing in <b>Fraud Detection and Prevention</b>. 
    Proven technical leader driving multi-year modernization and scale initiatives for mission-critical 
    financial platforms.
    """
    story.append(Paragraph(summary_text, body_style))
    
    story.append(Paragraph(
        '<b>Deep Expertise:</b> Designing and scaling multi-threaded, distributed applications, '
        'transitioning monolithic systems to modern cloud-neutral, microservice-based architectures.',
        body_style
    ))
    
    story.append(Paragraph(
        '<b>Modern Stack:</b> Hands-on experience with high-throughput stream processing using '
        'Apache Kafka and Apache Flink to build highly available, low-latency, and resilient systems.',
        body_style
    ))
    
    story.append(Paragraph(
        '<b>Leadership and Governance:</b> Expert in defining technical roadmaps, governance, FinOps, '
        'and operational excellence for platforms handling billions in transactions across hybrid cloud '
        '(AWS) environments.',
        body_style
    ))
    
    # Technical Skills
    story.append(Paragraph('<b>TECHNICAL SKILLS</b>', section_style))
    
    skills = [
        ('<b>Cloud and DevOps:</b>', 'Kubernetes, AWS, Docker, FinOps, Terraform, CloudFormation, Jenkins, Git'),
        ('<b>Architecture:</b>', 'Microservices, Apache Kafka, Distributed Systems, RESTful APIs, Multi-Threading, Spring Boot'),
        ('<b>Modernization and Migration:</b>', 'Mainframe-to-Cloud Migration, Legacy System Modernization, Application Re-platforming, Strangler Fig Pattern'),
        ('<b>Observability:</b>', 'OpenTelemetry, Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana), Splunk'),
        ('<b>Data and Caching:</b>', 'PostgreSQL, Cassandra, CockroachDB, Redis, Gemfire, Hazelcast'),
        ('<b>Domain:</b>', 'Payment Processing, Fraud Detection and Prevention, Funds Control, ISO 8583/20022'),
        ('<b>Languages:</b>', 'Java, Kotlin, Groovy, SQL')
    ]
    
    for category, items in skills:
        story.append(Paragraph(f'• {category} {items}', bullet_style))
    
    # Professional Experience (Start on Page 1)
    story.append(Spacer(1, 0.04*inch))
    story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE</b>', section_style))
    story.append(Spacer(1, 0.01*inch))
    
    # JPMorgan Chase
    story.append(Paragraph('<b>JPMORGAN CHASE AND CO.</b>', job_title_style))
    story.append(Paragraph(
        'Vice President of Software Engineering | November 2017 – Present (8 years)',
        job_info_style
    ))
    story.append(Paragraph(
        'Tampa/St. Petersburg, Florida Area (Targeting Bay Area Relocation)',
        job_info_style
    ))
    
    jpmc_achievements = [
        '<b>Cloud-Native Funds Control Platform:</b> Provided Principal architectural leadership for a '
        'cloud-neutral, multi-region resilient funds control platform, resulting in <b>30% reduced inter-region '
        'latency</b> and establishing a new <b>99.99% availability</b> standard.',
        
        '<b>Mainframe Modernization Initiative:</b> Led the strategic modernization of mainframe-hosted legacy '
        'payment systems to modern cloud-native architecture. Architected and executed the incremental migration of '
        'COBOL-based batch processing systems to containerized Spring Boot microservices on AWS, resulting in '
        '<b>70% reduction in processing time</b> and enabling real-time transaction capabilities. Implemented '
        'dual-run validation strategies to ensure zero data loss during the transition.',
        
        '<b>Legacy System Modernization:</b> Defined and drove the technical roadmap for core legacy system '
        'migration, orchestrating the transition from monolith to microservices, which enabled <b>60% faster '
        'feature release cycles</b> and reduced technical debt by <b>80%</b>.',
        
        '<b>FinOps and Automation:</b> Championed Infrastructure as Code (IaC) best practices '
        '(Terraform/CloudFormation) and FinOps principles, optimizing cloud resource consumption to achieve '
        '<b>30% reduction in infrastructure costs</b>.',
        
        '<b>Enterprise Security Governance:</b> Drove the adoption of standardized security frameworks across '
        '15+ applications, leveraging the proprietary file encryption system to mitigate PII exposure and '
        'ensure SAX audit compliance.',
        
        '<b>Observability:</b> Integrated enterprise observability solutions using OpenTelemetry, Prometheus, '
        'and Grafana to reduce mean-time-to-resolution (MTTR) and cut production incidents by <b>45%</b>.'
    ]
    
    for achievement in jpmc_achievements:
        story.append(Paragraph(f'• {achievement}', bullet_style))
    
    # ===== PAGE 2: Continued Experience and Education =====
    story.append(PageBreak())
    
    story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE (Continued)</b>', section_style))
    story.append(Spacer(1, 0.01*inch))
    
    # FIS - Senior IT Architect
    story.append(Paragraph('<b>FIS (Fidelity National Information Services)</b>', job_title_style))
    story.append(Paragraph(
        'Senior IT Architect | May 2017 – November 2017 (6 months)',
        job_info_style
    ))
    story.append(Paragraph('Milwaukee, Wisconsin, United States', job_info_style))
    
    fis_architect_achievements = [
        '<b>Cloud Strategy and Microservices:</b> Provided technical leadership on the in-house cloud strategy '
        'with OpenShift/Kubernetes adoption, driving the architectural design of a new Digital Banking Platform '
        'using Spring Boot Microservices.',
        
        '<b>Data Streaming:</b> Architected and implemented a complete message/event delivery backbone using '
        'Apache Kafka and Apache Apex for high-throughput micro-batching and real-time data flow.'
    ]
    
    for achievement in fis_architect_achievements:
        story.append(Paragraph(f'• {achievement}', bullet_style))
    
    story.append(Spacer(1, 0.03*inch))
    
    # FIS - Rules Engine Engineer/Architect
    story.append(Paragraph('<b>FIS (Fidelity National Information Services)</b>', job_title_style))
    story.append(Paragraph(
        'High-Performance Rules Engine Engineer/Architect | January 2004 – May 2017 (13 years 5 months)',
        job_info_style
    ))
    story.append(Paragraph('Milwaukee, Wisconsin, United States', job_info_style))
    
    fis_engineer_achievements = [
        '<b>Patented Rules Engine Architecture:</b> Architected, developed, and maintained a patented, '
        'SOA-certified, highly-scalable XML-based business rule engine (core Fraud/Payments system).',
        
        '<b>Performance Metrics:</b> Delivered a fault-tolerant system design that achieved <b>5000+ '
        'Transactions Per Second (TPS)</b> with <b>99.999% uptime</b>.',
        
        '<b>Optimization:</b> Drove performance optimization by implementing strategic caching mechanisms '
        '(Gemfire/Hazelcast) that resulted in an <b>80% reduction in database calls</b>.',
        
        '<b>Enterprise Observability and Monitoring:</b> Designed and deployed the ELK stack (Elasticsearch, '
        'Logstash, Kibana) for centralized logging and metrics aggregation, providing real-time monitoring of '
        'critical financial transaction pipelines.',
        
        '<b>Technical Mentorship:</b> Provided sustained technical mentorship and training to offshore '
        'engineering teams, establishing coding standards and best practices across the development life cycle.'
    ]
    
    for achievement in fis_engineer_achievements:
        story.append(Paragraph(f'• {achievement}', bullet_style))
    
    # Education
    story.append(Paragraph('<b>EDUCATION</b>', section_style))
    
    story.append(Paragraph('<b>Master of Computer Applications (MCA)</b>', job_title_style))
    story.append(Paragraph('Thiagarajar College of Engineering, India | 2004', job_info_style))
    
    story.append(Spacer(1, 0.02*inch))
    
    story.append(Paragraph('<b>Bachelor of Computer Science (B.Sc.)</b>', job_title_style))
    story.append(Paragraph('Madras University Chennai, India | 2001', job_info_style))
    
    # Build the PDF
    doc.build(story)
    print(f"✅ Resume PDF created successfully: {filename}")

if __name__ == '__main__':
    create_resume_pdf()
