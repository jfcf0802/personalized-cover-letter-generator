# Personalized Cover Letter Generator

This project is web application built using [Gradio](https://gradio.app/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) to generate professional, customized cover letters based on user input. The application uses the [`Qwen/Qwen2.5-1.5B-Instruct`](https://huggingface.co/Qwen/QwQ-32B-Preview) model for natural language processing tasks.

## Features

- Generate tailored cover letters by providing:
  - Company Name
  - Company Description
  - Position Name
  - Job Description
  - Resume Content
- Ensures the generated cover letter aligns closely with the provided information.
- Outputs a concise, professional letter (max 200 words or 900 characters).
- Easy-to-use web interface.

## How It Works

1. **Model and Tokenizer Initialization**:
   - The application uses the `Qwen/Qwen2.5-1.5B-Instruct` model from Hugging Face for text generation.
   - The tokenizer and model are loaded using the `transformers` library.

2. **Text Generation Pipeline**:
   - A pipeline is set up to generate cover letters based on the given inputs.

3. **Gradio Interface**:
   - A web-based interface is built with Gradio, allowing users to enter the required fields and receive the generated cover letter.

4. **Cover Letter Generation**:
   - The model is prompted with user-provided data to create a personalized cover letter.

## Requirements

- Python 3.12
- Required Python packages:
  - `gradio`
  - `transformers`
  - `torch`

## Usage

1. Open the application in your browser.
2. Fill in the required fields:
    - Company Name: Enter the name of the company.
    - Company Description: Provide a description of the company.
    - Position Name: Specify the name of the position you’re applying for.
    - Job Description Information: Paste the job description.
    - Resume Content: Paste your resume content.
3. Click the "Submit" button.
4. The generated cover letter will appear in the output section.


## Example

![imagem](https://github.com/user-attachments/assets/822f97e5-539c-423e-aa8d-8c2cf7407d88)

- Input:
  - Company Name: ABC Corp
  - Company Description: A leading provider of innovative tech solutions.
  - Position Name: Data Scientist
  - Job Description Information: Develop and deploy ML models.
  - Resume Content: Experienced data scientist with expertise in Python and cloud platforms for model development and deployment.

- Output:
  
    Dear Hiring Manager,
  
    I am writing to express my interest in the Data Scientist position at ABC Corp, where I have been impressed by your commitment to innovation and excellence in technology. With over five years of experience in developing and deploying machine learning models across various industries, I bring a wealth of knowledge and skills that align perfectly with the challenges you face.
  
    My background includes extensive work with Python, leveraging its powerful libraries such as TensorFlow and Scikit-learn, which are essential tools for building robust predictive models. Additionally, I possess deep expertise in cloud platforms like AWS and Google Cloud, enabling me to efficiently manage large-scale datasets and perform complex analyses.
  
    In my current role at XYZ Corporation, I successfully developed an AI-driven recommendation system that significantly improved customer satisfaction and operational efficiency. This project showcased my ability to integrate cutting-edge technologies into real-world applications, demonstrating my capability to tackle complex problems with precision and creativity.
  
    I am particularly drawn to ABC Corp's reputation for pushing boundaries in technological advancement and would be thrilled to contribute to your team. My passion for data science and my proven track record make me a strong candidate for this role, and I look forward to discussing how my skills can further enhance our organization’s capabilities.
  
    Thank you for considering my application. I am excited about the opportunity to discuss how I can add value to ABC Corp.
  
    Sincerely,
    
    [Your Name]
