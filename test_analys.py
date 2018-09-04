def answer_reducer(user_answer):
    result = {
        'rivalry': 0,
        'cooperation': 0,
        'compromise': 0,
        'avoidance': 0,
        'adjustment': 0
    }

    key_test = {
        'rivalry': ['3А', '6В', '8А', '9В', '10А', '13В', '14В', '16В', '17А', '22В', '25А', '28А'],
        'cooperation': ['2В', '5А', '8В', '11А', '14А', '19А', '20А', '21В', '23В', '26В', '28В', '30В'],
        'compromise': ['2А', '4А', '7В', '10В', '12В', '13А', '18В', '22А', '23А', '24В', '26А', '29А'],
        'avoidance': ['1А', '5В', '6А', '7А', '9А', '12А', '15В', '17В', '19В', '20В', '27А', '29В'],
        'adjustment': ['1В', '3В', '4В', '11В', '15А', '16А', '18А', '21А', '24А', '25В', '27В', '30А']
    }

    for answer in user_answer:
        for scale in key_test:
            if answer in key_test[scale]:
                result[scale] += 1

    return result


def user_result(test_result, test_reducer):
    result = test_reducer(test_result)
    result_sorted = []
    scale_sorted = []
    result_sort_value = []
    for values in sorted(result.values(), reverse=True):
        for key in result:
            if result[key] == values and key not in result_sort_value:
                result_sorted.append(values)
                result_sort_value.append(key)
                if key == 'rivalry':
                    scale_sorted.append('соперничество')
                if key == 'adjustment':
                    scale_sorted.append('приспособление')
                if key == 'compromise':
                    scale_sorted.append('компромисс')
                if key == 'cooperation':
                    scale_sorted.append('сотрудничество')
                if key == 'avoidance':
                    scale_sorted.append('избегание')

    conclusion = 'По результатам тестирования можно говорить о следующем:\n' \
                 'Максимальный бал был набран по шкале "{}" - {}\n' \
                 'По шкале "{}" набрано - {} баллов\n' \
                 'По шкале "{}" - {}, по шкале "{}" - {}\n' \
                 'Минимальный бал был набран по шкале "{}" - {}'.format(
                  scale_sorted[0], result_sorted[0],
                  scale_sorted[1], result_sorted[1],
                  scale_sorted[2], result_sorted[2],
                  scale_sorted[3], result_sorted[3],
                  scale_sorted[4], result_sorted[4])

    return conclusion
