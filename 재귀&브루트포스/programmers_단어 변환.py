def solution(begin, target, words):
    answer = 0
    Q = [begin]
    
    while True:
        temp_Q = []
        for Q_word in Q:
            # target에 도달할 경우
            if Q_word == target:
                return answer
            
            # words 끝에서 부터 거꾸로 검색
            # 거꾸로 검색하는 이유는 temp_Q에 담아줄 때 word에서 삭제해야하는데 거꾸로 해야 index 가 꼬이지 않기 때문
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                
                # 큐에 담아준 word와 words의 단어중 하나라도 알파벳이 같다면 temp_Q에 담아주고 words에서 pop
                if sum([x != y for x, y in zip(Q_word, word_2)]) == 1:
                    temp_Q.append(words.pop(i))
        
        # temp_Q에 아무것도 없다면 변환 가능한 단어가 없다는 뜻이므로 return 0
        if not temp_Q:
            return 0
        
        Q = temp_Q
        answer += 1