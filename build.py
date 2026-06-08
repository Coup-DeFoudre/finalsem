import os
import zipfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Coup-DeFoudre / Finalsem")
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, "This is a lightweight dummy PDF file for testing the Vercel static deployment.")
    c.drawString(100, 700, "After confirming that the download command works cleanly, you can replace")
    c.drawString(100, 680, "doc.zip with your original ZIP file.")
    c.save()

def create_zip(pdf_filename, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Save it inside the zip as 'document.pdf'
        zip_file.write(pdf_filename, arcname="document.pdf")

if __name__ == "__main__":
    pdf_file = "test.pdf"
    zip_file = "doc.zip"
    
    print(f"Generating {pdf_file}...")
    generate_pdf(pdf_file)
    
    print(f"Compressing to {zip_file}...")
    create_zip(pdf_file, zip_file)
    
    # Clean up the intermediate pdf file
    if os.path.exists(pdf_file):
        os.remove(pdf_file)
        
    print(f"Done! doc.zip size: {os.path.getsize(zip_file) / 1024:.2f} KB")
