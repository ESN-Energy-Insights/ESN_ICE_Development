SELECT c.mqtt_topic as value,c.company_name as label FROM company c
inner join ign_roles r
on r.role_name  = c.mqtt_topic
inner join ign_user_rl rl
on rl.role_id  = r.id 
inner join ign_users u
on u.id  = rl.user_id 
and u.username = :username
order by company_name
