def solution(string):
    if len(string) != 0:
        container_text = []
        for i in reversed(range(len(string))):
            container_text.append(string[i])
        return "".join(container_text)
    else:
        return ''

print(solution("good"))