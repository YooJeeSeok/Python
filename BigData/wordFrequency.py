import operator
import re
import time
import codecs

def hangul(text):
    text = re.sub(u'[^\u3130-\u318F\uAC00-\uD7A3]', '', text)
    return text

def get_encode(file):
        encodings = ['utf-16', 'utf-8', 'euc_kr', 'cp949']
        for e in encodings:
            try:
                fh = codecs.open(file, 'r', encoding=e)
                fh.readlines()
                fh.seek(0)

            except UnicodeDecodeError:
                pass
            except UnicodeError:
                pass
            else:
                return e
        return ''

if __name__ == "__main__":

    # file_name = 'test_UTF8.txt'
    file_name = 'test28_EUCKR.txt'

    word_freq = {}
    start = time.time()
    encode = get_encode(file_name)

    with open(file_name,encoding=encode) as f:
        while True:
            data = f.read(1024)

            if not data:
                break

            for word in data.split(' '):
                word = re.sub(u'[^a-zA-Z\u3130-\u318F\uAC00-\uD7A3]', '', word)
                if word =='':
                    continue
                count = word_freq.get(word, 0)
                word_freq[word] = count+1
    end = time.time()
    word_freq = sorted(word_freq.items(), key=operator.itemgetter(1),reverse=True)

    word_freq =dict(word_freq[:20])
    for word in word_freq:
        print(f'{word_freq[word]} : {word}')


    print(f'{end - start} seconds')
