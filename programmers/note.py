def solution(id_list, report, k):
    answer = []
    reporter = []
    reported = []

    report = list(set(report))

    for i in report:
        tmp_split = i.split(' ')
        reporter.append(tmp_split[0])
        reported.append(tmp_split[1])

    # print('신고자 :', reporter)
    # print('범죄자 :', reported)

    id_list_cnt = []
    for i in range(len(id_list)):
        id_list_cnt.append(0)

    for i in range(len(id_list)):
        for j in reported:
            if id_list[i] == j:
                id_list_cnt[i] += 1

    # print('id_list :', id_list)
    # print('id_list_cnt :', id_list_cnt)

    mail_cnt = []
    for i in range(len(id_list)):
        mail_cnt.append(0)

    for i in range(len(id_list_cnt)):
        tmp_criminal = ''
        if id_list_cnt[i] >= k:
            tmp_criminal = id_list[i]
            for j in range(len(reported)):
                if reported[j] == tmp_criminal:
                    # print(reporter[j], id_list.index(reporter[j]))
                    mail_cnt[id_list.index(reporter[j])] += 1

    answer = mail_cnt
    return answer




id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))