from pywsd.lesk import simple_lesk  

sentences = ['I went to the bank to deposit my money',  
'The river bank was full of dead fishes']  

print ("Context-1:", sentences[0])  
answer = simple_lesk(sentences[0],'bank')  
print ("Sense:", answer)  
print ("Definition : ", answer.definition())

print ("\nContext-2:", sentences[1])  
answer = simple_lesk(sentences[1],'bank')  
print ("Sense:", answer)  
print ("Definition : ", answer.definition())