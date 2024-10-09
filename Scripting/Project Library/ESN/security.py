def logUserLastLogin(id):
	logger = system.util.getLogger("myLogger")
	logger.info("Hello, world.")
	logger.info(id)	
	query = """INSERT INTO ign_user_ex (id,user_id, prop_name, prop_value)
	VALUES (?,?, 'lastlogin', now())
	ON CONFLICT(id) 
	DO UPDATE SET
	  prop_value = now()"""
	
	system.db.runPrepUpdate(query, [int(id),int(id)], 'Administration')

def changeUserPassword(email,password):

	from com.inductiveautomation.ignition.common.util import SecurityUtils
	
	SHA1 = SecurityUtils.sha1String(password)
	query = "UPDATE ign_users SET passwd=? WHERE username=?"
	system.db.runPrepUpdate(query, [SHA1, email],'Administration')

	return password
