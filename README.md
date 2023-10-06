# List of Greek Gods and Goddesses

> Web scraping of Wikipedia's [List of Greek mythological figures](https://en.wikipedia.org/wiki/List_of_Greek_mythological_figures).



## General info

Gods, titans, nymphs, and other divine figures were extracted from Wikipedia's [List of Greek mythological figures](https://en.wikipedia.org/wiki/List_of_Greek_mythological_figures) in December 2020. Most sections contained their own unique formatting style. Basic features were created and entry descriptions, many of which were quite lengthy, were condensed. 

A large handful of entries also needed to be corrected since they contained uncomfortably incomplete information and duplicates were removed. It was often obvious which duplicate entry to remove (e.g. 'Nyx: Νύξ: god: primordial: goddess of night' was kept and 'Nyx: Νύξ: god: chthonic: primeval goddess of night' was removed ). However, knowledge of the subject area was sometimes needed to make the correct decision (e.g. 'Thanatos: Θάνατος: god: primordial: god of death' was kept and 'Thanatos: Θάνατος: god: chthonic: god of death' was removed.)

This list and the Wikipedia list are not exhaustive. For example, it does not contain all entries for Oceanids and Potamoi, both which have their own long lists on separate pages. It also does not include heros, kings, and other mortals. In total, the resulting list contains a total of 445 divine figures.



Each entry was separated into the following:

* `name-english`: name in English; if multiple, the most well-known was chosen

* `name-greek`: name in Greek corresponding to the English name

* `main-type`: entry type: god, titan, or personification

* `sub-type`: type within `main-type`; often the type of god: e.g. olympian, primordial, chthonic, sea, sky, etc. 

* `description`: brief lower-cased description of the entry

  

The following files are included in this repo:

* `greek_gods_dataframe.ipynb`: code creating the dataframe
* `greek_gods_lists.py`: web scraping code
* `greek_gods.csv`: list of gods and goddesses exported from the dataframe
* `source_code.html`: a snapshot of the webpage; last modified 7 December 2020.



## Technologies

Python 3.7.6; the following modules were heavily utilised: BeautifulSoup, re, pandas. 



## Inspiration

My academic studies have always had a focus on religion in antiquity (albeit often Roman). This project no doubt was influenced by my profound interest in the subject. 
