def init_list(size: int) -> tuple[list, list]:
    return [0 if idx % 2 == 0 else 1 for idx in range(size)], [0 if idx % 2 == 1 else 1 for idx in range(size)]


def diff_list(arr1: list, arr2: list) -> int:
    return sum(1 for idx in range(len(arr1)) if arr1[idx] != arr2[idx])


def min_coin_swap(arr: list) -> int:
    if set(arr) != {0, 1}:
        raise ValueError('input list must only contain ones and zeros')

    zero_start_list, one_start_list = init_list(len(arr))

    return min(diff_list(arr, zero_start_list), diff_list(arr, one_start_list))


if __name__ == '__main__':

    INPUT = [1, 1, 0, 1, 0, 1, 1]

    print(f'input:           {INPUT}')
    print(f'min coin swap:   {min_coin_swap(INPUT)}')
