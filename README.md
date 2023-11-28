# KeyLogger
Made a Key-Logger and signature based , rule-based and task manager detection system for it as part of the Information Security Project.

#KeyLogger
⦁	Save the keylogger script as a .py file.
⦁	Open a command prompt and navigate to the directory where the script is saved.
⦁	Run the script using the following command: python keylogger.py
#Hash-based check:
⦁	Create a database of known malware hashes.
⦁	Extract the hashes of the files in the suspect directory.
⦁	Compare the extracted hashes to the known malware hashes.
⦁	If any matches are found, flag the corresponding files as malware.
#Rule-based check:
⦁	Defined a txt file which contains suspicious words.
⦁	Monitor the files in the suspect directory for words that match the words in the txt file.
⦁	If any suspicious behavior is detected, flag the corresponding files.
#Task manager check:
⦁	Open the Task Manager.
⦁	Look for any unusual processes that are running.
⦁	If you find any suspicious processes, investigate them further.


