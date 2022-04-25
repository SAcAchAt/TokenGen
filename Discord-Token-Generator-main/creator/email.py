import requests, time

class email:
    def checkEmail(self):
        response = requests.get('https://api.kopeechka.store/mailbox-get-message' + self.id + '&token=' + self.emailAPI).json()
        return response['value']

    def deleteEmail(self):
        requests.get('https://api.kopeechka.store/mailbox-cancel?id=' + self.id + '&token=' + self.emailAPI)

    def waitForEmail(self):
        tries = 0
        while tries < 30:
            time.sleep(2)
            value = self.checkEmail()
            if value != 'WAIT_LINK':
                self.deleteEmail()
                return value.replace('\\', '')
            tries += 1
        return False

    def __init__(self, emailAPI) -> None:
        self.emailAPI = emailAPI
        response = requests.get('https://api.kopeechka.store/mailbox-get-email?api=1.0&spa=1&site=discord.com&sender=discord' + self.emailAPI).json()
        if response['status'] == 'OK':
            self.id = response['Username']
            self.email = response['mail']
        else:
            Exception(response)
