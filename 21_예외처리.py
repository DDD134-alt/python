
while True:
    try:
        print("나눗셈 계산기 입니다.")
        num1 = int(input("첫 번째 숫자 입력 : "))
        num2 = int(input("두 번째 숫자 입력 : "))
        print(f"{num1} / {num2} = {int(num1 / num2)}")

    # except ValueError : (값 에러 처리)
    # 숫자가 들어와야 할 자리에 숫자 외 문자같은 잘못된 형식의 값이 입력될때 예외처리
    except ValueError:
        print("에러!!! 잘못된 값을 입력 하였습니다.")
        continue

    # except ZeroDivisionError as err : (0으로 나누기 에러 처리)
    # 0으로 나눠야 할때(영원히 구할 수 없는 값을 구해야 할때) 발생하는 에러를 예외처리
    except ZeroDivisionError as err:
        print("에러!!! 0으로 숫자를 나눌 수 없습니다!")
        continue

    # except Exception as err : (최종 에러 방어선)
    # 개발자가 예상하지 못한 종류의 에러가 발생했을 때 처리해 주는 최전선 만능 예외 처리기
    except Exception as err:
        print(err)
        continue

    else:
        print("정상 처리 되었습니다.")
        break

    # finally : (무조건 실행)
    # 에러가 발생했든, 정상 처리되었든 상관없이 프로그램 맨 마지막에 무조건 실행됩니다.
    # 파일 닫기, DB 연결 종료 등 반드시 마무리 지어야 하는 정리 작업을 넣을 때 사용합니다.
    finally:
        print("프로그램 실행 완료!!")


# 천 번의 실행 중 한 번 일어나는, 뭐땜시 발생하는지 모르겠는 버그...
# 그 버그의 원인을 찾을 수 없다면 차라리 아예 문제를 재현해 버린다!
# 그리고 그 문제의 원인을 찾는다!
# 그것이 버그를 수월하게 찾을 수 있는 방법.
# 버그 재현(Bug Reproduction)
# 원인을 알 수 없는 간헐적 버그는, 버그가 무조건 발생하는 규칙/조건을 찾아내야만
# (문제 발생 상황을 재현해야만) 비로소 원인을 찾고 고칠 수 있다.

# 따라서 아래와 같이 없으면 없는데로 그냥 넘어가는, 문제를 회피하는 코딩은 지양하는게 좋다.

try:
    score_file = open("1score.txt", "r", encoding="utf-8") # 해당 파일이 없으면 에러가 발생하지만 이 경우는 그냥 지나 감.
    print(score_file.read())
    score_file.close()
except FileNotFoundError:
    pass
