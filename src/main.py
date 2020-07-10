import datetime
from typing import List


def string_comma_to_list(message: str) -> List[str]:
    return message.split(',') if message else []

if __name__ == "__main__":


    my_dic = {
        "key1": f"value1",
        "key2": f"value2"
    }
    print(my_dic["key1"])
    for key in my_dic.keys():
        print("KEY:" + key)

    for value in my_dic.values():
        print("VALUE: " + value)

    for k, v in my_dic.items():
        print('Key: ' + k + ' --- Value: ' + v)
        if k == 'key1':
            #del my_dic[k]
            print(k + ' Deleted')

    print(len(my_dic))

    today = datetime.datetime.today()
    print(f"{today:%B %d, %Y}")