import time
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from PyPDF2 import PdfFileWriter, PdfFileReader
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="O nome/caminho do arquivo", metavar="FILE")
parser.add_option("-a", "--hash", dest="hash", help="A hash para a marca d'agua", metavar="FILE")
(options, args) = parser.parse_args()

c = canvas.Canvas('created/hash_watermark.pdf')

c.setFillColor(HexColor('#C0C0C0'))
c.setFont("Helvetica", 8)
c.drawString(40, 725, options.hash)
c.drawString(40, 15, options.hash)
c.save()

watermark = PdfFileReader(open("created/hash_watermark.pdf", "rb"))

output_file = PdfFileWriter()
input_file = PdfFileReader(open(options.filename, "rb"))

page_count = input_file.getNumPages()

for page_number in range(page_count):
    print "Marca d'agua na pagina {} de {}".format(page_number, page_count)
    input_page = input_file.getPage(page_number)
    input_page.mergePage(watermark.getPage(0))
    output_file.addPage(input_page)

output_file_name = "created/document-output.pdf"
with open(output_file_name, "wb") as outputStream:
    output_file.write(outputStream)