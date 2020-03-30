import re
from argparse import ArgumentParser


def read_sentence(file_name):
    with open(file_name) as f:
        return str(f.readline())

# 특수 문자 및 문자 부호 삭제
def hangul(text, mark=False):
    if not mark:
        return re.sub(u'[^a-zA-Z\u3130-\u318F\uAC00-\uD7A3]', '', text)

def hangulMark(text):
    word = re.sub(u'[^a-zA-Z\u3130-\u318F\uAC00-\uD7A3]', '', text)
    return word

def count_word(sentence):
    cnt = len(sentence.split(' '))
    return cnt

# 음절 개수
def count_syll(sentence):
    sentence = hangul(sentence)
    return len(sentence)

# 음절 분석
def get_syl_set(sentence):
    sentence = hangul(sentence) # 문자 부호 삭제
    set_syl = set(''.join(sentence.split()))
    return set_syl


def get_word_set(sentence):
    set_word = set(map(hangulMark, sentence.split(' ')))
    return set_word


def count_common_syll(sentence, set_syl):
    cnt = 0
    for ch in sentence:
        if ch in set_syl:
            cnt += 1
    return cnt

def count_common_word(sentence, set_word):
    cnt = 0

    for word in sentence.split(' '):
        word = hangulMark(word)

        if word in set_word:
            cnt += 1

    return cnt
# 어절 개수 구하기

# 공통 음절 개수 구하기


if __name__ == "__main__":
    parser = ArgumentParser()

    # 파일경로
    path_file1 = "input1.txt"
    path_file2 = "input2.txt"

    # 문장 읽기
    short_line = read_sentence(path_file1)
    long_line = read_sentence(path_file2)

    # 짧은 문장 비교
    if len(short_line) > len(long_line):
        short_line, long_line = long_line, short_line

    print("입력 짧은 문장 : ", short_line)
    print("입력 긴   문장 : ", long_line)

    # 음절 집합 구하기기
    set_syl_short = get_syl_set(short_line)
    # 음절 개수 구하기
    cnt_syllToShort = count_syll(short_line)
    cnt_syllToCommon = count_common_syll(long_line, set_syl_short)
    # 음절 유사도 구하기
    similar_syll = (float)(cnt_syllToCommon/ cnt_syllToShort)

    # 어절 집합 구하기
    set_word_short = get_word_set(short_line)
    # 어절 개수 구하기
    cnt_wordToShort = count_word(short_line)
    cnt_wordToCommon = count_common_word(long_line, set_word_short)
    # 어절 유사도 구하기
    similar_word = (float)(cnt_wordToCommon/cnt_wordToShort)

    print(f'공통 음절 개수 : {cnt_syllToCommon}')
    print(f'공통 어절 개수 : {cnt_wordToCommon}')

    print('음절 유사도 : {0:.3f}'.format(similar_syll*100))
    print('어절 유사도 : {0:.3f}'.format(similar_word*100))






