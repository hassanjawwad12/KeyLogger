# KeyLogger
Made a Key-Logger and signature based , rule-based and task manager detection system for it as part of the Information Security Project.

KeyLogger
<ul>
  <li>Save the keylogger script as a .py file.</li>
  <li>Open a command prompt and navigate to the directory where the script is saved.</li>
  <li>Run the script using the following command: python keylogger.py</li>
  
</ul>

Hash-based check:
<ul>
  <li>Create a database of known malware hashes.</li>
  <li>Extract the hashes of the files in the suspect directory.</li>
  <li>Compare the extracted hashes to the known malware hashes.</li>
  <li>If any matches are found, flag the corresponding files as malware.</li>
</ul>

Rule-based check:
<ul>
  <li>Defined a txt file which contains suspicious words.</li>
  <li>Monitor the files in the suspect directory for words that match the words in the txt file.</li>
  <li>If any suspicious behavior is detected, flag the corresponding files.</li>
</ul>

Task manager check:
<ul>
  <li>Open the Task Manager.</li>
  <li>Look for any unusual processes that are running.</li>
  <li>If you find any suspicious processes, investigate them further.</li>
</ul>
	

