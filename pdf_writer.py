from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
import html

def clean_html(text):
    # Remove broken tags and only allow <b>, <i>, <u>
    allowed_tags = ['b', 'i', 'u']
    text = html.escape(text)  # Escape all HTML first
    # Then unescape allowed tags
    for tag in allowed_tags:
        text = text.replace(f"&lt;{tag}&gt;", f"<{tag}>").replace(f"&lt;/{tag}&gt;", f"</{tag}>")
    return text

def create_study_pdf(explanations, filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=60, bottomMargin=60)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='SlideTitle', fontSize=16, leading=20, spaceAfter=12, alignment=TA_LEFT, fontName='Helvetica-Bold'))
    styles.add(ParagraphStyle(name='SlideText', fontSize=12, leading=16, spaceAfter=10, alignment=TA_LEFT))

    story = []

    # Add the single heading
    story.append(Paragraph("Simpler Explanation", styles['SlideTitle']))
    story.append(Spacer(1, 12))

    # Combine and write all lines neatly
    if isinstance(explanations, list):
        explanation_text = "\n".join(explanations)
    else:
        explanation_text = explanations

    for line in explanation_text.split('\n'):
        cleaned_line = clean_html(line.strip())
        if cleaned_line:
            story.append(Paragraph(cleaned_line, styles['SlideText']))

    doc.build(story)

