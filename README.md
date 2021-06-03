<p align="center">
  <h1 align="center">TMDB-Scraper</h1>
</p> 
Python script that allows to create a simple dataset of images extracted directly from Google Images from a term entered by the user.

Currently, it collects a small set of images that can serve as a starting point for the creation of the desired set of images.

# How it works
Once the script and the required webdriver (in this case the Google Chrome webdriver is used) have been downloaded, the file is executed. It will ask for two fields:
* Term: what you want the dataset to be about .
* Path: place where you want to create the directory where the downloaded images will be stored. It is recommended that the path be in the form *Users/me/directory*, without the final slash. 

Finally, you will have the images that could have been downloaded in the specified directory in .jpg format.

# Requirements
In requierements.txt it is possible to check the libraries needed to run the script. It is recommended for a correct execution of the program that the webdriver.exe file that uses the Selenium library is located in the same directory from which the script is launched.
