from console_ui import  ConsoleDbApp
from providers.raw_provider import RawSqlProvider


def main():
    app = ConsoleDbApp(RawSqlProvider,RawSqlProvider)
    app.start_app()

if __name__=='__main__':
    main()
