from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from textwrap import wrap

# ✅ Register Unicode font (supports emojis like 📘)
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

def create_study_pdf(explanations, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("DejaVuSans", 12)

    width, height = letter
    left_margin = 50
    right_margin = 50
    y = height - 50
    line_height = 18
    max_chars_per_line = 90  # Adjust for font size

    for i, explanation in enumerate(explanations, 1):
        title = f"📘 Slide {i}:"
        content = title + "\n" + explanation

        # Split content by lines and wrap each long line
        lines = []
        for line in content.split("\n"):
            lines.extend(wrap(line, width=max_chars_per_line))

        for line in lines:
            if y < 50:  # If we reach bottom, go to next page
                c.showPage()
                c.setFont("DejaVuSans", 12)
                y = height - 50
            c.drawString(left_margin, y, line)
            y -= line_height

        y -= 15  # Extra space between slides

    c.save()

