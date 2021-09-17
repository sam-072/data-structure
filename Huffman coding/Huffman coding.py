import heapq
import os
class BinaryNode:
    def __init__(self,value,freq):
        self.value=value
        self.frequency=freq
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
        self.__codes = {}
        self.__revCodes = {}
    
    def __frequency(self,text):
        d=dict()
        for i in text:
            d[i]=d.get(i,0)+1
        return d
    
    def __buildHeap(self,freq):

        for i in freq:
            newnode=BinaryNode(i, freq[i])
            heapq.heappush(self.__heap,newnode)
    
    def __buildTree(self):
        while len(self.__heap) > 1:
            node1=heapq.heappop(self.__heap)
            node2=heapq.heappop(self.__heap)
            newnode=BinaryNode(None, node1.frequency + node2.frequency)
            newnode.left=node1
            newnode.right=node1
            heapq.heappush(self.__heap, newnode)
        return 

    def __buildCodes(self):
        root=heapq.heappop(self.__heap)
        self.__buildCodesHealper(root,"")
    
    def __buildCodesHelper(self,root,curr_bits):
        if root is None:
            return
        
        if root.value is not None:
            self.__codes[root.value] = curr_bits
            self.__revCodes[curr_bits] = root.value
            return
        
        self.__buildCodesHelper(root.left, curr_bits+'0')
        self.__buildCodesHelper(root.right, curr_bits+'1')

    def __getEncodedText(self,text):
        encoded_text=""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text

    def __getPaddedText(self,encodedText):
        padded_amount = 8 - (len(encodedText) % 8)

        for i in range(padded_amount):
            encodedText+='0'
        padded_info = "{0:08b}".format(padded_amount)
        paddedText = padded_info + encodedText
        return paddedText
        
    def __byteArray(self,paddedText):
        l=[]
        for i in range(0,len(paddedText),8):
            byte = paddedText[i:i+8]
            l.append(int(byte,2))
        return l 

    def compress(self):
        # get file from path
        # read text from file
        file_name , file_ext = os.path.splitext(self.path)
        output_path = file_name + ".bin"

        with open( self.path,'r+') as file , open(output_path,'wb') as output:
            text = file.read()
            text = text.rstrip()
            
        # make frequency dict using the text
        freq_dict=self.__frequency(text)

        # construct the heap from the frequency dictionary
        self.__buildHeap(freq_dict)

        # construct the binary tree from the heap
        self.__buildTree()

        # constrcut the codes from binary tree
        self.__buildCodes()

        # Creating the encoded text using the codes
        encoded_text = self.__getEncodedText(text)

        # put this encoded text into the binary file

        # pad this encoded text into the binary file
        padded_text = self.__getPaddedText(encoded_text)
        byte_array=self.__byteArray(padded_text)
        finalByte = bytes(byte_array)
        output.write(finalByte)
        
        # return this binary file as output
        print("compressed")
        return output_path
    
    def __removePadding(self,text):
        padding_info = text[:8]
        padding_amount = int(padding_info,2)

        # remove padding info from text
        text = text[8:]
        
        # remove padding amount from text
        text = text[:-1*padding_amount]

        return text

    def __decodeText(self,text):
        curr_bits = ""
        decodedText = ""
        for i in text:
            curr_bits += i
            if curr_bits  in self.__revCodes:
                decodedText += self.__revCodes[curr_bits]
                curr_bits = ""
        return decodedText

    def decompress(self,input_path):
        file_name , file_ext = os.path.splitext(self.path)
        output_path = file_name + "decompressed" + ".txt"
        with open(input_path,'rb') as file , open(output_path,'w') as output:
            bit_string = ""
            byte = file.read(1)
            while byte :
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)
            actualText = self.__removePadding(bit_string)
            text = self.__decodeText(actualText)
            output.write(text)
        return

        

if __name__=='__main__':
    path = 'D:\download\Output'
    d=Huffman(path)
    d.compress()