try:
    import streamlit as st
    from PyPDF2 import PdfFileReader
    print("Modules imported successfully!")
except ImportError as e:
    print("Error importing modules:", e)