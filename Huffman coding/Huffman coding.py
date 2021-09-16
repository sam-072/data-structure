import heapq

class BinaryNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None
    
    def __lt__(self,other):
        return self.frequency < other.frequency

    def __eq__(self,other):
        return self.frequency == other.frequency

class Huffman:
    def __init__(self,path):
        self.path = path
        self.__heap = []
    
    def __frequency(self,text):
        d=dict()
        for i in text:
            d[i]=d.get(i,0)+1
        return d
    
    def __buildHeap(self,freq):

        for i in freq:
            newnode=BinaryNode(i, freq[i])
            heapq.push(self.__heap,newnode)
    
    def comress(self):
        # get file from path
        # read text from file
        text="hvaskassdasgdajbaskj"

        # make frequency dict using the text
        freq_dict=self.__frequency(text)

        # construct the heap from the frequency dictionary
        self.__buildHeap(freq_dict)

        # construct the binary tree from the heap

        # constrcut the codes from binary tree

        # Creating the encoded text using the codes

        # put this encoded text into the binary file





if __name__=='__main__':
    s="sadasjsdgasskdasjha"
    d=Huffman("path")
    # print(d.frequency(s))