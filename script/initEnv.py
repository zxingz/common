import os
import telegram

class env():

    def __init__(self, module):
        os.environ['APP_BASE'] = '/'.join(os.environ.get('PWD').split('/')[:-2])
        if not os.path.exists(os.environ.get('APP_BASE')+'/log/common/'):
            os.makedirs(os.environ.get('APP_BASE')+'/log/common/')
        self.commonLogger = self.setupLogger(os.environ.get('APP_BASE') + '/log/common/initEnv.log', 'common')
        self.commonLogger.info('setting environment variables...')
        try:
            self.module = module.split('/')[-3]
            self.script = module.split('/')[-1]
            if self.script.find('.') != -1:
                self.script = self.script[:self.script.find('.')]
            os.environ['MODULE_NAME'] = self.script
            os.environ['LOG_BASE'] = os.environ.get('APP_BASE') + '/log/' + self.module
            if not os.path.exists(os.environ.get('LOG_BASE')):
                os.makedirs(os.environ.get('LOG_BASE'))
            os.environ['DATA_BASE'] = os.environ.get('APP_BASE') + '/data/' + self.module
            if not os.path.exists(os.environ.get('DATA_BASE')):
                os.makedirs(os.environ.get('DATA_BASE'))
            self.commonLogger.info('setting script logger: '+os.environ.get('LOG_BASE') + '/' + self.script + '.log')
            self.scriptLogger = self.setupLogger(os.environ.get('LOG_BASE') + '/' + self.script + '.log', self.script)
            self.bot = telegram.Bot(token='392833384:AAHY326OuYKdXk5D6oXtlwND0bACqB87FNQ')
        except Exception as error:
            self.commonLogger.info('Error occured in common: '+str(error))

    def setupLogger(self, file, name):
        import logging
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
        handler = logging.FileHandler(file)
        handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)
        return logger

    def ret(self):
        return self.scriptLogger, self.bot
