import codecs
import argparse
from konlpy.tag import Kkma
from konlpy.utils import pprint

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


# 인코딩 방식
def read_sentence(file_name):
    e = get_encode(file_name)
    with open(file_name, 'rt', encoding= e) as f:
        return str(f.readline())

# N-gram 으로 음절 빈도 구하기
def syll_ngram(sentence, num_gram):
  # in the case a file is given, remove escape characters
  if(num_gram == 5):
      return syll_ngram(sentence,2) + syll_ngram(sentence,3)
  sentence = sentence.replace('\n', ' ').replace('\r', ' ')

  ngrams = [sentence[x:x+num_gram] for x in range(0, len(sentence))]

  return tuple(ngrams)

# N-gram 으로 공통 음절 빈도 조사
def count_common_syll_ngram(sentence, n, set_syl):
    cnt = 0
    ngrams = syll_ngram(sentence, n)
    for token in ngrams:
        if token in set_syl:
            cnt += 1
    return cnt


def count_common_syll_morp(long_kkma, short_kkma):
    cnt = 0
    set_short_kkma = set(short_kkma)

    for morp in long_kkma:
        if morp in set_short_kkma:
            cnt += 1
    return cnt


if __name__ == "__main__":
    # 파일경로
    path_file1 = "input1.txt"
    path_file2 = "input2.txt"
    # ngram 값
    n = 5
    # 문장 읽기
    short_line = read_sentence(path_file1)
    long_line = read_sentence(path_file2)

    # 짧은 문장 비교
    if len(short_line) > len(long_line):
        short_line, long_line = long_line, short_line

    print("입력 짧은 문장 : ", short_line)
    print("입력 긴   문장 : ", long_line)

    # 음절 집합 구하기기
    set_syl_short = set(syll_ngram(short_line, n))
    # 음절 개수 구하기
    cnt_syllToShort = len(syll_ngram(short_line, n))
    cnt_syllToCommon = count_common_syll_ngram(long_line, n, set_syl_short)
    # 음절 유사도 구하기
    similar_syll = (float)(cnt_syllToCommon/ cnt_syllToShort)

    
    # 형태소 분석 라이브러리 선언
    kkma = Kkma()
    # 형태소 분석
    short_kkma = list(kkma.morphs(short_line))
    long_kkma  = list(kkma.morphs(long_line))
    # 형태소 개수 구하기
    cnt_morpToShort = len(short_kkma)
    cnt_morpToCommon = count_common_syll_morp(long_kkma, short_kkma)
    # 형태소 유사도 계산
    similar_morp = (float)(cnt_morpToCommon/cnt_morpToShort)

    

    print('음절 N-gram 유사도 : {0:.3f}%'.format(similar_syll * 100))
    print('형태소 유사도 : {0:.3f}%'.format(similar_morp * 100))