import subprocess
import time
topics = ["html","css","design","javascript","ruby","php","wordpress","ios","android","development-tools","business","python"]
for topic in topics:
	subprocess.Popen(['python', 'minion.py', 'anubhav.sinha@live.com', 'TNixv10a', topic]) 
	time.sleep(2)