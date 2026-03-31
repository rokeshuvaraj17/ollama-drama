# Study Plan

A study plan for the concepts covered here is outlined below:

**Module 1: Getting Started with Ollama**

* **Installation and Setup**: Understand the installation process for various platforms including macOS, Linux, and Windows.  
* **Advantages of Local LLMs**: Explore the benefits of running models locally, such as data privacy (intellectual property protection), speed, and the absence of API rate limits.  
* **Model Repository Navigation**: Familiarize yourself with the Ollama website to browse popular models like Google's Gemma 3 (creative work) and Meta's Llama (creative and general tasks).

**Module 2: Model Architecture and Performance**

* **Understanding Parameters**: Learn how model size (e.g., 1B vs. 8B vs. 70B parameters) impacts accuracy, resource requirements (RAM and disk space), and processing speed.  
* **Selecting the Right Model**: Compare different models based on use cases, such as using Code Llama for programming or Qwen 3 for fast chatbot interfaces.  
* **Inference Logic**: Study how certain models, like Qwen 3, use a "thinking" process to introspect and provide more logical answers compared to direct responses.

**Module 3: Working with the Ollama CLI**

* **Basic Commands**: Practice essential command-line operations:  
  * ollama list: View currently installed models.  
  * ollama pull: Download specific models from the repository.  
  * ollama run: Execute a model and interact with it via the terminal.  
  * ollama ps: Check which models are currently active in memory.  
  * ollama stop: Remove a model from active memory to free resources.  
  * ollama cp and ollama rm: Manage model files by copying or deleting them.

**Module 4: Advanced Customization and Integration**

* **System Prompts**: Learn to use system prompts to define an LLM's persona or specific behavior (e.g., acting as a career planner or answering only in knock-knock jokes).  
* **Creating Custom Models (Modelfiles)**: Master the creation of personalized local models by baking prompts and parameters into a "Modelfile".  
* **API and Programming Integration**:  
  * **Curl**: Use Curl to interact with the generate and chat API endpoints.  
  * **Python Scripts**: Utilize libraries like Gradio to build web-based chatbot interfaces and the Requests library to programmatically communicate with the local LLM.  
  * **Testing**: Implement Python tests (e.g., Pytest) to verify that customized models respond with expected accuracy.
