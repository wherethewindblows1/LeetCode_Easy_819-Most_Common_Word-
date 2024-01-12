from collections import *

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        #Sol 1-1) 
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)  #정규 표현식에서 *re.sub() 사용, ^\w -> 단어 문자가 아닌 모든 문자를 공백으로 치환.
            .lower().split()
                if word not in banned]  #banned에 포함되어 있지 않은 단어 선정.
        counts = collections.defaultdict(int)  #collections 모듈의 defaultdict을 사용하여 딕셔너리인 counts의 default 값이 0(int)이 되도록 만듦.
        for word in words:
            counts[word] += 1
        
        return max(counts, key=counts.get)  #max(counts, key=counts.get) 사용하여 key 값 추출. 


        #Sol 1-2)
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
        counts = collections.Counter(words) # collections 모듈의 Counter()를 사용하여, 값이 많이 나온 순서대로 정렬. 

        return counts.most_common(1)[0][0]  # collections 모듈의 most_common(1)을 사용하여, 가장 많이 나온 단어의 key 값 추출.
    
        '''
        So1 1-1)
        1. 정규 표현식에서 *re.sub() 사용, ^\w -> 단어 문자가 아닌 모든 문자를 공백으로 치환.
        2. collections 모듈의 defaultdict을 사용하여 딕셔너리인 counts의 default 값이 0(int)이 되도록 만드는 딕셔너리 사용 
        3. max(counts, key=counts.get) 사용하여 key 값 추출. 
        
        Sol 1-2)
        1. 정규 표현식에서 *re.sub() 사용, ^\w -> 단어 문자가 아닌 모든 문자를 공백으로 치환.
        2. collections 모듈의 Counter()를 사용하여, 값이 많이 나온 순서대로 정렬. 
        3. collections 모듈의 most_common(1)을 사용하후, 인덱싱([0][0])하여 가장 많이 나온 단어의 key 값 추출.
        '''









        

         
