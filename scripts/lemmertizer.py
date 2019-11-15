from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#import nltk
#nltk.download('wordnet')

wordnet_lemmatizer = WordNetLemmatizer()
def lemmatize(sentence):
    punctuations="?:!.,;"
    sentence_words = word_tokenize(sentence)
    for word in sentence_words:
        if word in punctuations:
            sentence_words.remove(word)

    refined_words = []
    for word in sentence_words:
        if word == '\'ll':
            refined_words.append('will')
        elif word == '\'m':
            refined_words.append('am')
        elif word == '\'d':
            refined_words.append('should') 
            refined_words.append('had') 
            refined_words.append('would') 
            refined_words.append('could')
        elif word == '\'s':
            refined_words.append('is') 
            refined_words.append('\'s')
        elif word == '\'ve':
            refined_words.append('have')
        elif word == 'in\'':
            refined_words.append('ing')
        elif word == 'n\'t':
            refined_words.append('not')
        else:
            refined_words.append(wordnet_lemmatizer.lemmatize(word, pos='v'))
    result_sentence = ' '.join(refined_words)

    return result_sentence