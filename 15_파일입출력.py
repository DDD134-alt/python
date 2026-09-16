# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학: 45", file=score_file)
# print("영어: 55", file=score_file)
# score_file.write("과학: 88\n")
# score_file.write("코딩: 100\n")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())    # 파일 전체 내용을 읽어 하나의 문자열로 반환
score_file.close()


score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline() # 한줄씩 읽기
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # 전체를 다 읽기. 이게 좀 더 나음
for line in lines:
    print(line, end="")
score_file.close()