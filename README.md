<!-- HEADING -->

<h1 align="center">App Blocker</h1>

<div align="center">
  <img src="https://github.com/LopezIgnacio2201/appBlocker/assets/105466036/396b1098-1196-4cd8-a5c8-66cddafbb2b0" width="800" height="400">
</div>

<!-- END OF HEADING -->

<br>

<!-- START BLOCK OF DESCRIPTION -->

<p align="center"> Welcome! AppBlocker is a really short python terminal based program that asks the user for some name of an app that it wishes to block, and a timer. More on the technical
aspects of the program later; after the timer reaches 0, it blocks the program and it prevents the user from executing it until the next day.
</p>

<p align="center">Currently, the program while it gets the job done, it is somewhat buggy on some aspects and could be optimized.</p>

<p align="center"> Feel free to explore the code and provide feedback if you have any!</p>

<!-- END BLOCK OF DESCRIPTION -->

<hr>

<!-- START BLOCK OF DOCUMENTATION -->

<div align="center" id="user-content-toc">
  <details>
    <summary>
      <h1 align="center" id="documentation"> Documentation </h1>
    </summary>   

<p align="center">
  <strong>This project was made using:</strong>
</p>

<div align="center">
  <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/VSCode-Dark.svg" width="100" height="100"/>
  <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Python-Dark.svg" width="100" height="100"/>
</div>

<hr>

<h4 align="center"> Installation and use:
</h4>

<!-- START TABLE -->

<table><tr><td valign="top" width="50%">
<br>

<p align="center">
  <em>Inside the main folder there will be two .py, "configScript.py" and "silentMode.py". To get started for the very first time, execute configScript.py, which would do some checks
  and functions call if needed (More on this below), it will also prompt for the AppName and the timer. As you can see, theres silentMode.py and silentMode.exe, both works the same however the .py may require installation of certain dependencies and resources, while the .exe does not.</em>
</p>
<br>
<p align="center">
  <em>The script would check if the windows registry key on "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\explorer" exists, if not, create it. It will also create the disallowRun key
  which will be used later to block the programs. Then it will check and add the script "silentMode.py" to startup, lastly, after prompting the user for appname and the timer, it will
  modify the config.json inside the json folder with the data provided.  </em>
</p>
<br>
<ul align="center">
  <li>AppName MUST BE identical to how the executable of the app is called, including the extension.</li>
  <li>The process of such app MUST ALSO BE either identical or really similar to the name of the app for the script to work correctly.</li>
  <li>KEEP IN MIND that due to how the program works, it can only block 1 app at a time. Surely there is a workaround, like creating multiple disallowRun keys and each storing 1 app, for example. </li>
</ul>

<p align="center">
  <em>After configScript.py was succesful, run silentMode.py (Or restart the computer to avoid any kind of issues, program should autorun by now), it will keep in the background as silent
  as possible, waiting and checking for processes related to the app that indicated to be blocked, once it detectes it, ergo the app is running, start the timer countdown. Once it reaches 0, it kills the process and sets on the windows registry "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\explorer\DisallowRun" a new string with name 1 and value data being the appname, which would prevent such app from executing.  </em>
</p>

<p align="center">
  <em>Keep in mind I'm a cybersecurity student, there is probably much room for optimization and bug fixing, feel free to modify and re-distribute the code as you like (I would appreciate some kind of mention)</em>
</p>

<br>

</td></tr></table>  

<!-- END TABLE -->

<br/>  
    
</details>

<!-- END BLOCK OF DOCUMENTATION -->

<hr>


<!-- START BLOCK AUTHOR/CONTACT -->

<h2 align="center">Author</h2>

<div align="center">
<img src="https://user-images.githubusercontent.com/105466036/233513753-5a5f04fb-4310-4a77-b282-1a0cbe8b0256.jpg" alt="Author photo" width=250 height=250>  
</div>

<h2 align="center">Contact</h2>

<div align="center">

  <p align="center">
  <a href="https://www.linkedin.com/in/ignacio-ariel-lopez/">
    <img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white" alt="LinkedIn Badge">
  </a>
  
  <a href="https://github.com/LopezIgnacio2201">
    <img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white" alt="GitHub Badge">
  </a>
  
  <a href="mailto:lopezignacio2201@gmail.com">
    <img src="https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white" alt="Gmail Badge">
  </a>
</p>

</div>

<br>

<!-- START FOOTER -->

<p align="center">
  <sub>If you found this project interesting or useful in any way, please consider giving it a ⭐️ on <a href="[https://github.com/LopezIgnacio2201/cs50-archive]">GitHub ❤︎</a>!</sub>
</p>

<!-- END FOOTER -->