# https://github.com/odysseusmax/animated-lamp/blob/master/bot/database/database.py
import motor.motor_asyncio
from info import DATABASE_NAME, DATABASE_URI, DATABASE_URI2, DATABASE_NAME2, IMDB, IMDB_TEMPLATE, MELCOW_NEW_USERS, P_TTI_SHOW_OFF, SINGLE_BUTTON, SPELL_CHECK_REPLY, PROTECT_CONTENT

class Database2: 
  
     def __init__(self, uri2, database_name2): 
         self._client = motor.motor_asyncio.AsyncIOMotorClient(uri2) 
         self.db2 = self._client[database_name2] 
         self.col2 = self.db2.users 
         self.grp2 = self.db2.groups 
  
  
     def new_user(self, id, name): 
         return dict( 
             id = id, 
             name = name, 
             ban_status=dict( 
                 is_banned=False, 
                 ban_reason="", 
             ), 
         ) 
  
  
     def new_group(self, id, title): 
         return dict( 
             id = id, 
             title = title, 
             chat_status=dict( 
                 is_disabled=False, 
                 reason="", 
             ), 
         ) 
      
     async def add_user(self, id, name): 
         user = self.new_user(id, name) 
         await self.col2.insert_one(user) 
      
     async def is_user_exist(self, id): 
         user = await self.col2.find_one({'id':int(id)}) 
         return bool(user) 
      
     async def total_users_count(self): 
         count = await self.col2.count_documents({}) 
         return count 
      
     async def remove_ban(self, id): 
         ban_status = dict( 
             is_banned=False, 
             ban_reason='' 
         ) 
         await self.col2.update_one({'id': id}, {'$set': {'ban_status': ban_status}}) 
      
     async def ban_user(self, user_id, ban_reason="No Reason"): 
         ban_status = dict( 
             is_banned=True, 
             ban_reason=ban_reason 
         ) 
         await self.col2.update_one({'id': user_id}, {'$set': {'ban_status': ban_status}}) 
  
     async def get_ban_status(self, id): 
         default = dict( 
             is_banned=False, 
             ban_reason='' 
         ) 
         user = await self.col2.find_one({'id':int(id)}) 
         if not user: 
             return default 
         return user.get('ban_status', default) 
  
     async def get_all_users(self): 
         return self.col2.find({}) 
      
  
     async def delete_user(self, user_id): 
         await self.col2.delete_many({'id': int(user_id)}) 
  
  
     async def get_banned(self): 
         users = self.col2.find({'ban_status.is_banned': True}) 
         chats = self.grp2.find({'chat_status.is_disabled': True}) 
         b_chats = [chat['id'] async for chat in chats] 
         b_users = [user['id'] async for user in users] 
         return b_users, b_chats 
      
  
  
     async def add_chat(self, chat, title): 
         chat = self.new_group(chat, title) 
         await self.grp2.insert_one(chat) 
      
  
     async def get_chat(self, chat): 
         chat = await self.grp2.find_one({'id':int(chat)}) 
         return False if not chat else chat.get('chat_status') 
      
  
     async def re_enable_chat(self, id): 
         chat_status=dict( 
             is_disabled=False, 
             reason="", 
             ) 
         await self.grp2.update_one({'id': int(id)}, {'$set': {'chat_status': chat_status}}) 
          
     async def update_settings(self, id, settings): 
         await self.grp2.update_one({'id': int(id)}, {'$set': {'settings': settings}}) 
          
      
     async def get_settings(self, id): 
         default = { 
             'button': SINGLE_BUTTON, 
             'botpm': P_TTI_SHOW_OFF, 
             'file_secure': PROTECT_CONTENT, 
             'imdb': IMDB, 
             'spell_check': SPELL_CHECK_REPLY, 
             'welcome': MELCOW_NEW_USERS, 
             'template': IMDB_TEMPLATE
         }
         chat = await self.grp2.find_one({'id':int(id)}) 
         if chat: 
             return chat.get('settings', default) 
         return default 
      
  
     async def disable_chat(self, chat, reason="No Reason"): 
         chat_status=dict( 
             is_disabled=True, 
             reason=reason, 
             ) 
         await self.grp2.update_one({'id': int(chat)}, {'$set': {'chat_status': chat_status}}) 
      
  
     async def total_chat_count(self): 
         count = await self.grp2.count_documents({}) 
         return count 
  
     async def get_all_chats(self): 
         return self.grp2.find({}) 
      
     async def get_2db_size(self):
        return (await self.db2.command("dbstats"))['dataSize']
db2 = Database2(DATABASE_URI2, DATABASE_NAME2)

class Database1:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db1 = self._client[database_name] 
        self.col = self.db1.users

    async def get_1db_size(self):
        return (await self.db1.command("dbstats"))['dataSize']


db1 = Database1(DATABASE_URI, DATABASE_NAME)
