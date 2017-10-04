# CSE503S Module 4 Individual
This repo is for module 4.  

## What do I do?
In this module, I write 3 regular expressions to match different patterns of plain text as well as a script to calculate the baseball stat.  
As for the former problem, I have nothing to say.  
But when it comes to the latter, I solve this problem to make it more convenient for user to use.

```
python spider.py {year}
```

The {year} in this command can be replaced by 1930 and 1940-1944. If you input other years, it will thow a error which would caught and handle by the program.  
Simply run the command above and it will automatically get the statistics you want without downloading the text file onto your local machine.  
I use "BeautifulSoup4", which is a famous web scrapying package of python, to get file list from the server, extracting and processing each season's information from them separately.