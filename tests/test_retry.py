# ！/usr/bin/python
import time

TIMES = 3


def brand_name_for_partner(partner_id: str) -> str:
    """
    Finds the brand name for the given partner ID
    :param partner_id: The partner ID for which we're looking for its brand name
    :return: The brand name of the partner ID
    """
    try_time = 1
    result = partner_id
    while try_time <= TIMES:
        print('try_time=', try_time)
        try:
            if try_time < 3:
                raise Exception('hhhhhh')
            else:
                result = 'OK'
                break
        except ValueError:
            print('Value Error')
        except Exception as e:
            print(str(e))
            time.sleep(1)
        finally:
            try_time += 1
        return result


print(brand_name_for_partner('not ok'))
