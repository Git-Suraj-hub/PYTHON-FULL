from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image('C:/Users/suraj/OneDrive/Desktop/PYTHON1/PYTHON-FULL/PYTHON PROJECT/PDF/OIP.jpeg',10,8,25)
        self.set_font('times','b',16)
        pdf.cell(80,30,ln=0)

        self.cell(40,20,'RAM',border=1,align='C',ln=True)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('times','I',15)
        self.cell(0,10,f'No.{self.page_no()}/{{nb}}',border=0,align='C',ln=True)



# create fpdf object
#  layout --> "potarit" "landscape"
# unit --->   "mm" , "cm" , "in"
# format ---> "A3" ,"A4" , "A5" ,"legal" ,"letter" ,"(100(width),140(height))"
pdf = PDF("p","mm","A4")
# add a page in Pdf

pdf.alias_nb_pages()


pdf.set_auto_page_break(auto=True,margin=25)
pdf.add_page()

# set font
# font  ("times" , "courier" , "levicta" , "symbol")

# bold , italics , underline , 
pdf.set_font('Times','b',10)

# add cell

# width
# height
# border
# new line

for i in range(4000):
    pdf.cell(40,20,f'{i+1}). JAI SHREE RAM',border=0,ln=True)

pdf.output('1.pdf')

