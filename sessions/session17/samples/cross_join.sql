SELECT
	C.customer_id,
	C.first_name,
	C.last_name,
	a.address_id,
	a.address,
	a.district,
	CI.city,
	CO.country
FROM
	CUSTOMER AS C,
	ADDRESS AS A,
	CITY AS CI,
	COUNTRY AS CO
WHERE
	C.address_id = a.address_id
	AND ci.city_id = a.city_id
	AND a.district ILIKE '%esfahan%'
	AND co.country_id = ci.country_id
ORDER BY
	C.CUSTOMER_ID,
	A.ADDRESS_ID