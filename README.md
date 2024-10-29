# ScribeVision - a PDF Image Analysis Tool

Currently, multimodal LLMs cannot process scanned PDFs directly. This tool converts PDF pages to images, processes them through a Large Language Model (LLM), and generates detailed answers based on user prompts. Especially useful for exams, textbooks, and other educational materials.

## Features

- PDF to image conversion
- Automatic whitespace trimming for better image processing
- Integration with LLM API for image analysis
- Gradio web interface for easy interaction
- Results saved in markdown format with timestamps
- Context-aware processing between PDF pages

## Prerequisites

- Required Python packages:
  - gradio
  - pdf2image
  - Pillow
  - numpy
  - requests
  - python-dotenv

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ScribeVision
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your LLM API credentials:
```env
LLM_API_KEY=your_api_key
LLM_BASE_URL=your_api_base_url
LLM_MODEL=your_model_name
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to the provided Gradio interface URL (typically `http://localhost:7860`)

3. Upload a PDF file and enter your analysis prompt

4. View the results in the interface and find the detailed markdown report in the project directory

## Project Structure

- `app.py` - Main application file with Gradio interface
- `utils/`
  - `pdf_processor.py` - PDF conversion and image processing utilities
  - `llm_client.py` - LLM API client implementation
- `config.py` - Configuration and environment variables
- `results_*.md` - Generated analysis reports

## Output Format

The tool generates a markdown file for each analysis with:
- Timestamp
- Analysis prompt
- Results for each page
- Formatted content for easy reading

