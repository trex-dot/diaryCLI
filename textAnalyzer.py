import os
import re
class textAnalyzer():
    def __init__(self, filename):

        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' does not exist")
        self.filename = filename
        with open(filename, 'r') as f:
              self.content = f.read()
        self.lines = self.content.splitlines()
    @property    
    def wordcount(self):
        
        words = self.content.split()
        return len(words)          
    @property    
    def line_count(self):
        
        count_lines=0
        for i in self.lines:
            count_lines=count_lines+1
        return count_lines    

    @property    
    def char_count(self):
       
        return len(self.content)       

    def most_common_words(self,n):
        common_words={}
        
        self.content=" ".join(self.content.split())
        for word in self.content.split():
            if word not in common_words:
                common_words[word]=1
            else:
                common_words[word]=common_words[word]+1
        sorted_data = dict(sorted(common_words.items(), key=lambda x: x[1], reverse=True))
        items = dict(list(sorted_data.items())[:n])
        return items
        


    def find_sentences_with(self,word):
        
        sentences=[]
        for i in self.lines:
            s=i
            check=set(s.split())
            if word in check:
                sentences.append(i)
        return sentences        


analyser = textAnalyzer("sample.txt")
print(analyser.wordcount)
print(analyser.line_count)
print(analyser.char_count)
print(analyser.most_common_words(3))
print(analyser.find_sentences_with("Python"))