<h2> 1. My Achievements: </h2>

- The model is deployed by integrating LangChain’s AddRoute with FastAPI. 

- The chatbot model can extract information from PDF files (academic papers). When users ask questions, the LLM model (Llama-2-7B-Chat.Q6_K) can provide accurate answers.
  
**Below are some examples:**

  _a. Example 1:_
  
  Q: What is OCR? 
  
  A: "OCR stands for Optical Character Recognition which is the process of converting printed or visual text into editable machine-encoded text. This process involves two main modules - text detection and text recognition. The current state-of-the-art models on printed, handwritten, and scene text recognition tasks are available publicly through the link mentioned in the content."
  
  ![1](https://github.com/user-attachments/assets/e05828ce-41f9-4769-a672-aca76ca01cbb)
  _b. Example 2:_
  
  Q: What is Attention?
  
  A: "Attention is a mechanism used to relate different positions in a sequence of data. It allows a model to weigh the importance of different parts of the input when computing its output. In the context of the Transformer model, self-attention is used to compute the weighted sum of the encoder's output, where the weights are learned during training."
  
  ![2](https://github.com/user-attachments/assets/46545471-a151-4ec8-bc07-aede9643784e)
  
  c. Example 3:
  
  Q: Does Transformer have parallel computing capabilities?
  
  A: "Yes, Transformer has parallel computing capabilities. According to the context, the Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs."
  
  ![3](https://github.com/user-attachments/assets/53078fc4-8a13-402b-a4c2-e63f1cff5dec)
  
<h2> 2. Installation Guide: </h2>

**Step 1: Install Conda **
  
  Before setting up the environment, ensure you have Conda installed. Then, create the environment using the following command:

  `conda env create -f chatbot.yaml`
  
  Once the environment is set up, activate and work within it using:

  `conda activate chatbot`
  
**Step 2: Download the LLM Model**

Visit the [Hugging Face homepage](https://huggingface.co/) to download an LLM model compatible with your system.

**Step 3: Authenticate Hugging Face**

Generate a token in your Hugging Face account and log in on your machine using the following command:

`huggingface-cli login`

**Step 4: Download PDF Files**

Select and download the desired PDF files that the chatbot will process.

**Step 5: Start the Chatbot**

Run the chatbot using the following command:

`uvicorn src.app:app --host "0.0.0.0" --port 5050`

You can chance port in case have problems with this port 

**Step 6: Access the Chatbot**

Open your browser and go to: [http://localhost:5050/docs](http://localhost:5050/docs)
