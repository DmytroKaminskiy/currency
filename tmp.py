# gunicorn -w 4 --bind 0.0.0.0:8000 settings.wsgi

# from time import sleep
#
# CACHE = {}
#
#
# def foo(a, b):
#
#     key = f'{a}_{b}'
#
#     if key in CACHE:
#         print('FROM CACHE')
#         return CACHE[key]
#     else:
#         print('NOT IN CACHE')
#         result = a * b
#         sleep(3)
#         CACHE[key] = result
#         return result
#
# print(foo(2, 2))
# print(foo(2, 3))

# KEY = 2
#
#
# def crypt(password):
#     return ''.join([chr(ord(c) + KEY) for c in password])
#
#
# def decrypt(password):
#     return ''.join([chr(ord(c) - KEY) for c in password])
#
# assert crypt('Dima') == 'bcde'

# import xlsxwriter
#
# # Create an new Excel file and add a worksheet.
# workbook = xlsxwriter.Workbook('demo.xlsx')
# worksheet = workbook.add_worksheet()
# # Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)
# # Write some simple text.
# worksheet.write('A1', 'Hello')
# workbook.close()

# docker exec -it backend pytest ./src/tests --cov=src --cov-report html
# docker exec -it backend pytest ./src/tests --cov=src --cov-report html --cov-fail-under=58.00

# pip list --outdated
# https://github.com/pytest-dev/pytest-cov
# https://github.com/DmytroKaminskiy/currency_exchange/commit/8218d47bcf4ed752fc1bff6964d0c3ea1a160916
# https://github.com/DmytroKaminskiy/currency_exchange/commit/2f79fca5ec8b2024806c150873d22a00e331bf6e

# use bootstrap pagination!
# GO to page "form"
# pagination for API
# add filters to API
