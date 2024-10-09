INSERT INTO ign_user_ex (user_id, prop_name, prop_value)
VALUES (:userid, 'lastlogin', now())
ON CONFLICT(user_id) 
DO UPDATE SET
  prop_value = now(),
  WHERE prop_name = 'lastlogin'
