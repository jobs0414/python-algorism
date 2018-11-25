s = "when I was young, I live in new york" 

letter = input("검색할 알파벳을 입력해주세요.")

if letter in s: 
    print("문자를 찾았다.",letter )

else: 
    print("그러한 문자는 없습니다.")