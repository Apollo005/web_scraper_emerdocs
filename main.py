from bs4 import BeautifulSoup
import webbrowser

# Open the HTML file
with open("Course Welcome.html", "r") as HTMLFileToBeOpened:
    # Read the file and store the contents in a variable
    contents = HTMLFileToBeOpened.read()

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(contents, 'html.parser')

# Define the class to remove
unwanted_class1 = 'content_container element_2'
unwanted_class2 = 'content_container element_39'

# Find all div elements with the unwanted class
divs_to_remove1 = soup.find_all('div', class_=unwanted_class1)
divs_to_remove2 = soup.find_all('div', class_=unwanted_class2)

# Remove each found div
for div in divs_to_remove1:
    div.decompose()

for div in divs_to_remove2:
    div.decompose()

# Write the modified HTML to a new file
output_file = "Test_Course_Welcome.html"
with open(output_file, "w") as file:
    file.write(str(soup))


# Code for content
    
    
with open("Course Welcome.html", "r") as HTMLFileToBeOpened:
    # Read the file and store the contents in a variable
    contents = HTMLFileToBeOpened.read()

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(contents, 'html.parser')

unwanted_class3 = 'content_container element_101'
unwanted_class4 = 'content_container element_102'

# Find all div elements with the unwanted class
divs_to_remove3 = soup.find_all('div', class_=unwanted_class3)
divs_to_remove4 = soup.find_all('div', class_=unwanted_class4)

# Remove each found div
for div in divs_to_remove3:
    div.decompose()

for div in divs_to_remove4:
    div.decompose()

# Write the modified HTML to a new file
output_file = "Train_Course_Welcome.html"
with open(output_file, "w") as file:
    file.write(str(soup))