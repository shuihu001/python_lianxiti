"""
-*- coding: utf-8 -*-
@author: wang cong
@Created on: 2020/2/12 16:46
@File : wiki_loop.py
@Software: PyCharm
@desc:
"""



def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True