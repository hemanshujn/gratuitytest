# excel_writer.py

from openpyxl import Workbook
from io import BytesIO

def generate_excel(ages, service, salary, gratuity, discount, pv):

    wb = Workbook()
    ws = wb.active
    ws.title = "Gratuity Projection"

    ws.append(["Age", "Service", "Salary", "Gratuity", "Discount Factor"])

    for i in range(len(ages)):
        ws.append([
            int(ages[i]),
            round(service[i], 2),
            round(salary[i], 2),
            round(gratuity[i], 2),
            round(discount[i], 6)
        ])

    ws.append([])
    ws.append(["Present Value", round(pv, 2)])

    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return file_stream