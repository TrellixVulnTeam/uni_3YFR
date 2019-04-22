# -*- coding: utf-8 -*-


def inventory_management(R, T, C1, C2):
    """
    :param R: Количество продукции R в период времени T
    :param T: Период времени T в месяцах
    :param C1: Стоймость производства партии продукции C1
    :param C2: Стоймость хранения единицы продукции в месяц C2

    Пусть:
        n - размер партии, t - интервал выпуска партии.

    Тогда:
        t = T * n / R.

    Затраты на хренение продукции для интервала t:
        cs = n / 2 * C2 * t.

    Общая стоймость продукции для интервала t:
        q = (n / 2 * C2 * t) + C1

    Общая стоймость продукции для времени T:
        Q = R / n * ((n / 2 * C2 * t) + C1);
        Q = R / n * ((n / 2 * C2 * T / R) + C1);
        Q = (C2 * T * n / 2) + (C1 * R / n).

    Определяем оптимальный размер партии через минимум функции:
        dQ/dn = (C2 * T / 2) - (C1 * R / n^2);
        (C2 * T / 2) - (C1 * R / n0^2) = 0;
        C1 * R / n0^2 = C2 * T / 2;
        n0^2 = (C1 * R * 2) / (C2 * T);
        n0 = ((C1 * R * 2) / (C2 * T)) ** 0.5.

    Определяем интервыл выпуска партии:
        t0 = T * n0 / R.

    :return: n0: оттимальный размер партии, t0 - оптимальный интервал выпуска партии
    """
    n0 = ((2 * R * C1) / (T * C2)) ** 0.5
    t0 = (T * n0) / R
    return n0, t0


if __name__ == '__main__':
    data = dict(R=24000, T=12, C1=350, C2=0.1)
    n0, t0 = inventory_management(**data)
    print('Отпимальный размер партии: {} единиц.'.format(int(n0)))
    print('Оптимальный интервал выпуска: {:.3} месяца.'.format(t0))