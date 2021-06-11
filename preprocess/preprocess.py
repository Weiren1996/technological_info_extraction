# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:15:59 2021

@author: win
"""
import os


start_filter = ["https://api","RESOURCE_NOT_FOUND","Page Unavailable","Error","Wiley Online Library"]


class Preprocessor:
    def __init__(self, file_path):
        self.ori_txt_path = file_path
    
    def filter_by_start_length(self):
        """
        移除文件夹中以某字符开头且总文本长度小于700的文件,这种方法主要针对从Elsevier,Springer和willey期刊中得到的TXT文件
        在当前文件夹中删除不符合要求的TXT文件
        """
        process_txt = list()
        for txt in os.listdir(self.ori_txt_path):
            txt_path = os.path.join(self.ori_txt_path, txt)
            with open(txt_path, encoding='utf-8') as f:
                content = f.read()
                for start_str in start_filter:
                    if content.startswith(start_str) and len(content) < 700:
                        process_txt.append(txt)
        for txt_path in process_txt:
            os.remove(os.path.join(self.ori_txt_path, txt_path))
            
    
