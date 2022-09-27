import json

from django.db import models


class Account(models.Model):
    currency = models.CharField(max_length=3)
    name = models.CharField(max_length=30)


# class ResponseAccountAdded:
#     def __init__(self, account_id):
#         self.code = "OK"
#         self.id = account_id
#
#     def toJSON(self):
#         return json.dumps(self.__dict__)
#
#
# class ResponseAccountDeleted:
#     def __init__(self, account_id):
#         self.code = "OK"
#         self.id = account_id
#
#     def toJSON(self):
#         return json.dumps(self.__dict__)
#
#
# class ResponseError:
#     def __init__(self, message):
#         self.code = "Error"
#         self.message = message
#
#     def toJSON(self):
#         return json.dumps(self.__dict__)
#
#
# class Database:
#     def __init__(self):
#         self.accounts = []
