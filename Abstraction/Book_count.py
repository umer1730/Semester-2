class Document:
    book_count = 0
    def __init__(self,text):
        self.text = text
        Document.book_count += 1
    
    def get_alpha_count(self): 
        letters = []
        for ch in self.text:
            if ch.isalpha():
                letters.append(ch)
        return len(letters)
   
    @classmethod
    def from_non_string(cls,data):
        return cls(str(data))
    
d1 = Document("hello i am the only man who discover the python")
d2 = Document.from_non_string(12345)
d3 = Document.from_non_string(["A", "B", "C"])
print(d1.get_alpha_count())    
print(d2.get_alpha_count())    
print(d3.get_alpha_count())    


