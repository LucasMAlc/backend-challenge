SELECT 
     u.id AS user_id,
     u.name AS user_name,
     u.email AS user_email,
     r.description AS role_description,
     c.description AS claim_description
 FROM 
     users u
 INNER JOIN 
     roles r ON u.role_id = r.id
 LEFT JOIN 
     user_claims uc ON u.id = uc.user_id
 LEFT JOIN 
     claims c ON uc.claim_id = c.id AND c.active = true
 ORDER BY 
     u.name, c.description;