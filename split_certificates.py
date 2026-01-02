import PyPDF2
import csv
import os

# Read the ID mapping from id.csv
ids = []
with open('id.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ids.append(row['ID'])

print(f"Found {len(ids)} certificate IDs")

# Create assets folder if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')
    print("Created assets folder")

# Open the PDF file
pdf_file = open('certficates.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

total_pages = len(pdf_reader.pages)
print(f"PDF has {total_pages} pages")

if total_pages != len(ids):
    print(f"WARNING: PDF has {total_pages} pages but id.csv has {len(ids)} entries")

for i in range(total_pages):
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(pdf_reader.pages[i])

    if i < len(ids):
        cert_id = ids[i]
        output_filename = f'assets/{cert_id}.pdf'

        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)
        
        print(f"Page {i+1}/{total_pages}: Saved as {output_filename}")
    else:
        print(f"Page {i+1}/{total_pages}: No ID mapping found, skipping")

pdf_file.close()
print("\n✅ PDF splitting complete!")
print(f"All certificates saved in the 'assets' folder")
