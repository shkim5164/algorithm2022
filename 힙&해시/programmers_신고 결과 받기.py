def solution(id_list, report, k):
    answer = [0 for i in id_list]
    set_report = set(report)
    id_cnt = {user_id: [index, []] for index, user_id in enumerate(id_list)}
    
    for report in set_report:
        split_report = report.split()
        user_id = split_report[0]
        report_id = split_report[1]
        id_cnt[report_id][1].append(user_id)
    
    for key, value in id_cnt.items():
        report_list = value[1]
        if len(report_list) >= k:
            for report_id in report_list:
                index = id_cnt[report_id][0]
                answer[index] += 1
    return answer