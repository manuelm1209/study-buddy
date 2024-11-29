
# Study Buddy - Chat and Learn

**Study Buddy** is a document-based AI chatbot built using Streamlit and OpenAI's API. The application enables users to upload documents, transform them into embeddings, and interact with the content through an AI-powered chat interface.

## Features

- **Document Upload**: Users can upload files which are processed into embeddings for AI interaction.
- **Chat with Your Documents**: Use AI to query and learn from the uploaded documents.
- **Citations and References**: The assistant provides responses with citations for clarity and accuracy.
- **Streamlit Interface**: A user-friendly web interface for uploading files and chatting.

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. A valid OpenAI API key
3. Required Python packages (see `requirements.txt`)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/study-buddy.git
    cd study-buddy
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

### Running the Application

1. Start the Streamlit server:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to `http://localhost:8501` to access the app.

## How to Use

1. **Upload Files**: Use the sidebar to upload one or more documents.
2. **Transform to Embeddings**: Click the "Upload File" button to process the files.
3. **Start Chatting**: After uploading, click the "Start Chatting" button to initiate a session.
4. **Interact**: Use the chat input to ask questions about the uploaded documents. The assistant will respond with relevant citations.

## Customization

- Modify `app.py` to adjust settings such as the AI model (`gpt-4o-mini`) or chat instructions.
- Extend functionalities like additional file types or UI enhancements.

## Known Issues

- Placeholder citations: The citations for files are hardcoded as placeholders and should be connected to actual document retrieval.

## Future Enhancements

- Support for additional file types.
- Enhanced citation management.
- Improved UI/UX design.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Happy Learning!**
