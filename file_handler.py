
import io
import PyPDF2

async def read_file_content(attachment):
    file_bytes = await attachment.read()

    if attachment.filename.lower().endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
            text_content = "\n\n".join(page.extract_text() for page in pdf_reader.pages)
            return text_content.strip() or "The PDF doesn't contain extractable text."
        except Exception as e:
            return f"Error reading PDF file: {str(e)}"

    try:
        return file_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return f"Cannot process binary file: {attachment.filename}"
