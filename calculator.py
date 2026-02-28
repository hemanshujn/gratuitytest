# calculator.py

import numpy as np

def run_projection(current_age, current_salary, current_service,
                   retirement_age=60,
                   salary_growth=0.05,
                   discount_rate=0.07):

    years = retirement_age - current_age + 1

    ages = np.arange(current_age, retirement_age + 1)

    service_vector = current_service + (ages - current_age)

    salary_vector = current_salary * ((1 + salary_growth) ** (ages - current_age))

    factor = 15 / 26
    gratuity_vector = factor * salary_vector * service_vector

    discount_vector = 1 / ((1 + discount_rate) ** (ages - current_age))

    # Present value using matrix multiplication
    pv = np.matmul(gratuity_vector, discount_vector)

    return ages, service_vector, salary_vector, gratuity_vector, discount_vector, pv