import pdfplumber 
import pyperclip
import json
from types import SimpleNamespace



with pdfplumber.open("pdf_files/test2.pdf") as pdf:
    accumulator = [];

    for page in pdf.pages:
        p0 = pdf.pages[0]

    #     # crops the the page into quarters
        first_quarter = p0.crop((0.13 * float(p0.width), 0.12 * float(p0.height), 0.32 * float(p0.width), 0.89 * float(p0.height)))
        second_quarter = p0.crop((0.30 * float(p0.width), 0.12 * float(p0.height), 0.50 * float(p0.width), 0.89 * float(p0.height)))
        third_quarter = p0.crop((0.49 * float(p0.width), 0.12 * float(p0.height), 0.68 * float(p0.width), 0.89 * float(p0.height)))
        fourth_quarter = p0.crop((0.68 * float(p0.width), 0.12 * float(p0.height), 0.90 * float(p0.width), 0.89 * float(p0.height)))


    # # extracts the words from the section of the page along with the fontname attributes
        firstExtract = first_quarter.extract_words(x_tolerance =10, y_tolerance=1.5, keep_blank_chars=True, extra_attrs=["fontname"])
        secondExtract = second_quarter.extract_words(x_tolerance =10, y_tolerance=1.5, keep_blank_chars=True, extra_attrs=["fontname"])
        thirdExtract = third_quarter.extract_words(x_tolerance =10, y_tolerance=1.5, keep_blank_chars=True, extra_attrs=["fontname"])
        fourthExtract = fourth_quarter.extract_words(x_tolerance =10, y_tolerance=1.5, keep_blank_chars=True, extra_attrs=["fontname"])

    # # concatinates de extract arrays
        fullExtract = firstExtract + secondExtract + thirdExtract + fourthExtract
        accumulator += fullExtract

    # # converts the results to JSON
    else:
        print(accumulator)
        jsoned = json.dumps(accumulator)

    # appends the results to a json file
        f = open("python-extractor.json", "a")
        f.write(jsoned)

        
        # string = pyperclip.copy(str(results))
        # print(json)