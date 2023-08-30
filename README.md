# Meta Invoice Renamer

I came across this project on Upwork and decided to give it a shot. Here are the job requirements as provided by the client.

> Every month we have Meta (Facebook) invoices as attached. I would like to extract the reference number (f.ex. KJ3LSEBAS2 in the attached file) and rename the file with it.
>
> I should be able to insert a batch of invoices and get all renamed files back.
>
> In the end, the script should be easily usable by a non-programmer.

Here's the attachment, with confidential details blacked out to maintain privacy.

![a meta invoice](https://raw.githubusercontent.com/Kavishna/meta-invoice-renamer/main/meta_invoice.png)

Here are a few questions asked by the client, along with potential answers.

> 1.  What's your idea to make this easily usable by a non-programming person in the end?
>
> - **built a desktop application that is easy to use by a none programming person**

> 2.  What programming language would you use for this?
>
> - **python**

I suggest solving this problem by creating a desktop application using Tkinter. This application will be user-friendly for those without programming knowledge. Here's a breakdown of the issue:

- Pick a folder that has all the invoices. This way, the client can rename all the files together instead of doing it one by one, which is slow and frustrating.

## How can i find the reference number?

I have two methods in mind to locate the reference number.

1.  Since the PDFs are consistently generated with the same format, my first idea is to find the reference number's location and extract it from there.
2.  The second idea is to just use regular expressions (regex) to get the number. It's in a format like "Reference Number: KJ3LSEBAS2".

I chose the second method because it's easier to implement. I extract all the text from the PDF and then follow the pattern to retrieve the reference number. For extracting data from the PDF, I'm using the PyPDF2 library.

Here is the regex pattern:

    ref_pattern  =  r"Reference Number: ([A-Z0-9]+)"

This function will provide a reference number if one is available; otherwise, it will return "None".

    def  extract_ref_number(pdf_path):

        ref_pattern  =  r"Reference Number: ([A-Z0-9]+)"

        with  open(pdf_path,  "rb")  as  pdf_file:
    	    reader  =  PdfReader(pdf_file)
    		page  =  reader.pages[0]
    		str  =  page.extract_text()

    	    match  =  re.search(ref_pattern,  str)
    		if  match:
    			ref_number  =  match.group(1)
    			return  ref_number

        return  None

## User Flow

![user flow diagram](https://raw.githubusercontent.com/Kavishna/meta-invoice-renamer/main/user_flow.drawio.png)

This outlines the user flow:

1. When the app is launched, the user needs to choose a folder path containing the files they want to rename.
2. If no PDF files are discovered in the chosen path, a warning will be displayed, and the rename button will be deactivated.
3. If the user selects a folder with PDF files, they will be able to rename the files.

To manage files without reference numbers, I've introduced an error count. The function exits without renaming such files. After the process, a dialog will show the error and success counts to the user.

    if  ref_number  is  None:
    	failure_count  +=  1
    	continue
