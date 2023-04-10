[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&pause=1000&color=FF9D2B&width=900&lines=Random+Website+Opener)](https://git.io/typing-svg)

<p>This program is a simple GUI application built using the Python <code>tkinter</code> library. The program allows the user to enter a search term and then opens a random website that contains the specified search term.</p>

<h2>How it Works</h2>

<p>When the user enters a search term and clicks the "Open Random Website" button, the <code>open_random_website_gui</code> function is called. This function retrieves the search term entered by the user from the <code>entry</code> field and passes it to the <code>open_random_website</code> function.</p>

<p>The <code>open_random_website</code> function then sends a request to Google with the specified search term and retrieves the first page of results. It then extracts the links to pages that contain the search term and saves them to a list. Finally, it selects a random link from the list and opens it in a new browser tab using the <code>webbrowser</code> library.</p>

<h2>Dependencies</h2>

<p>This program has the following dependencies:</p>

<ul>
  <li><code>tkinter</code>: The standard Python GUI library</li>
  <li><code>webbrowser</code>: A Python library for opening web pages</li>
  <li><code>requests</code>: A Python library for making HTTP requests</li>
  <li><code>random</code>: A standard Python library for generating random numbers</li>
</ul>

<h2>How to Use</h2>

<p>To use this program, you can follow these steps:</p>

<ol>
  <li>Clone the repository to your local machine</li>
  <li>Install the dependencies using pip</li>
  <li>Run the program using <code>python random_website_opener.py</code></li>
  <li>Enter a search term in the entry field and click the "Open Random Website" button</li>
</ol>

<p>The program will then open a random website that contains the specified search term.</p>

<p>Alternatively, if you do not want to install Python and its dependencies on your system, you can download an executable file from the <a href="https://github.com/miceroman/random-website-opener/releases">releases page</a>. Simply download the file and double-click it to run the program.</p>

<h2>License</h2>

<p>This program is licensed under the MIT License. See the <code>LICENSE</code> file for more information.</p>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=FFE809&width=300&lines=pls+star+%E2%AD%90)](https://git.io/typing-svg)
