SELECT
	C.customer_id,
	C.first_name,
	C.last_name,
	a.address_id,
	a.address,
	a.district,
	CI.city
	-- CO.country
FROM
	CUSTOMER AS C
	JOIN ADDRESS AS A ON C.ADDRESS_ID = A.ADDRESS_ID
	JOIN CITY AS CI ON CI.CITY_ID = A.CITY_id
WHERE
	A.DISTRICT ILIKE '%esfahan%'
ORDER BY
C.CUSTOMER_ID,A.ADDRESS_ID