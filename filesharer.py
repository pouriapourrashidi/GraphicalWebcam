from filestack import Client


class FileSharer:

    def __init__(self, filePath, apiKey="AdYBYg9A1QqfJzSxELekqz"):
        self.filePath = filePath
        self.apiKey = apiKey

    def share(self):
        client = Client(self.apiKey)
        fileLink = client.upload(filepath=self.filePath)
        return fileLink.url

