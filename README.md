# LangChain React Agent with Google Gemini and SerpAPI

This project demonstrates how to build a LangChain-based AI agent that can:

- Search the web using **SerpAPI**
  
- Perform custom logic using tools (e.g., count text length)
  
- Respond intelligently using **Google Gemini 1.5 Flash** as the language model

## Features

-  **SerpAPI Integration**: Real-time search results from the web
  
-  **Google Generative AI (Gemini)**: Fast and efficient language model reasoning
  
-  **Custom Tools**: Example function to return text length
  
-  **AgentExecutor**: Enhanced control with error handling and intermediate steps

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/Hariarul/langchain_react_agent_that_searches_web.git
```

### Install Dependencies

pip install -r requirements.txt

### Create .env File

SERPAPI_API_KEY=your_serpapi_key_here

GOOGLE_API_KEY=your_google_gemini_api_key_here

### Run the Application

python main.py

### output 

```
Hi hari...you here again...
Response 1 Output: Several laptops with RTX 3050 and RTX 4050 GPUs are available under ₹70,000.  However, I cannot provide direct purchase links due to constantly changing prices and availability.  I recommend searching major online retailers (like Flipkart or Amazon India) for laptops with "RTX 4050" or "RTX 3050" within your budget.  The RTX 4050 will generally offer better performance for LLM fine-tuning.  Remember to check the VRAM (video RAM) amount; more VRAM is better for this task.
Response 2 Output: 6

```




