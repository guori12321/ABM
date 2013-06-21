# Adblock Minus (ABM)

I aims to block more advertisements by less rules. Thus I name my program `Adbluck Minus`.

## Author Introduction
Author: Guo Rui

Sex: Male

Affiliation: Harbin Institute of Technology (HIT) 

Grade: Junior

Age: 20

E-mail: guori12321@gmail.com

github ID: guori12321

blog: guori12321.github.cn

Hi, I'm Guo Rui (Guo is the family name), a junior student of Harbin Institute of Technology.
My major is software engineering, and I'll get my bachelor degree in 2014.

I love coding, in fact, I develop a chrome extension to time how long users focus on renren.com (a social network website that is similar to facebook).
I'm always excited about social network, and I published a paper `CUVIM: Extracting Fresh Information from Social Network` on `WAIM2013`.
The paper describes the math model that I built for the weibo.com (another social network that is similar to twitter) crawler. 
I want to solve the current web problems, including advertisement recognizing and social network analyzing, through distribution, machine learning and data mining methods.

## ABM Describe
Advertisements all have their links: when you click the ad, no matter picture ad or text ad, they will lead you to a website who post advertisements. 

Assume that there are only ten web pages in the whole world, and there is only one company who post advertisements.
In such case, we just block this company, and all the advertisements are blocked. 
`ABM` just collects several companies who post ads, and block them.

However, there are far more than ten web pages and one company.
At present `ABM` is simple and low effective, for the company list is far from complete.
To get a better rule list to detect ads, I revise the `chinaLazy` list to `GuoRuiList`.
Both the `chinaLazy` list and `GuoRuiList` is included in the root path of this program, as well as the revise script `revise.py`. As for the RegExp in the `chinaLzay`, it is too slow to run it in ABM. So I remove all the RegExp.

I search the html documents through Depth-First-Search (DFS) and match the elements and rules. It is slow, however, it is the best I can do, for the time in this contest is limited.

The ABM may take 30 seconds when search a complicate web pages such as youku.com.

## File list
1. content.js : The source code of ABM.

2. manifest.json : I develop ABM as a chrome extension, and this file is necessary for it.

3. Guo_Rui_CV.pdf : My CV.

4. README.md : just this README file that you are looking at.

5. revise.py : to revise the `chinaLazy` list to a available list (GuoRuiList.txt) for ABM.

6. GuoRuiList.txt : the available list that is revised from `chinaLazy` by revise.py.

7. chinalazy.txt : the `chinaLazy` list.

## Licence
MIT
