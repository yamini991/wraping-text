from django.shortcuts import render
from myapp.models import Job_seeker
import PyPDF2


def index(request):
    if request.method== "POST":
        jname=request.POST["name"]
        jemail=request.POST["email"]
        jphone_no=request.POST["phone_no"]
        jskills=request.POST["skills"] 
        print('name is: ',jname)
        print('email is: ',jemail)
        print('phone_no is: ',jphone_no)
        print('skills is: ',jskills)

        job=Job_seeker()
        job.name=jname
        job.email=jemail
        job.phone_no=jphone_no
        job.skills=jskills
        job.save()
    else:
        return render(request,"myapp/index.html")

pdfFileObj = open('2+ -converted.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print('no of pages',pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 


# extracting text from page 
print(pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close()



