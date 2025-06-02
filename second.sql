SELECT track, 
    CASE 
        WHEN finished == true THEN 2
        WHEN canсelled == true THEN -1
        WHEN inDelivery == true THEN 1
        ELSE 0
    END
FROM "Orders"