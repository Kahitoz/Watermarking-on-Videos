# About this Project
The project is the demonstration of how can we implement the watermark on the videos
The project is mainly about buiding an api now much of the frontend part is paid attention

# Project Setup


* For the server - 
1) run this command after navigating to video-watermarker-server
pip install -r requirements.txt

2) MSSQL Server setup
download and install the sql server from this - https://www.microsoft.com/en-us/download/details.aspx?id=101064

3) after installation create the database named 'video-data'

4) change the credentials in db.py which is inside the database folder 

5) Navigate to the database directory and run this command 
uvicorn main:app --reload

6) After running the server open this link -> http://127.0.0.1:8000/docs and run the post upload_video route

Sample Video Credits -> https://www.pexels.com/
Sample Logo Credits -> https://www.peakpx.com/

