# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l01 — Data Classification Schemes & Sensitivity Labeling
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l01
# © LearnSome.tech
import shutil, zipfile
import xml.etree.ElementTree as ET
CP = ("{http://schemas.openxmlformats.org/officeDocument/2006/"
      "custom-properties}property")
def stamp(path, label):
    xml = open("custom.xml").read().replace(">Confidential<", f">{label}<")
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("docProps/custom.xml", xml)
        z.writestr("word/document.xml", "<w:document/>")

def read_label(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("docProps/custom.xml"))
    for prop in root.iter(CP):
        name = prop.get("name")
        if name.startswith("MSIP_Label_") and name.endswith("_Name"):
            return prop[0].text
if __name__ == "__main__":
    stamp("pricing-2027.docx", "Confidential")
    shutil.copy("pricing-2027.docx", "copy-for-partner.docx")
    for f in ["pricing-2027.docx", "copy-for-partner.docx"]:
        print(f, "is labelled", read_label(f))
