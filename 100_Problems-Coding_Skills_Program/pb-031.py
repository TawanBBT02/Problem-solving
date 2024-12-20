def highest_sales_country(sales:dict[str,int])->tuple[str,int]:
    highest_sales_country = max(sales_data, key=sales.get)
    highest_sales_value = sales_data[highest_sales_country]
    return highest_sales_country,highest_sales_value

sales_data = {
    "Thailand":1500,
    "Laos":1200,
    "Vietnam":1700,
    "China":2000
}

print(highest_sales_country(sales_data))