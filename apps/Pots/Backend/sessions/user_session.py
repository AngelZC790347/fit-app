from flask.sessions import SecureCookieSession
from uuid import uuid3,NAMESPACE_OID
class UserSession(SecureCookieSession):
	def __init__(self,key):
		super(UserSession, self).__init__()
		self.key = uuid3(NAMESPACE_OID,key)
	