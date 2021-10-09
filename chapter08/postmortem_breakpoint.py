import math

def compute_rmse(observed, ideal):
    total_err_2 = 0
    count = 0
    for got, wanted in zip(observed, ideal):
        err_2 = (got - wanted) ** 2
        if err_2 >= 1:
            breakpoint()
        total_err_2 += err_2
        count += 1

    mean_err = total_err_2 / count
    rmse = marth.sqrt(mean_err)
    return rmse

result = compute_rmse([1.8, 1.7, 3.2, 7j])
print(result)

