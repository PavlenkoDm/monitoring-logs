import sentry_sdk

sentry_sdk.init(
    dsn="https://2f38506062126d3bda35dcdd9d2fe981@o4510517349908480.ingest.de.sentry.io/4510517440544848",
    send_default_pii=True,
)

try:
    division_by_zero = 1 / 0
except Exception as e:
    sentry_sdk.capture_exception(e)
    print("Ошибка отправлена в Sentry!")

print("Скрипт завершён. Перейти в Sentry через 10-20 секунд.")