import os
from dotenv import load_dotenv
import openai
import json

import time
import logging
from datetime import datetime
import streamlit as st

load_dotenv()

client = openai.OpenAI()

model = "gpt-4o-mini"

# Create a vector store caled "Test Vectore Store"
# vector_store = client.beta.vector_stores.create(name="Test Vectore Store")

# Step 1. Upload a file to OpenAI embeddings ===
file_path = ["./cryptocurrency.pdf"]
file_streams = [open(path, "rb") for path in file_path]

# Upload the user provided file to OpenAI
# file_path_2 = "./AI_Program_Brochure.pdf"
# file_object = client.files.create(
#   file=open(file_path_2, "rb"), purpose="assistants"
# )

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
# file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
#   vector_store_id=vector_store.id, files=file_streams
# )

# You can print the status and the file counts of the batch to see the result of this operation.
# print(file_batch.status)
# print(file_batch.file_counts)


# Step 2. Create an assistant
# assistant = client.beta.assistants.create(
#     name="Study Buddy",
#     instructions="""You are a helpful study assistant who knows a lot about understanding research papers.
#     Your role is to summarize papers, clarify terminology within context, and extract key figures and data.
#     Cross-reference information for additional insights and answer related questions comprehensively.
#     Analyze the papers, noting strengths and limitations.
#     Respond to queries effectively, incorporating feedback to enhance your accuracy.
#     Handle data securely and update your knowledge base with the latest research.
#     Adhere to ethical standards, respect intellectual property, and provide users with guidance on any limitations.
#     Maintain a feedback loop for continuous improvement and user support.
#     Your ultimate goal is to facilitate a deeper understanding of complex scientific material, making it more accessible and comprehensible.""",
#     tools=[{"type": "file_search"}],
#     model=model,
# )

# # === Update the assistant to use the new Vector Store ===
# assis_id = assistant.id
# vector_store_id = vector_store.id
# print(f"Assistant ID: {assis_id}")
# print(f"Vector Store ID: {vector_store_id}")

# assistant = client.beta.assistants.update(
#   assistant_id=assistant.id,
#   tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
# )

# == Hardcoded ids to be used once the first code run is done and the assistant was created
assis_id = "asst_Xr0FXRBhGUjAiURw2YkgnrdU"
thread_id = "thread_OXNU4QTfQt5XVNzGogD4JReV"

# # === Step 3. Create a Thread
message = "What is mining?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

# thread = client.beta.threads.create(
#     messages=[{
#         "role":"user",
#         "content":message,
#         # Attach the new file to the message.
#         "attachments": [{ "file_id": file_object.id, "tools": [{"type": "file_search"}]}],
# }])
# thread_id = thread.id
# print(f"Thread ID: {thread_id}")

# === Run the Assistant
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assis_id,
    instructions="Please address the user as James Bond"
)


def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    if thread_id and run_id:
        while True:
            try:
                run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
                if run.completed_at:
                    elapsed_time = run.completed_at - run.created_at
                    formatted_elapsed_time = time.strftime(
                        "%H:%M:%S", time.gmtime(elapsed_time)
                    )
                    print(f"Run completed in {formatted_elapsed_time}")
                    logging.info(f"Run completed in {formatted_elapsed_time}")
                    # Get messages here once Run is completed!
                    messages = client.beta.threads.messages.list(thread_id=thread_id)
                    last_message = messages.data[0]
                    response = last_message.content[0].text.value
                    print(f"Assistant Response: {response}")
                    # st.markdown("#### MESSAGES: ")
                    # st.write(messages)
                    break
            except Exception as e:
                logging.error(f"An error occurred while retrieving the run: {e}")
                break
            logging.info("Waiting for run to complete...")
            time.sleep(sleep_interval)
        
# === Run it
wait_for_run_completion(client=client,
                        thread_id=thread_id,
                        run_id=run.id)

# === Check the Run Steps - LOGS ===
run_steps = client.beta.threads.runs.steps.list(thread_id=thread_id, run_id=run.id)
print(f"\nRun Steps:::>>> {run_steps.data[0]}")

thread_retrieve = client.beta.threads.retrieve(thread_id)
print(f"\nThread retreaved: {thread_retrieve}")

# st.write(thread_retrieve)