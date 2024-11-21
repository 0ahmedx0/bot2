
# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27361100"))
API_HASH = getenv("API_HASH", "70f07944c80e1e52784f14cfe49f37fa")
BOT_TOKEN = getenv("BOT_TOKEN", "7822077170:AAHpdjQIfh2SZl0wbx_Seb8RtTlWE7FbVlg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6419499019").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb://ahmedalsaltani30:ahmedabcd074@cluster0-shard-00-00.quu8v.mongodb.net:27017,cluster0-shard-00-01.quu8v.mongodb.net:27017,cluster0-shard-00-02.quu8v.mongodb.net:27017/?ssl=true&replicaSet=atlas-s98j2a-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002293967199")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002293967199"))
