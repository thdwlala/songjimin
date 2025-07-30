
#괄호 짝 검사


def check_brackets(text):
    stack =[]

    #문자열 내용 체크
    for char in text:
        print(char,end =" ")
    
        #만약, 문자열 괄호가 사용되면, 스펙에 추가
        if char in "({[":
            stack.append(char)
            print(f"stack = {stack}")

        elif char in ")}]":
            # 예외1) 닫는 괄호가 남아있는데 스텍이 비었다면?
            if not stack:
                return False

            top = stack.pop()
            print(top)
            print(f"stack = {stack}")

            #예외2) 괄호의 모양이 일치하지 않는 경우
            if (char ==")" and top != "(" ) or\
                (char =="}" and top != "{" ) or\
                (char =="]" and top != "[" ):
                return False

    #"스택에 데이터 유무 확인"
    return len(stack) == 0 #True
#마지막에 데이터가 남아있지 않으면 괄호가 매칭이 안된것

print(check_brackets("(a+b)"))
print(check_brackets("(a+b])"))
print(check_brackets("[(a+b})]"))
print(check_brackets("[(a+b}]"))
print(check_brackets("a+b"))