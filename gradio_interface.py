# Import necessary packages
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# import torch

# # Check if a GPU is available
# device = 0 if torch.cuda.is_available() else -1

# Model and project settings
# Using a smaller, faster model
# model_id = "allenai/Llama-3.1-Tulu-3-8B"

# # Initialize the tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id)

# # Initialize the text generation pipeline with hardware acceleration
# generator = pipeline('text-generation', model=model,
#                      tokenizer=tokenizer, do_sample=True)

generator = pipeline("text-generation", model="microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True)

# Function to generate a customized cover letter


def generate_cover_letter(company_name, position_name, job_description, resume_content):
    # Craft the prompt for the model to generate a cover letter
    prompt = f"Generate a customized cover letter using the company name: {company_name}, the position applied for: {position_name}, and the job description: {job_description}. Ensure the cover letter highlights my qualifications and experience as detailed in the resume content: {
        resume_content}. Adapt the content carefully to avoid including experiences not present in my resume but mentioned in the job description. The goal is to emphasize the alignment between my existing skills and the requirements of the role."

    # # Debugging: Print the prompt to verify it
    # print("Prompt:", prompt)

    # Generate the cover letter
    generated_response = generator(prompt, max_new_tokens=300, temperature=0.2)

    # Extract the generated text
    cover_letter = generated_response[0]["generated_text"]

    # Debugging: Print the generated cover letter to verify it
    print("Generated Cover Letter:", cover_letter)

    return cover_letter


# Create Gradio interface for the cover letter generation application
cover_letter_app = gr.Interface(
    fn=generate_cover_letter,
    inputs=[
        gr.Textbox(label="Company Name",
                   placeholder="Enter the name of the company..."),
        gr.Textbox(label="Position Name",
                   placeholder="Enter the name of the position..."),
        gr.Textbox(label="Job Description Information",
                   placeholder="Paste the job description here...", lines=10),
        gr.Textbox(label="Resume Content",
                   placeholder="Paste your resume content here...", lines=10),
    ],
    outputs=gr.Textbox(label="Customized Cover Letter", placeholder="The generated cover letter will appear here..."),
    title="Customized Cover Letter Generator",
    description="Generate a customized cover letter by entering the company name, position name, job description and your resume."
)

# Launch the application
cover_letter_app.launch(share=True)
