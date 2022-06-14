import approx as ap

if __name__ == '__main__':
    func = [[1.2, 2.9, 4.1, 5.5, 6.7, 7.8, 9.2, 10.3],
            [7.4, 9.5, 11.1, 12.9, 14.6, 17.3, 18.2, 20.7]]

    func1 = [[1.1, 2.3, 3.7, 4.5, 5.4, 6.8, 7.5],
             [2.5, 4.1, 5.2, 6.9, 8.3, 14.8, 21.2]]

    approx = [
        'линейная',
        'квадратичная',
        'кубическая',
        'экспоненциальная',
        'логарифмическая',
        'степенная'
    ]

    lin_approx, lin_app_func, lin_e_arr, lin_p_arr, lin_sko = ap.linear_approx(func)
    quad_approx, quad_app_func, quad_e_arr, quad_arr, quad_sko = ap.quad_approx(func)
    qubic_approx, qubic_app_func, qubic_e_arr, qubic_p_arr, qubic_sko = ap.qubic_approx(func)
    exp_approx, exp_app_func, exp_e_arr, exp_p_arr, exp_sko = ap.exp_approx(func)
    log_approx, log_app_func, log_e_arr, log_p_arr, log_sko = ap.log_approx(func)
    pow_approx, pow_app_func, pow_e_arr, pow_p_arr, pow_sko = ap.pow_approx(func)

    sko_arr = [lin_sko, quad_sko, qubic_sko, exp_sko, log_sko, pow_sko]
    min_sko, idx_sko = min((val, idx) for (idx, val) in enumerate(sko_arr))
    print(f'Лучшая аппроксимация: {approx[idx_sko]}')
    print(f'СКО = {round(min_sko, 3)}')

