
# End-to-end-Medical-Chatbot-using-Llama2

## How to run?

STEPS:

1. Clone the repository

Project repo: https://github.com/

2. Create a python environment after opening the repository using python 3.10:
   
   python -m venv venv
   
   venv\Scripts\activate

3. Install the requirements:
   
   pip install -r requirements.txt

4. Create a `.env` file in the root directory and add your Pinecone credentials as follows:
   
   PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


5. Download the quantized model from the link provided in the `model` folder and place the model in the `model` directory:

   Download the Llama 2 Model:
   
   llama-2-7b-chat.ggmlv3.q4_0.bin

   From the following link:
   
   https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

6. Run the following command to store the index:
   
   python store_index.py

7. Finally, run the following command to start the application:
   
   python app.py

8. Open up localhost in your browser to access the chatbot.

---

## Tech Stack Used:
- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone

