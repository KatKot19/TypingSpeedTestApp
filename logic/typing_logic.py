class TypingLogic:

    def __init__(self):

        pass

    def calculate_wpm(self,typed_text,elapsed_time):

        words=typed_text.split()
        num_words=len(words)
        minutes=elapsed_time/60

        if minutes == 0 :
            return 0

        wpm=num_words/minutes

        return wpm


    def calculate_accuracy(self,typed_text,target_text):

        if not target_text:
            return 0

        correct_chars=0
        for typed_char,target_char in zip(typed_text,target_text):
            if typed_char==target_char:
                correct_chars +=1

        accuracy = (correct_chars/max(len(target_text),1))*100
        return accuracy