


def revword(word:str) -> str:

   i= len(word)
   n_str= ""   
   for b in word:
        i=i-1
        n_str= n_str+ word[i]
        
   return n_str.lower()


def countword()->int:

    
    file= open('text.txt')
    first_line = file.readline()
    count=0
    for line in file:
        line=line.rsplit()
        
        # reading each word        
        for word in line:
            
            word= revword(word)
            
            if  word in first_line:
                count= count+1
    return(count)
