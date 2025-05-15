# stt-osc-td

# Vosk / OSC / and TouchDesigner
This project performs real-time speech-to-text recognition using Vosk and sends the recognized speech as OSC messages to TouchDesigner.

# Prerequisites
Before getting started, you must have the following:

Python 3.7+

Download the language model in your folder

TouchDesigner (running on the same machine or network)

Internet connection (for initial package installations)



# Setup Instructions
## 1. Download a Vosk Language Model:

Download an English model (or your preferred language) from the Vosk Models page:
https://alphacephei.com/vosk/models 

## 2. Create a Virtual Environment:

In your Terminal use the following command:
      
      python3 -m venv my_venv

Activate the Virtual Enviroment:
  
      source my_venv/bin/activate  # On Windows use: my_venv\Scripts\activate

## 3. Install Dependencies:
When in the Virtual Environment now you can install the dependencies. 
Terminal Command: 
      
      pip install -r requirements.txt

## 4. Configuration:
Update the following variables in the main script (stt_osc_main.py):
      
      model_path: Path to the downloaded and extracted Vosk model.
      
      osc_ip and osc_port: IP address and port where TouchDesigner is listening.
      
      output_file_path: Path to save recognized speech locally.

## 5. OSC Setup in TouchDesigner

Add an OSC In DAT in TouchDesigner.
Set its network port to match osc_port in the script (in our example 10002).
Optional: Add a Convert DAT to convert the messages to Table (Split Cells at “”). Then add a Select DAT to select only the column of the messages. You can add another Convert DAT to convert the table to plain text.

## 6. Run the Application
Activate your virtual environment (if not already activated), then run:
	
     python3 stt_osc_main.py

Say "terminate" to stop the application.

## 7. Clean Exit
The script will automatically shut down when it hears the word "terminate". You can also stop it with CTRL+C.
