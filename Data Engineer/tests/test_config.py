from config.config import settings

print("Host      :", settings.DB_HOST)
print("Database  :", settings.DB_NAME)
print("Schema    :", settings.SCHEMA_RAW)
print("CSV File  :", settings.SOURCE_FILE)