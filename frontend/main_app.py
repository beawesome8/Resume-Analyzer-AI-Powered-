import streamlit as st
from backend.pdf_ingestion import load_split_pdf
from backend.vector_store import create_vector_store
from backend.analysis import analyze_resume
import os
import shutil
import uuid

# Main application with "Upload Resume" and "Resume Analysis" sections
def render_main_app():
    
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            min-width: 25%;
            max-width: 25%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Moving the upload section to the sidebar
    with st.sidebar:
        st.header("Upload Resume")  # Header for the upload section
        
        # File uploader for PDF resumes
        resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

        # Text area for job description input
        job_description = st.text_area("Enter Job Description", height=300)

        if resume_file and job_description:  # Check if both inputs are provided
            if resume_file.type != "application/pdf":
                st.error("Please upload a valid PDF file.")
                return
            
            # Create a temporary directory if it doesn't exist
        
            temp_dir = "temp"
            os.makedirs(temp_dir, exist_ok=True)
            
            # Generate unique filename to avoid conflicts
            file_id = str(uuid.uuid4())
            filename = f"{file_id}_{resume_file.name}"
            file_path = os.path.join(temp_dir, filename)

            # Save the uploaded file to the temporary directory
            with open(file_path, "wb") as f:
                f.write(resume_file.getbuffer())

            # Load the saved file
            resume_docs, resume_chunks = load_split_pdf(file_path)

            # Create a vector store from the resume chunks
            vector_store = create_vector_store(resume_chunks)
            st.session_state.vector_store = vector_store  # Store vector store in session state
                
            # Remove the temporary directory and its contents
            shutil.rmtree(temp_dir)

            # Button to begin resume analysis
            if st.button("Analyze Resume", help="Click to analyze the resume"):
                # Combine all document contents into one text string for analysis
                full_resume = " ".join([doc.page_content for doc in resume_docs])
                # Analyze the resume
                with st.spinner("Analyzing resume..."):
                    analysis = analyze_resume(full_resume, job_description)
                # Store analysis in session state
                st.session_state.analysis = analysis    
        else:
            st.info("Please upload a resume and enter a job description to begin.")

    # Display the analysis result if it exists in session state 
    if "analysis" in st.session_state:
        st.header("Resume-Job Compatibility Analysis")
        st.markdown(st.session_state.analysis, unsafe_allow_html=True)
    else:
        st.header("Welcome to the Ultimate Resume Analysis Tool!")
        st.subheader("Your one-stop solution for resume screening and analysis.")
        st.info("Do you want to find out the compatibility between a resume and a job description? So what are you waiting for?")

        todo = ["Upload a Resume", "Enter a Job Description", "Click on Analyze Resume"]
        st.markdown("\n".join([f"##### {i+1}. {item}" for i, item in enumerate(todo)]))