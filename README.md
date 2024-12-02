# Django_yfinance

This is a backend application developed using Python and the Django framework. The core functionality of the application involves fetching currency exchange rate data from Yahoo Finance and storing it in a local MSQL database.

The app is structured around a RESTful API, enabling efficient interaction with the stored data. Key endpoints allow users to:

Retrieve a list of available currencies.

![currency](https://github.com/user-attachments/assets/5e66ba27-33bf-4892-811c-2feaf233f2f3)

Fetch currency pairs based on a base currency.

![currency_aaa](https://github.com/user-attachments/assets/2b503421-293a-4f78-ba67-8dd52e2b8808)

Access the latest exchange rate for specific currency pairs.

![curr_bbb_aaa](https://github.com/user-attachments/assets/25cdbcb4-56d7-4a55-ade5-f6b224d52570)
![curr_aaa_bbb](https://github.com/user-attachments/assets/ae8b0e84-0fd1-411e-9c11-336a90e7ed64)

ADMIN 
Database structure listing Unique values.

![currency_list](https://github.com/user-attachments/assets/8ad92b6b-aa4e-4449-97b4-9df8a00adea3)
![currpairs](https://github.com/user-attachments/assets/0aa54e39-7440-4cd0-9d07-ab187bbd0ec8)

For each currency pair, maintain a record of historical exchange rates along with the timestamp indicating when each rate was retrieved.

![admin_history](https://github.com/user-attachments/assets/612c8203-07b9-410f-a8bc-f1d81aa0572e)
