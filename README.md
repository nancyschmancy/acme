# Acme Insurance API
Acme Insurance API is simple API which creates personalized insurance quotes.

To run this API, you will need Python 3.10 and virtualenv.
## Installation
1.  Unzip the Acme Insurance project. Within the project root, create a virtualenv and activate.
    ```
    python3 -m virtualenv venv
    source venv/bin/activate
    ```
2. Install requirements.
    ```
    pip install -r requirements.txt
    ```
3. Perform database migration
    ```
    python3 manage.py migrate
    ```
4. Create your login. Once prompted, enter your desired username, and password.
    ```
    python3 manage.py createsuperuser
    ```
5. You're now ready to roll! Run server:
    ```
    python3 manage.py runserver
    ```

## Basic Usage
In order for a new quote to be generated, the following information must be provided in the Quote object:
```
effective_date = date (formatted 'YYYY-MM-DD')
has_cancelled = bool
owns_property = bool
state = string
zip_code = string (formatted XXXXX or XXXXX-XXXX)
```
### API Endpoints
| HTTP | Endpoints | Action |
| --- | --- | --- |
| GET | /api/quote/ | Retrieve all quotes |
| POST | /api/quote/ | Create a new quote |
| GET | /api/quote/:id | Retrieve quote details |
#### GET /api/quote/
```
curl -i -H 'Accept: application/json' http://localhost:8000/api/quote/
```
**Example Response**
```
[
    {
        "id": "QTPzxxMlqZ",
        "total_term_premium": "68.93",
        "total_term_discounts": "0.00",
        "total_term_fees": "8.99",
        "total_monthly_premium": "11.49",
        "total_monthly_discounts": "0.00",
        "total_monthly_fees": "1.50",
        "effective_date": "2022-03-13",
        "has_cancelled": true,
        "owns_property": false,
        "state": "MT",
        "zip_code": "00303",
        "base_premium": "59.94",
        "cancelled_fee": "8.99",
        "volcano_fee": "0.00",
        "not_cancelled_discount": "0.00",
        "ownership_discount": "0.00"
    },
    {
        "id": "GWuitoucr5",
        "total_term_premium": "71.92",
        "total_term_discounts": "-11.99",
        "total_term_fees": "23.97",
        "total_monthly_premium": "11.99",
        "total_monthly_discounts": "-2.00",
        "total_monthly_fees": "4.00",
        "effective_date": "2000-05-30",
        "has_cancelled": true,
        "owns_property": true,
        "state": "CA",
        "zip_code": "2323",
        "base_premium": "59.94",
        "cancelled_fee": "8.99",
        "volcano_fee": "14.98",
        "not_cancelled_discount": "0.00",
        "ownership_discount": "-11.99"
    }
]
```
#### POST /api/quote/
**Example Request**
```
{
	"effective_date": "2022-03-13",
	"state": "montana",
	"has_cancelled": true,
	"owns_property": false,
	"zip_code": "00303"
}
```
**Example Response**
```
{
    "id": "QTPzxxMlqZ",
    "total_term_premium": "68.93",
    "total_term_discounts": "0.00",
    "total_term_fees": "8.99",
    "total_monthly_premium": "11.49",
    "total_monthly_discounts": "0.00",
    "total_monthly_fees": "1.50",
    "effective_date": "2022-03-13",
    "has_cancelled": true,
    "owns_property": false,
    "state": "MT",
    "zip_code": "00303",
    "base_premium": "59.94",
    "cancelled_fee": "8.99",
    "volcano_fee": "0.00",
    "not_cancelled_discount": "0.00",
    "ownership_discount": "0.00"
}

```
#### GET /api/quote/:id
```
curl -i -H 'Accept: application/json' http://localhost:8000/api/quote/QTPzxxMlqZ/
```
**Example Response**
```
{
    "id": "QTPzxxMlqZ",
    "total_term_premium": "68.93",
    "total_term_discounts": "0.00",
    "total_term_fees": "8.99",
    "total_monthly_premium": "11.49",
    "total_monthly_discounts": "0.00",
    "total_monthly_fees": "1.50",
    "effective_date": "2022-03-13",
    "has_cancelled": true,
    "owns_property": false,
    "state": "MT",
    "zip_code": "00303",
    "base_premium": "59.94",
    "cancelled_fee": "8.99",
    "volcano_fee": "0.00",
    "not_cancelled_discount": "0.00",
    "ownership_discount": "0.00"
}
```

## Tests
To run the test suite, run the following command:
```
python3 manage.py test
```
