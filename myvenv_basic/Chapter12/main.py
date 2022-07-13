from calendar import different_locale
import os, csv
from post import Post
# 파일 경로
file_path = "./myvenv/Chapter12/data.csv"

# post 객체를 저장할 리스트
post_list = []


if os.path.exists(file_path):
    #pass
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf*")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)

else:
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()


#print(post_list[0].get_title())

# 게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""
    print("\n\n - 게시글 쓰기 -")
    title = input("제목을 입력 >>> ")
    content = input("내용 입력 >>> ")
    # 글 번호
    id = post_list[-1].get_id()+1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

# 게시글 목룍
def list_post():
    #print(post_list)
    print("\n\n - 게시글 목록 -")
    id_list = []
    for post in post_list:
        print("번호 : ", post.get_id())
        print("제목 : ", post.get_title())
        print("조회수 : ", post.get_view_count())
        print("")
        id_list.append(post.get_id())

    while True:
        print("Q) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력해주세요")
        try:
            id = int(input(">>> "))
            if id in id_list:
                #print("게시글 상세보기")
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요")

# 글 상세 페이지
def detail_post(id):
    """게시글 상세보기"""
    print("\n\n - 게시글 상세보기 -")

    for post in post_list:
        if post.get_id() == id:
            # 조쇠수 1증가
            post.add_view_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("본문 : ", post.get_content())
            print("조회수 : ", post.get_view_count())
            target_post = post
    while True:
        print("Q) 수정:1 삭제:2 (메뉴로 돌아가려면 -1을 입력")
        try:
            choice = int(input(">>> "))
            if choice == 1:
                #print("수정")
                update_post(target_post)
                break
            elif choice == 2:
                #print("삭제")
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요")

# 게시글 수정
def update_post(target_post):
    """게시글 수정 함수"""
    print("\n\n - 게시글 수정 - ")
    title = input("제목 입력 >>> ")
    content = input("본문 입력 >>> ")
    target_post.set_post(target_post.id, title, content, target_post.view_count)
    print("# 게시글이 수정되었습니다.")

# 게시글 삭제
def delete_post(target_post):
    """게시글 삭제 함수"""
    post_list.remove(target_post)
    print("# 게시글이 삭제되었습니다.")

# 게시글 저장
def save():
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count]
        writer.writerow(row)
    f.close()
    print("# 저장이 완료 되었습니다.")
    print("# 프로그램을 종료")


# 메뉴 출력하기
while True:
    print("\n\n- 메뉴를 선택해 주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input(">>> "))
    except ValueError as e:
        print("숫자를 입력해 주세요", e)
    else:
        if choice == 1:
            #print("게시글 쓰기")
            write_post()
        elif choice == 2:
            #print("2")
            list_post()
        elif choice == 3:
            save()
            #print("프로그램을 종료합니다.")
            break

