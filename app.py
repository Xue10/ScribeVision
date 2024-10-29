import gradio as gr
import os
from datetime import datetime
from utils.pdf_processor import convert_pdf_to_images, trim_whitespace, encode_image
from utils.llm_client import LLMClient

class PDFAnalyzer:
    def __init__(self):
        self.llm_client = LLMClient()
        
    def process_pdf(self, pdf_file, prompt):
        # Convert PDF to images
        images = convert_pdf_to_images(pdf_file.name)
        
        results = []
        # Process each image
        for idx, img in enumerate(images):
            try:
                # Trim whitespace
                trimmed_img = trim_whitespace(img)
                # Encode image
                encoded_img = encode_image(trimmed_img)
                # Query LLM
                response = self.llm_client.query_image(encoded_img, prompt)
                
                result = response['choices'][0]['message']['content']
               
                
            except Exception as e:
                result = f"Error processing page {idx + 1}: {str(e)}"
            
            results.append(result)
            print(f"Result for page {idx + 1}: {result}")  # Debug print
            
        # Save results in markdown format
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"results_{timestamp}.md"
        with open(output_file, "w") as f:
            f.write(f"# PDF Analysis Results\n\n")
            f.write(f"## Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Prompt\n{prompt}\n\n")
            f.write("## Results\n\n")
            for idx, result in enumerate(results):
                f.write(f"### Page {idx + 1}\n{result}\n\n")
                
        return "\n\n".join(results)

def create_gradio_interface():
    analyzer = PDFAnalyzer()
    
    def process_file(pdf_file, prompt):
        return analyzer.process_pdf(pdf_file, prompt)
    
    interface = gr.Interface(
        fn=process_file,
        inputs=[
            gr.File(label="Upload PDF", file_types=[".pdf"]),
            gr.Textbox(label="Enter your prompt", value="Answer all the questions.")
        ],
        outputs=gr.Textbox(label="Results"),
        title="ScribeVision - a PDF Image Analysis Tool",
        description="Upload a PDF file and ask questions about its contents."
    )
    
    return interface

if __name__ == "__main__":
    interface = create_gradio_interface()
    interface.launch() 